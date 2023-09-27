from data_stark import lista_personajes
from funciones import *


normalizado = False

while True:
    opciones = stark_menu_principal()
    if opciones == 1 and normalizado == False:
        if stark_normalizar_datos(lista_personajes):   
            print("Datos normalizados")
            normalizado = True 
    elif opciones == 2 and normalizado:
        imprimir_superheores(lista_personajes, "NB")
    elif opciones == 3 and normalizado:
        mas_alto_f = superheroe_mas_alto_genero(lista_personajes, "F")
        if mas_alto_f:
            print(f"Superhéroe más alto de género F:{ mas_alto_f['nombre']}")
        else:
            print("No se encontraron superhéroes de género F en la lista.")
    elif opciones == 4 and normalizado:
        mas_alto_m = superheroe_mas_alto_genero(lista_personajes, "M")
        if mas_alto_m:
            print(f"Superhéroe más alto de género M: {mas_alto_m['nombre']}")
        else:
            print("No se encontraron superhéroes de género F en la lista.")
    elif opciones == 5 and normalizado:
        mas_debil_m = superheroe_mas_debil_genero(lista_personajes, "M")

        if mas_debil_m:
            print(f"Superhéroe más débil de género M:{mas_debil_m['nombre']}")
        else:
            print("No se encontraron superhéroes de género NB en la lista.") 
            
    elif opciones == 6 and normalizado:
        mas_debil_m = superheroe_mas_debil_genero(lista_personajes, "NB")
        if mas_debil_m:
            print(f"Superhéroe más débil de género NB:{mas_debil_m['nombre']}") 
        else:
            print("No se encontraron superhéroes de género NB en la lista.")
    elif opciones == 7 and normalizado:
        fuerza_promedio_NB = fuerza_promedio_genero_NB(lista_personajes)
        if fuerza_promedio_NB != None:
            print(f"Fuerza promedio de superhéroes de género NB: {fuerza_promedio_NB:.2f}")
        else:
            print("No se encontraron superhéroes de género NB en la lista.")
    elif opciones == 8 and normalizado:
        colores_ojos = contar_atributo(lista_personajes, "color_ojos")
        for color, cantidad in colores_ojos.items():
            print(f"Color de ojos: {color} - Cantidad de superhéroes: {cantidad}")
    elif opciones == 9 and normalizado:
        colores_pelo = contar_atributo(lista_personajes, "color_pelo")
        for color, cantidad in colores_pelo.items():
            print(f"Color de pelo: {color} - Cantidad de superhéroes: {cantidad}")
    
    elif opciones == 10 and normalizado:
        superheroes_agrupados(lista_personajes, "color_ojos")
    
    elif opciones == 11 and normalizado:
        superheroes_agrupados(lista_personajes, "inteligencia")
    elif opciones == 12:
        break


