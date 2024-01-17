def save_clasification_file(equipos, year):
    try:
        with open('../Data/clasificacion.csv', 'a') as f:
            # for i, equipo in enumerate(equipos, 1):
            #     f.write(f"{i}, {equipo.nombre}, {equipo.puntos}\n")

            # Escribir encabezados solo si el archivo está vacío
            if f.tell() == 0:
                f.write("Posicion, Nombre, Puntos\n")

            # Iterar sobre los equipos y escribir los datos en columnas diferentes
            for i, equipo in enumerate(equipos, 1):
                f.write(f"{i}, {equipo.nombre}, {equipo.puntos}\n")


    except Exception as e:
        print(f"ERROR: no se pudo anexar los equipos a clasificacion_{year}.csv. Error: {e}")