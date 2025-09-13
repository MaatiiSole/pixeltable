import pixeltable as pxt

# libros = pxt.create_table('libros', {

#     'titulo': pxt.String,
#     'autor': pxt.String,
#     'portada': pxt.Image
# })

libros = pxt.get_table('libros')

# libros.insert([
#     {'titulo': '1984', 'autor': 'George Orwell', 'portada': 'Images/prueba1.png'},
#     {'titulo': 'Constitución Argentina', 'autor': 'Juan Bautista Alberdi', 'portada': 'Images/prueba2.jpg'}
# ])

res = libros.where(libros.autor == 'George Orwell').collect()

print("Resultado consulta:", res)