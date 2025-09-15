import pixeltable as pxt
from pixeltable.functions.ollama import chat

print("Creando pipeline de RAG...")

print("Entrada de queries...")

pxt.create_table('pixeltable_db.queries_t', schema={
    'Question': pxt.String
})

docs_chunks = pxt.get_table('pixeltable_db.docs_chunks')


@pxt.query
def top_k(query_text: str):
    sim = docs_chunks.text.similarity(query_text)
    return (
        docs_chunks.order_by(sim, asc=False)
            .select(docs_chunks.text, sim=sim)
            .limit(5)
    )

queries_t = pxt.get_table('pixeltable_db.queries_t')

queries_t.add_computed_column(
    question_context=top_k(queries_t.Question)
)

print("Creando prompts y respuestas...")

@pxt.udf
def create_prompt(top_k_list: list[dict], question: str) -> str:
    concat_top_k = '\n\n'.join(
        elt['text'] for elt in reversed(top_k_list)
    )
    return f"""
    PASSAGES:

    {concat_top_k}

    QUESTION:

    {question}
    """

queries_t = pxt.get_table('pixeltable_db.queries_t')

queries_t.add_computed_column(
    prompt=create_prompt(queries_t.question_context, queries_t.Question)
)

# Preparamos los mensajes para Ollama
messages = [
    {
        'role': 'system',
        'content': 'Please read the following passages and answer the question based on their contents.'
    },
    {
        'role': 'user',
        'content': queries_t.prompt
    }
]

# Llamamos al modelo de Ollama (por ej. llama3)
queries_t.add_computed_column(
    output=chat(
        messages=messages,
        model='llama3',
        options={'max_tokens': 300, 'temperature': 0.5}
    )
)

# Extraemos solo el texto de la respuesta
queries_t.add_computed_column(
    answer=queries_t.output.message.content
)

print("Pipeline de RAG creado.")