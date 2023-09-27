from data_stark import lista_personajes

def stark_normalizar_datos(lista:list) -> bool:
    """
Normaliza los datos de la lista de superhéroes, convirtiendo las alturas y pesos en números flotantes
y la fuerza en números enteros, si es necesario.

Args:
    lista (list): La lista de superhéroes con datos a normalizar.

Returns:
    bool: True si se realizaron cambios en la lista, False si no se realizaron cambios.
"""

    if len(lista) > 0:   
        retorno = 0       
        for elemento in lista:
            if type(elemento['altura']) != type(float()):
                elemento['altura'] = float(elemento['altura'])
                retorno += 1
            if type(elemento['peso']) != type(float()):
                elemento['peso'] = float(elemento['peso'])
            if type(elemento['fuerza']) != type(int()):
                elemento['fuerza'] = int(elemento['fuerza'])
        if retorno > 0:
            return True
        else:
            return False



#Crear la función ”obtener_dato()” la cual recibirá por parámetro un
# diccionario el cual representara a un héroe y también recibirá un string que
# hace referencia a una “clave” del mismo
# Validar siempre que el diccionario no esté vacío y que el mismo tenga una key
# llamada “nombre”. Caso contrario la función retornara un False

def obtener_dato(dicc:dict,key:str):
    """
        Verifica si un diccionario contiene una clave específica.

        Args:
            dicc (dict): El diccionario en el que se buscará la clave.
            key (str): La clave que se desea verificar.

        Returns:
            bool: True si la clave existe en el diccionario, False si no.
        """
    contador = 0
    if dicc == {}:
        return False
    for key in dicc:
        if key == "nombre":
            contador += 1
    if contador == 0 :
        return False
    else:
        return True
    
#     1.2 Crear la función ;obtener_nombre&#; la cual recibirá por parámetro un diccionario el
# cual representara a un héroe y devolverá un string el cual contenga su nombre
# formateado de la siguiente manera:
# Nombre: Howard the Duck
# Validar siempre que el diccionario no este vacío y que la key que se pide exista. Caso
# contrario la función retornara un False
    
def obtener_nombre(dicc:dict):
    """
        Obtiene el nombre de un superhéroe a partir de un diccionario.

        Args:
            dicc (dict): El diccionario que representa a un superhéroe.

        Returns:
            str: El nombre del superhéroe en formato "Nombre: {nombre}" si existe en el diccionario, o False si no.
        """

    if dicc == {}:
        return False
    nombre = obtener_dato(dicc, "nombre")
    if nombre:
        return f"Nombre: {nombre}"
    else:
        return False
    

def obtener_nombre_y_dato(dicc:dict,key:str):
    """
        Obtiene el nombre y un dato específico de un superhéroe a partir de un diccionario.

        Args:
            dicc (dict): El diccionario que representa a un superhéroe.
            key (str): La clave del dato específico que se desea obtener.

        Returns:
            str: Una cadena que combina el nombre del superhéroe y el dato específico si ambos existen en el diccionario,
                o False si el diccionario está vacío o no contiene la clave del nombre.
        """
    if dicc == {}:
        return False
    return f"{obtener_nombre(dicc,) | {key}: {dicc[key]}}"


def obtener_maximo(lista:list, key:str):
    """
Encuentra el valor máximo de un atributo específico en una lista de superhéroes.

Args:
    lista (list): La lista de superhéroes.
    key (str): La clave del atributo para el cual se desea encontrar el valor máximo.

Returns:
    float: El valor máximo encontrado en el atributo especificado.
    False: Si no se pudo encontrar el valor máximo (por ejemplo, si el atributo no es numérico).
"""
    maximo = 0
    for dato in lista:
        if type(dato[key]) == int or type(dato[key]) == float:
            if maximo == None:
                maximo = dato[key]
            elif maximo < dato[key]:
                maximo = dato[key]
        else:
            return False
    return maximo
    
def obtener_minimo(lista:list, key:str):
    """
    Encuentra el valor mínimo de un atributo específico en una lista de superhéroes.

    Args:
        lista (list): La lista de superhéroes.
        key (str): La clave del atributo para el cual se desea encontrar el valor mínimo.

    Returns:
        float: El valor mínimo encontrado en el atributo especificado.
        False: Si no se pudo encontrar el valor mínimo (por ejemplo, si el atributo no es numérico).
    """
    minimo = None
    for dato in lista:
        if type(dato[key]) == int or type(dato[key]) == float:
            if valor_min == None:
                valor_min = dato[key]
            elif valor_min > dato[key]:
                valor_min = dato[key]
        else:
            return False
    return minimo
            


def obtener_dato_cantidad(lista: list, valor: float, key: str)->list:
    """
Obtiene una lista de superhéroes que cumplen con una condición específica en un atributo dado.

Args:
    lista (list): La lista de superhéroes.
    valor (float): El valor que se debe buscar en el atributo especificado.
    key (str): La clave del atributo en el que se buscará el valor.

Returns:
    list: Una lista de superhéroes que cumplen con la condición especificada.
"""
    lista_heroes = []
    max_valor = obtener_maximo(lista, key)
    min_valor = obtener_minimo(lista, key)
    
    if valor == max_valor or valor == min_valor:
        for heroe in lista:
            if float(heroe[key]) == valor:
                lista_heroes.append(heroe)
    
    return lista_heroes


def stark_imprimir_heroes(lista:list):
    """
    Imprime los nombres de los superhéroes de una lista.

    Args:
        lista (list): La lista de superhéroes cuyos nombres se imprimirán.

    Returns:
        bool: False si la lista está vacía, None si se imprimen los nombres de los superhéroes.
    """
    if lista == []:
        return False
    for i in range(len(lista_personajes)):
        print(f"{lista_personajes}")


def sumar_dato_heroes(lista:list, key:str):
    """
    Suma los valores de un atributo específico de superhéroes en una lista.

    Args:
        lista (list): La lista de superhéroes.
        key (str): La clave del atributo que se sumará.

    Returns:
        float: La suma de los valores del atributo especificado en la lista de superhéroes.
        False: Si ocurre un error en la suma, como datos faltantes o no numéricos.
    """
    suma = 0
    for e_lista in lista :
        if type(e_lista) == dict:
            if e_lista == {""}:
                return False
            elif e_lista[key].isalpha() == False:
                suma += float(e_lista[key])
            if e_lista[key].isalpha():
                return False
    return suma

def dividir(dividendo:int,divisor:int):#devuelve el resultadod e la divicion
    """
    Realiza una división entre dos números enteros y devuelve el resultado.

    Args:
        dividendo (int): El número que se va a dividir.
        divisor (int): El número por el cual se va a dividir el dividendo.

    Returns:
        float: El resultado de la división como un número de punto flotante.
        False: Si el divisor es igual a cero, lo cual resultaría en una división por cero.
    """
    resustado = 0
    if divisor == 0:
        return False
    elif divisor != 0:
        resustado = dividendo / divisor
    return resustado

def calcular_promedio(lista:list,key:str)-> float:#devolvera el promedo del dato que se quiera sacar
    """
Calcula el promedio de un atributo específico en una lista de superhéroes.

Args:
    lista (list): La lista de superhéroes.
    key (str): La clave del atributo del cual se calculará el promedio.

Returns:
    float: El promedio de los valores del atributo especificado en la lista de superhéroes.
"""
    promedio = 0
    cantida = 0
    sumatoria = sumar_dato_heroes(lista,key)
    for e_lista in lista:
        for e_dic in e_lista:
            if e_dic == key:
                cantida += 1
    promedio = dividir(sumatoria,cantida)
    return promedio

def mostrar_promedio_dato(lista:list,key:str):#devuelve si la lista esta vacia o  que la key no sea entero o float
    """
        Valida si la lista está vacía o si el atributo especificado no contiene valores numéricos.

        Args:
            lista (list): La lista de superhéroes.
            key (str): La clave del atributo que se verificará.

        Returns:
            bool: False si la lista está vacía o si el atributo especificado no contiene valores numéricos.
        """


    if lista == [""]:
        return False
    else:
        for e_lita in lista:
            if e_lita[key].isalpha():
                return False

def imprimir_menu():
    """
    Imprime menu
    """
    print("\n1 Normalizar datos (No se debe poder acceder a los otros puntos)\n2 (nombre de cada superhéroe de género NB)\n3 (superhéroe más alto de género F)\n4 (superhéroe más alto de género M)\n5 (superhéroe más débil de género M)\n6 (superhéroe más débil de género NB) \n7(fuerza promedio de los superhéroes de género NB.)\n8(cuántos superhéroes tienen cada tipo de color de ojos.)\n9(cuántos superhéroes tienen cada tipo de color de pelo.)\n10(superhéroes agrupados por color de ojos.)\n11(superhéroes agrupados por tipo de inteligencia)\n12(Para salir de las opciones)")
    
    
def validar_entero(string:str):#valida  que el string ingresado sea solo digitos
    """
Valida si una cadena de caracteres contiene solo dígitos.

Args:
    string (str): La cadena que se va a validar.

Returns:
    bool: True si la cadena contiene solo dígitos, False en caso contrario.
"""
    if string.isdigit():
        return True
    else:
        return False

def stark_menu_principal():
    """
    Muestra el menú principal de la aplicación Stark Marvel y solicita al usuario que ingrese una opción válida.

    Returns:
        int: El número de opción seleccionado por el usuario (entre 1 y 12), o False si la opción no es válida.
    """
    while True:
        imprimir_menu()
        opciones = input("Ingrese el número de la opcion: ")
        if validar_entero(opciones):
            opciones = int(opciones)
            if opciones >= 1 and opciones <= 12:
                return opciones
            else: 
                return False

def stark_marvel_app(lista_personajes):
    """
Función principal de la aplicación Stark Marvel que interactúa con el usuario y realiza diversas acciones según las opciones seleccionadas.

Args:
    lista_personajes (list): La lista de personajes de superhéroes.

Returns:
    -
"""
    normalizado = False

    while True:
        opciones = stark_menu_principal()
        if opciones == 1 and normalizado == False:
            if stark_normalizar_datos(lista_personajes):   
                print("Datos normalizados")
                normalizado = True 
        elif opciones == 2 and normalizado:
            pass
        elif opciones == 3 and normalizado:
            pass
        elif opciones == 4 and normalizado:
            pass
        elif opciones == 5 and normalizado:
            pass
        elif opciones == 6 and normalizado:
            pass
        elif opciones == 7 and normalizado:
            pass
        elif opciones == 8 and normalizado:
            pass
        elif opciones == 9 and normalizado:
            pass
        elif opciones == 10 and normalizado:
            pass
        elif opciones == 11 and normalizado:
            pass
        elif opciones == 12:
            break
        else:
            print("Opcion incorrecta, seleccione una opcion correcta(primero normalizar con 1)")


def imprimir_superheores(lista:list, genero:str):
    """
Imprime los nombres de superhéroes de un género específico de la lista de superhéroes.

Args:
    lista (list): La lista de superhéroes.
    genero (str): El género de superhéroes a imprimir (p. ej., "M" o "F").

Returns:
    -
"""
    if lista == []:
        return False
    for heroe in lista:
        if heroe.get("genero", "").upper() == genero.upper():
            print(heroe.get("nombre", "Nombre no especificado"))



def superheroe_mas_alto_genero(lista: list, genero: str):
    """
Busca y devuelve al superhéroe más alto de un género específico en una lista de superhéroes.

Args:
    lista (list): La lista de superhéroes.
    genero (str): El género de superhéroes a considerar (p. ej., "M" o "F").

Returns:
    dict or None: Un diccionario que representa al superhéroe más alto del género especificado,
    o None si no se encuentra ninguno.
"""
    max_altura = 0
    superheroe_mas_alto = None
    
    for heroe in lista:
        if heroe.get("genero", "").upper() == genero.upper():
            altura = heroe.get("altura", 0)  # Obtenemos la altura del superhéroe
            if altura > max_altura:
                max_altura = altura
                superheroe_mas_alto = heroe
    
    return superheroe_mas_alto


def superheroe_mas_debil_genero(lista: list, genero: str):
    """
Busca y devuelve al superhéroe más débil de un género específico en una lista de superhéroes.

Args:
    lista (list): La lista de superhéroes.
    genero (str): El género de superhéroes a considerar (p. ej., "M" o "F").

Returns:
    dict or None: Un diccionario que representa al superhéroe más débil del género especificado,
    o None si no se encuentra ninguno.
"""
    min_fuerza = None
    superheroe_mas_debil = None
    
    for heroe in lista:
        if heroe.get("genero", "").upper() == genero.upper():
            fuerza = heroe.get("fuerza", 0)  # Obtenemos la fuerza del superhéroe
            if min_fuerza == None or (fuerza < min_fuerza):
                min_fuerza = fuerza
                superheroe_mas_debil = heroe
    
    return superheroe_mas_debil


def fuerza_promedio_genero_NB(lista: list):

    """
Calcula la fuerza promedio de los superhéroes de género no binario (NB) en una lista de superhéroes.

Args:
    lista (list): La lista de superhéroes.

Returns:
    float or None: El valor promedio de la fuerza de los superhéroes de género NB, o None si no
    hay superhéroes de ese género en la lista.
"""

    suma_fuerza = 0
    cantidad_NB = 0
    
    for heroe in lista:
        if heroe.get("genero", "").upper() == "NB":
            fuerza = heroe.get("fuerza", 0)
            suma_fuerza += fuerza
            cantidad_NB += 1
    
    if cantidad_NB > 0:
        fuerza_promedio = suma_fuerza / cantidad_NB
        return fuerza_promedio
    else:
        return None
    

def contar_atributo(lista: list, color: str):
    """
    Cuenta la cantidad de superhéroes que tienen cada valor para un atributo específico en una lista de superhéroes.

    Args:
        lista (list): La lista de superhéroes.
        atributo (str): El atributo que se desea contar, como "color_de_ojos" o "color_de_pelo".

    Returns:
        dict: Un diccionario que contiene cada valor único del atributo como clave y la cantidad de superhéroes
        que tienen ese valor como valor.
    """
    contador_color = {}  # Un diccionario para contar los valores del atributo
    
    for heroe in lista:
        valor_color = heroe.get(color, "")  # Obtenemos el valor del atributo del superhéroe
        
        contador_color[valor_color] = contador_color.get(valor_color, 0) + 1
    
    return contador_color


def superheroes_agrupados(lista: list, agrupacion: str):
    """
    Cuenta la cantidad de superhéroes que tienen cada valor para un atributo específico en una lista de superhéroes.

    Args:
        lista (list): La lista de superhéroes.
        atributo (str): El atributo que se desea contar, como "color_de_ojos" o "color_de_pelo".

    Returns:
        dict: Un diccionario que contiene cada valor único del atributo como clave y la cantidad de superhéroes
        que tienen ese valor como valor.
    """

    superheroes = []
    agrupar = contar_atributo(lista, agrupacion)
    for elemento in agrupar.items():
        print(f"{agrupacion.capitalize()}: {elemento}")
        
        for heroe in lista:
            if heroe.get(agrupacion) == elemento:
                superheroes.append(heroe["nombre"])
        
        for heroe in superheroes:
            print(f"  - {heroe}")


