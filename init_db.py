import pixeltable as pxt

print("Inicializando la base de datos...")
# Directorio de la base de datos
pxt.drop_dir("pixeltable_db", force=True)
pxt.create_dir("pixeltable_db")

# Estrucura de la base de datos
docs = pxt.create_table('pixeltable_db.docs', {
    'filename': pxt.String,
    'content': pxt.Document
})

docs.insert([
    {'filename': 'codigo_penal_juvenil_libro_1', 'content': 'docs/codigo_penal_juvenil_libro_1.pdf'},
    {'filename': 'codigo_penal_libro_1', 'content': 'docs/codigo_penal_libro_1.pdf'}
])
print("Base de datos inicializada.")