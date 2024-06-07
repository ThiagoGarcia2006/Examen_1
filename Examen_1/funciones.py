import csv
import json
import random

def get_path_actual(nombre_archivo):
    import os 
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def cargar_csv(nombre_archivo):
    with open(get_path_actual(nombre_archivo), mode="r", newline="", encoding="utf-8") as archivo:
        datos = []
        encabezado = archivo.readline().strip("\n").split(",")  
        for linea in archivo:
            fila = {}
            valores = linea.strip("\n").split(",")  
            for i, valor in enumerate(valores):
                fila[encabezado[i]] = valor  
            fila["likes"] = int(fila["likes"])
            fila["dislikes"] = int(fila["dislikes"])
            fila["followers"] = int(fila["followers"])
            datos.append(fila)
    print("Se a cargado con exito")           
    return datos

def mapeo_lista(datos:list):
    for fila in datos:
        print(fila)

def asignar_estadisticas(datos):
    for post in datos:
        post["likes"] = random.randint(500, 3000)
        post["dislikes"] = random.randint(300, 3500)
        post["followers"] = random.randint(10000, 20000)

def filtrar_mejores_posts(datos):
    return list(filter(lambda post: post["likes"] > 2000, datos))

def filtrar_haters(datos):
    return list(filter(lambda post: post["dislikes"] > post["likes"], datos))

def promedio_followers(datos):
    total_followers = sum(post["followers"] for post in datos)
    return total_followers / len(datos) if datos else 0

def ordenar_por_usuario(datos):
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if datos[j]["user"] > datos[j + 1]["user"]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos

def guardar_en_json(datos, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

def mas_popular(datos):
    if not datos:
        return [], 0
    
    max_likes = datos[0]["likes"]
    for post in datos:
        if post["likes"] > max_likes:
            max_likes = post["likes"]
    
    usuarios_populares = [post["user"] for post in datos if post["likes"] == max_likes]
    return usuarios_populares, max_likes


