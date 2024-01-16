def save_file():
    try:
        with open('../data/noticias_' + categoria_scraping + '.csv', 'a') as f:
            f.write(titulo + ',' + url_noticia + ',' + categoria + ',' + str(
                fecha) + '\n')
        # Analizar el contenido con BeautifulSoup
    except:
        print("ERROR: no se pudo anexar la noticia al archivo noticias.csv")