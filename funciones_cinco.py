import os,csv,json
from data_stark import *

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except Exception as e:
        print(f'Error al leer el archivo {nombre_archivo}: {str(e)}')
        return False
    

def guardar_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
        print(f"Se creó el archivo: {nombre_archivo}")
        return True
    except Exception as e:
        print(f"Error al crear el archivo {nombre_archivo}: {str(e)}")
        return False

# Punto 1.3
def generar_csv(nombre_archivo, lista_superheroes):
    if lista_superheroes:
        # Crear el string CSV
        contenido_csv = "nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia\n"
        for heroe in lista_superheroes:
            contenido_csv += f"{heroe['nombre']},{heroe['identidad']},{heroe['empresa']},{heroe['altura']},{heroe['peso']},{heroe['genero']},{heroe['color_ojos']},{heroe['color_pelo']},{heroe['fuerza']},{heroe['inteligencia']}\n"

        # Llamar a la función para guardar el archivo
        return guardar_archivo(nombre_archivo, contenido_csv)
    else:
        print("La lista de superhéroes está vacía.")
        return False

# Punto 1.4
def leer_csv(nombre_archivo):
    try:
        lista_superheroes = []
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for row in lector_csv:
                lista_superheroes.append(row)
        return lista_superheroes
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {str(e)}")
        return False
    

def generar_json(nombre_archivo, lista_superheroes, nombre_lista):
    if lista_superheroes:
        # Normalizar los datos antes de generar el JSON
        lista_normalizada = normalizar_datos(lista_superheroes)

        # Crear un diccionario con una sola clave (nombre_lista)
        diccionario_superheroes = {nombre_lista: lista_normalizada}

        try:
            # Guardar el diccionario como JSON en el archivo con indent=4
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo_json:
                json.dump(diccionario_superheroes, archivo_json, indent=4) 

#indent=4 al generar el JSON: Esta es una opción que puedes proporcionar al método json.dump para formatear el JSON de una manera más legible. Cuando estableces indent=4, el JSON se formatea con sangrías de 4 espacios para hacerlo más fácil de leer.

            print(f"Se creó el archivo JSON: {nombre_archivo}")
            return True
        except Exception as e:
            print(f"Error al crear el archivo JSON {nombre_archivo}: {str(e)}")
            return False
    else:
        print("La lista de superhéroes está vacía.")
        return False
    
def normalizar_datos(lista_superheroes):
    lista_normalizada = []

    for heroe in lista_superheroes:
        try:
            heroe["altura"] = float(heroe["altura"]) if heroe["altura"] else None
            heroe["peso"] = float(heroe["peso"]) if heroe["peso"] else None
            heroe["fuerza"] = int(heroe["fuerza"]) if heroe["fuerza"] else None
        except ValueError as e:
            print(f"Error al convertir valores: {e}. Ignorando este héroe.")
            continue

        lista_normalizada.append(heroe)

    return lista_normalizada


def leer_json(nombre_archivo, nombre_lista):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            retorno = datos.get(nombre_lista, [])
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        retorno = False
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {e}")
        retorno = False
    return retorno


def ordenar_heroes_ascendente(heroes, clave):
    n = len(heroes)
    for i in range(n):
        for j in range(0, n-i-1):
            if float(heroes[j][clave]) < float(heroes[j+1][clave]):
                heroes[j], heroes[j+1] = heroes[j+1], heroes[j]
    return heroes

def ordenar_heroes_descendente(heroes, clave):
    n = len(heroes)
    for i in range(n):
        for j in range(0, n-i-1):
            if float(heroes[j][clave]) > float(heroes[j+1][clave]):
                heroes[j], heroes[j+1] = heroes[j+1], heroes[j]
    return heroes

def ordenar_heroes_por_clave(heroes, clave):
    direccion = input("¿Cómo quieres ordenar los héroes? ('asc' para ascendente, 'desc' para descendente): ").lower()
    
    if direccion == 'asc':
        heroes_ordenados = ordenar_heroes_ascendente(heroes, clave)
    elif direccion == 'desc':
        heroes_ordenados = ordenar_heroes_descendente(heroes, clave)
    else:
        print("Opción no válida. Se devolverá la lista sin ordenar.")
        return heroes

    print(f"Lista de héroes ordenados por {clave.upper()} de manera {direccion.upper()}:")
    for heroe in heroes_ordenados:
        print(heroe)

    return heroes_ordenados
    


