import requests
from bs4 import BeautifulSoup

from src.Models.Team import Team

from datetime import datetime

from src.Services.file_services import save_clasification_file


def SelectWebScraping(opc):
    # Ciclo principal del menú
    try:
        try:
            if opc == 1:
                year = int(input("Introduzca una año: "))
                url = f"https://es.besoccer.com/competicion/clasificacion/primera/{year}"
                Clasificacion(url,year)
            elif opc == 2:
                date = input("Introduzca una fecha (formato: YYYY-MM-DD): ")
                try:
                    fecha = datetime.strptime(date, "%Y-%m-%d")
                    url = f"https://es.besoccer.com/livescore/{fecha.date()}"
                    # Match_dates(url)
                except ValueError:
                    print("Formato de fecha incorrecto. Utiliza el formato YYYY-MM-DD.")
            elif opc == 3:
                year = int(input("Seleccione una año: "))
                url = f"https://es.besoccer.com/competicion/clasificacion/primera/{year}"
                Clasificacion(url,year)
            elif opc == 4:
                year = int(input("Seleccione una año: "))
                url = f"https://es.besoccer.com/competicion/clasificacion/primera/{year}"
                Clasificacion(url, year)
            elif opc == 5:
                print("Saliendo del programa. ¡Hasta luego!")
        except:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")


def Clasificacion(url, year):
    try:
        # Realizar una solicitud HTTP para obtener el contenido de la página web
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Crear un objeto BeautifulSoup para analizar el contenido HTML de la página
            soup = BeautifulSoup(response.text, 'html.parser')

            # Encontrar el div con id="tab_total0" y class="tab-content active"
            clasificacion = soup.find('div', id='tab_total0')

            if clasificacion:
                # Buscar y obtener datos de las etiquetas anidadas dentro de div_total0
                etiquetas_nombre = clasificacion.find_all('span', class_='team-name')
                etiquetas_puntos = clasificacion.find_all('td', class_='green bold br-l')

                # Verificar que la cantidad de etiquetas nombre y puntos sea la misma
                if len(etiquetas_nombre) == len(etiquetas_puntos):
                    # Crear una lista de objetos Team con los datos de las etiquetas
                    equipos = []

                    for nombre, puntos in zip(etiquetas_nombre, etiquetas_puntos):
                        nombre_equipo = nombre.text.strip()
                        puntos_equipo = puntos.text.strip()
                        equipo = Team(nombre_equipo, 1, puntos_equipo)
                        equipos.append(equipo)

                    # Imprimir los datos de los objetos Team
                    for i, equipo in enumerate(equipos, 1):
                        print(f"{i} - {equipo.nombre}, Puntos: {equipo.puntos}")

                    save_clasification_file(equipos, year)

                else:
                    print(
                        "La cantidad de etiquetas 'team-name' no coincide con la cantidad de etiquetas "
                        "'green bold br-l'")
            else:
                print("No se encontró el div con id='tab_total0' y class='tab-content active'")

            # # Aquí puedes realizar operaciones de web scraping utilizando BeautifulSoup
            # # Por ejemplo, imprimir el título de la página
            # print("Título de la página:", soup.title.text)

        else:
            print("Error al realizar la solicitud. Código de estado:", response.status_code)

    except Exception as e:
        print("Error durante el web scraping:", e)

# def Match_dates(url):
#     try:
#         # Realizar una solicitud HTTP para obtener el contenido de la página web
#         response = requests.get(url)
#
#         # Verificar si la solicitud fue exitosa (código de estado 200)
#         if response.status_code == 200:
#             # Crear un objeto BeautifulSoup para analizar el contenido HTML de la página
#             soup = BeautifulSoup(response.text, 'html.parser')
#
#             partidos = soup.find('div', class_='matches mt10')
#
#             if partidos:
#                 midle = partidos.find_all('div', class_='middle-info ta-c')
#                 competicion = partidos.find_all('span', class_='va-m')
#
#                 # # Verificar que la cantidad de etiquetas nombre y puntos sea la misma
#                 # if len(etiquetas_nombre) == len(etiquetas_puntos):
#                 #     # Crear una lista de objetos Team con los datos de las etiquetas
#                 #     equipos = []
#                 #
#                 #     for nombre, puntos in zip(etiquetas_nombre, etiquetas_puntos):
#                 #         nombre_equipo = nombre.text.strip()
#                 #         puntos_equipo = puntos.text.strip()
#                 #         equipo = Team(nombre_equipo, 1, puntos_equipo)
#                 #         equipos.append(equipo)
#                 #
#                 #     # Imprimir los datos de los objetos Team
#                 #     for i, equipo in enumerate(equipos, 1):
#                 #         print(f"{i} - {equipo.nombre}, Puntos: {equipo.puntos}")
#
#                 else:
#                     print(
#                         "La cantidad de etiquetas 'team-name' no coincide con la cantidad de etiquetas "
#                         "'green bold br-l'")
#             else:
#                 print("No se encontró el div con id='tab_total0' y class='tab-content active'")
#         else:
#             print("Error al realizar la solicitud. Código de estado:", response.status_code)
#     except Exception as e:
#         print("Error durante el web scraping:", e)
