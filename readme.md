## Setup
```bash
python -m venv .env
.env\Scripts\activate.bat
pip install -r requirements.txt

# Download Ollama and run
ollama pull llama3

#Para inicializar pxt correr
init_pxt.py
#Esto falla porque corre la consulta al mismo tiempo que levanta el server
#Esperar y correrlo nuevamente hasta que funcione xd 
#(tobi arregla esto pls, un .py que solo levante el server asi no rompe nada)
#Esto directamente de los notebooks no funciona, si o si desde aca primero

# Init database
python init_db.py
# Create chunks
python chunking.py
# Create embeddings
python embeddings.py
# Create RAG
python rag_pipeline.py


# Documentation
https://github.com/pixeltable/pixeltable/blob/release/docs/notebooks/use-cases/rag-demo.ipynb