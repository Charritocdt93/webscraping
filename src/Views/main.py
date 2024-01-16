from datetime import datetime

from src.Services.web_scraping_services import SelectWebScraping

if __name__ == '__main__':

    def mostrar_menu():
        print("1. Clasificación La Liga")
        print("2. Partidos Destacados de hoy")
        print("3. Top 15 Jugadores")
        print("4. Top 15 Jugadores Sub21")
        print("5. Salir")

    # Ciclo principal del menú
    try:
        # Ciclo principal del menú
        while True:
            mostrar_menu()

            try:
                opcion = int(input("Seleccione una opción (1-5): "))

                SelectWebScraping(opcion)

                if 1 <= opcion <= 4:
                    SelectWebScraping(opcion)
                elif opcion == 5:
                    print("Saliendo del programa. ¡Hasta luego!")
                    break
                else:
                    print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

            except ValueError:
                print("Error: Ingrese un número entero.")

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
