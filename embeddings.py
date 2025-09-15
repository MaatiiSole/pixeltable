import pixeltable as pxt
from pixeltable.functions.huggingface import sentence_transformer

print("Agregando embeddings...")

docs_chunks = pxt.get_table('pixeltable_db.docs_chunks')

# Embedding con CLIP (modelo base, livianito y rápido)
docs_chunks.add_embedding_index(
    'text',
    embedding=sentence_transformer.using(model_id='sentence-transformers/all-MiniLM-L6-v2')
)

# Si te la bancas con el large:

# docs_chunks.add_embedding_index(
#     'text',
#     embedding=sentence_transformer.using(model_id='intfloat/e5-large-v2')
# )

print("Embeddings agregados.")