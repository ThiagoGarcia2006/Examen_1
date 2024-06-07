from funciones import *

datos = []
while True:
    print("\nMenu de opciones:")
    print("1) Cargar archivo CSV")
    print("2) Imprimir lista")
    print("3) Asignar estadisticas")
    print("4) Filtrar por mejores posts")
    print("5) Filtrar por haters")
    print("6) Informar promedio de followers")
    print("7) Ordenar los datos por nombre de usuario ascendente")
    print("8) Mostrar mas popular")
    print("9) Salir")
        
    opcion = input("Seleccione una opcion: ")
        
    if opcion == "1":
        nombre_archivo = "archivo.csv"
        datos = cargar_csv(nombre_archivo)
    elif opcion == "2":
        mapeo_lista(datos)
    elif opcion == "3":
        asignar_estadisticas(datos)
        print("Estadisticas asignadas.")
    elif opcion == "4":
        mejores_posts = filtrar_mejores_posts(datos)
        archivo_salida = "mejores_posts.csv"
        with open(archivo_salida, "w", newline="", encoding="utf-8") as archivo:
            archivo.write(",".join(datos[0].keys()) + "\n")
            for post in mejores_posts:
                archivo.write(",".join(map(str, post.values())) + "\n")
        print(f"Archivo {archivo_salida} generado con los mejores posts.")
    elif opcion == "5":
        posts_haters = filtrar_haters(datos)
        archivo_salida = "haters_posts.csv"
        with open(archivo_salida, "w", newline="", encoding="utf-8") as archivo:
            archivo.write(",".join(datos[0].keys()) + "\n")
            for post in posts_haters:
                archivo.write(",".join(map(str, post.values())) + "\n")
        print(f"Archivo {archivo_salida} generado con los posts de haters.")
    elif opcion == "6":
        promedio = promedio_followers(datos)
        print(f"El promedio de followers es: {promedio:.2f}")
    elif opcion == "7":
        datos_ordenados = ordenar_por_usuario(datos)
        archivo_salida = "datos_ordenados.json"
        guardar_en_json(datos_ordenados, archivo_salida)
        print(f"Archivo {archivo_salida} generado con los datos ordenados.")
    elif opcion == "8":
        usuarios, max_likes = mas_popular(datos)
        print(f"El post mas likeado tiene {max_likes} likes y es del siguiente usuario: {usuarios}")
    elif opcion == "9":
        print("Saliendo...")
        break
    else:
        print("Opcion invalida. Intente de nuevo.")




