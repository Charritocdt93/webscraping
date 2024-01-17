import pandas as pd
import matplotlib.pyplot as plt

def mostrar_grafico_clasificacion():
    try:
        # Paso 1: Abrir el archivo CSV con pandas
        archivo = '../Data/clasificacion.csv'

        try:
            datos = pd.read_csv(archivo, encoding='utf-8')
        except UnicodeDecodeError:
            # Si hay un error de decodificación, intenta con otras codificaciones
            try:
                datos = pd.read_csv(archivo, encoding='latin1').rename(columns=lambda x: x.strip())
            except UnicodeDecodeError:
                # Intenta con otras codificaciones según sea necesario
                datos = pd.read_csv(archivo, encoding='ISO-8859-1')


        plt.scatter(datos['Puntos'], datos['Nombre'])

        plt.title('Gráfico de dispersión de Equipos vs Puntos')
        plt.xlabel('Equipos')
        plt.ylabel('Puntos')
        plt.show()

    except Exception as e:
        print("Error durante la visualizacion:", e)


