# Desafío #02:
# Usando como base lo realizado en el anterior desafío realizar los siguientes
# informes en un menú
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
# género NB
# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia
# NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú
from data_stark import lista_personajes

#from funciones import *

def mostrar_nb():
    for i in range(len(lista_personajes)):
        nombre = lista_personajes[i]['nombre']
        genero = lista_personajes[i]['genero']
        if genero == "NB":
            print(f"{nombre}")


def mas_alto_f():
    mas_alto_f = 0
    for i in range(len(lista_personajes)):
        nombre = lista_personajes[i]['nombre']
        genero = lista_personajes[i]['genero']
        altura = float(lista_personajes[i]['altura'])
        if genero == "F" and altura > mas_alto_f:
            mas_alto_f = altura
            nombre_mas_alto_f = nombre
    print(f"El superheroe mas alto femenino es: {nombre_mas_alto_f}")

def mas_alto_m(): 
    mas_alto_m = 0
    for i in range(len(lista_personajes)):
        nombre = lista_personajes[i]['nombre']
        genero = lista_personajes[i]['genero']
        altura = float(lista_personajes[i]['altura'])
        if genero == "M" and altura > mas_alto_m:
            mas_alto_m = altura
            nombre_mas_alto_m = nombre
    print(f"El superheroe mas alto femenino es: {nombre_mas_alto_m}")

def mas_debil_m():
        heroe_mas_debil_m = 0
        nombre_mas_debil_m = None
        for i in range(len(lista_personajes)):
            nombre = lista_personajes[i]['nombre']
            genero = lista_personajes[i]['genero']
            fuerza = int(lista_personajes[i]['fuerza'])
            if genero == "M": 
                if heroe_mas_debil_m == 0 or fuerza < heroe_mas_debil_m:
                    heroe_mas_debil_m = fuerza
                    nombre_mas_debil_m = nombre
        print(f"El heroe mas debil masculino {nombre_mas_debil_m}")

def mas_debil_nb():
        heroe_mas_debil_nb = 0
        nombre_mas_debil_nb = None
        for i in range(len(lista_personajes)):
            nombre = lista_personajes[i]['nombre']
            genero = lista_personajes[i]['genero']
            fuerza = int(lista_personajes[i]['fuerza'])
            if genero == "NB": 
                if heroe_mas_debil_nb == 0 or fuerza < heroe_mas_debil_nb:
                    heroe_mas_debil_nb = fuerza
                    nombre_mas_debil_nb = nombre
        print(f"El heroe mas debil masculino {nombre_mas_debil_nb}")

def fuerza_promedio_nb():
        contador_fuerza_nb = 0
        acumulador_fuerza_nb = 0
        for i in range(len(lista_personajes)):
            genero = lista_personajes[i]['genero']
            fuerza = int(lista_personajes[i]['fuerza'])
            if genero == "NB":
                contador_fuerza_nb += 1
                acumulador_fuerza_nb += fuerza
        promedio_nb = acumulador_fuerza_nb/contador_fuerza_nb
        print(f"La fuerza promedio de los nb es: {promedio_nb:.2f}")

def contar_colores_ojos(lista_personajes):
    colores_ojos = {}  
    for personaje in range(len(lista_personajes)):
        color_ojos = personaje['color_ojos']
        if color_ojos in colores_ojos:
            colores_ojos[color_ojos] += 1
        else:
            colores_ojos[color_ojos] = 1
    for color, cantidad in colores_ojos.items():
        print(f"Color de ojos '{color}': {cantidad} superhéroes")

def contar_colores_pelo(lista_personajes):
    colores_pelo = {}
    for personaje in range(len(lista_personajes)):        
        color_pelo = personaje["color_pelo"]
        if color_pelo in colores_pelo:
            colores_pelo[color_pelo] += 1
        else:
            colores_pelo[color_pelo] = 1
    for color, cantidad in colores_pelo.items():
        print(f"{color}: {cantidad}")
     
def mostrar_listas_ojos(lista:list):
    heroes_ojos_Red = []
    heroes_ojos_Brown = []
    heroes_ojos_Yellow = []
    heroes_ojos_Yellow_without_irises = []
    heroes_ojos_Blue = []
    heroes_ojos_Green = []
    heroes_ojos_Hazel = []
    heroes_ojos_Silver = []
    for i in range(len(lista)):
        color_ojos = lista[i]["color_ojos"]
        nombre_super = lista[i]["nombre"]
        match color_ojos:
            case "Brown":
                heroes_ojos_Brown.append(nombre_super)
            case "Yellow":
                heroes_ojos_Yellow.append(nombre_super)
            case "Yellow (without irises)":
                heroes_ojos_Yellow_without_irises.append(nombre_super)
            case "Blue":
                heroes_ojos_Blue.append(nombre_super)
            case "Green":
                heroes_ojos_Green.append(nombre_super)
            case "Hazel":
                heroes_ojos_Hazel.append(nombre_super)
            case "Silver":
                heroes_ojos_Silver.append(nombre_super)
            case "Red":
                heroes_ojos_Red.append(nombre_super)
    print(f"{heroes_ojos_Blue} tienen color azul \n{heroes_ojos_Brown} tienen color marron \n{heroes_ojos_Green} tienen color verde \n{heroes_ojos_Red} tiene el color rojo \n{heroes_ojos_Hazel} tienen color avellana \n{heroes_ojos_Silver} tienen color Plata \n{heroes_ojos_Yellow} tienen color amarillo \n{heroes_ojos_Yellow_without_irises} tienen color Amarillo sin iris")


def mostrar_listas_inteligencia(lista:list):
    high = []
    average = []
    good = []
    nada = []
    for i in range(len(lista)):
        inteligencia = lista[i]["inteligencia"]
        nombre_super = lista[i]["nombre"]
        match inteligencia:
            case "high":
                high.append(nombre_super)
            case "average":
                average.append(nombre_super)
            case "good":
                good.append(nombre_super)
            case "":
                nada.append(nombre_super)
    print(f"{high} tienen nivel de inteligencia alta \n{average} tienen nivel de inteligencia promedio \n{good} tienen nivel de inteligencia buena \n{nada} tiene niuvel de inteligencia nulo")





while True:
    opciones = input("\nA (nombre de cada superhéroe de género NB  e)\nB (superhéroe más alto de género F)\nC (superhéroe más alto de género M)\nD (Recorrer la lista y determinar cuál es el superhéroe más débil de género M)\nE (cuál es el superhéroe más débil de género NB)\nF (fuerza promedio de los superhéroes de género NB) \nG(cuántos superhéroes tienen cada tipo de color de ojos.)\nH(cuántos superhéroes tienen cada tipo de color de pelo.)\nI(superhéroes agrupados por color de ojos.)\nJ(uperhéroes agrupados por tipo de inteligencia):")

    if opciones == "A":
            mostrar_nb()
    elif opciones == "B":
            mas_alto_f()
    elif opciones == "C":
            mas_alto_m()
    elif opciones == "D":
            mas_debil_m()
    elif opciones == "E":
            mas_debil_nb()
    elif opciones == "F":
            fuerza_promedio_nb()
    elif opciones == "G":
            contar_colores_ojos()
    elif opciones == "H":
            contar_colores_pelo()
    elif opciones == "I":
            mostrar_listas_ojos()
    elif opciones == "J":
            mostrar_listas_inteligencia()


