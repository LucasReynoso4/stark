# A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
# B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
# fuerza (MÁXIMO)
# C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
# (MÍNIMO)
# D. Recorrer la lista y determinar el peso promedio de los superhéroes
# masculinos (PROMEDIO)
# E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
# género) los cuales su fuerza supere a la fuerza promedio de todas las
# superhéroes de género femenino

from data_stark import lista_personajes


def mostrar_datos_heroes():
    for heroe in lista_personajes:
        print(f"Nombre: {heroe['nombre']}, Identidad: {heroe['identidad']}, Género: {heroe['genero']}, Peso: {float(heroe['peso']):.2f}, Fuerza: {heroe['fuerza']}")


while True:
    opciones = input("\nA (Datos de cada superhéro  e)\nB (Identidad y peso del superhéroe con mayor fuerza)\nC (Nombre e identidad del superhéroe más bajo)\nD (Peso promedio de los super héroes masculinos)\nE (Nombre y peso de los superhéroes cuales supete la fuerza promedio de las superheroes femeninas)\nF (para salir) \nseleciones opcion:")

    if opciones == "A":
        mostrar_datos_heroes()
    elif opciones == "B":
        maximo_fuerza = int(lista_personajes[0]['fuerza'])
        for i in range(len(lista_personajes)):
            fuerza = int(lista_personajes[i]['fuerza'])
            identidad = lista_personajes[i]['identidad']
            peso = lista_personajes[i]['peso']
            if fuerza > maximo_fuerza:
                maximo_fuerza = fuerza
                identidad_fuerza = identidad
                peso_fuerza = peso
        print(f"La identidad del superheroe con mayor fuerza es {identidad_fuerza} y el peso {peso_fuerza}")
    elif opciones == "C":
        menor_bajo_heroe = 10000000000000
        for i in range(len(lista_personajes)):
            identidad = lista_personajes[i]['identidad']
            nombre = lista_personajes[i]['nombre']  
            altura = float(lista_personajes[i]['altura'])
            if altura < menor_bajo_heroe:
                menor_bajo_heroe = altura
                nombre_bajo = nombre
                identidad_bajo = identidad
        print(f"La identidad del superheroe mas bajo es {identidad_bajo} y su nombre {nombre_bajo}")
    elif opciones == "D":
        contador_masculinos = 0
        acumulador_peso = 0
        for i in range(len(lista_personajes)):
            peso = lista_personajes[i]['peso']
            genero = lista_personajes[i]['genero']
            peso = float(peso)
            if genero == "M":
                contador_masculinos += 1
                acumulador_peso += peso
        promedio = acumulador_peso/contador_masculinos
        print(f"El promedio de los superheroes masculinos es de: {promedio}")
    elif opciones == "E":
        contador_femenino = 0
        acumulador_femenino = 0

        for i in range(len(lista_personajes)):
            nombre = lista_personajes[i]["nombre"]
            peso = lista_personajes[i]["peso"]
            fuerza = float(lista_personajes[i]["fuerza"])
        
            if lista_personajes[i]["genero"] == "F":
                contador_femenino += 1
                acumulador_femenino += fuerza

        if contador_femenino != 0:
            promedio_femenino = acumulador_femenino / contador_femenino


            if fuerza > promedio_femenino:
                print(f"El nombre es {nombre} y el peso {peso}")
        else:
            print("No hay personajes femeninos en la lista.")

    elif opciones == "F":
        break
                








