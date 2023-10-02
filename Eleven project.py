import bs4, requests

# Crear Url sin número de página
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# Lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar paginas
for pagina in range(1,51):

    # Crear Soup en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    soup = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccionar datos de los libros
    libros = soup.select('.product_pod')

    # Iterar en los libros
    for libro in libros:

        # Chequear 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

            # Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # Agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)

# Ver los libros en consola
for t in titulos_rating_alto:
    print(t)