from src.Services.visualizacion import mostrar_grafico_clasificacion
from src.Services.web_scraping_services import SelectWebScraping

if __name__ == '__main__':

    def mostrar_menu():
        print("1. Clasificación La Liga")
        print("2. Partidos Destacados de hoy")
        print("5. Mostrar Grafico Clasificacion")
        print("6. Salir")

    # Ciclo principal del menú
    try:
        # Ciclo principal del menú
        while True:
            mostrar_menu()
            try:
                opcion = int(input("Seleccione una opción (1-6): "))

                if 1 <= opcion <= 4:
                    SelectWebScraping(opcion)
                elif opcion == 5:
                    mostrar_grafico_clasificacion()
                elif opcion == 6:
                    print("Saliendo del programa. ¡Hasta luego!")
                    break
                else:
                    print("Opción no válida. Por favor, ingrese un número del 1 al 6.")
            except ValueError:
                print("Error: Ingrese un número entero.")

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
