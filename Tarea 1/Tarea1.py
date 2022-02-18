def string_work(texto):
    # Se crean 2 listas como base de datos
    # una con el abecedario en minusculas y otra en mayusculas
    minuscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mayuscula = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S',
                 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    textolista = list(texto)
    # pasa el texto del parametro de entrada a una lista de strings
    tamaño = len(textolista)  # saber el tamaño de la lista anterior
    flag = 0  # para saber si encontró la letras en las minusculas
    flag1 = 0  # para saber si encontró la letras en las mayusculas

    for cont in range(tamaño):  # recorre la lista del texto de entrada
        flag = 0
        flag2 = 0
        for cont1 in range(27):  # recorre la lista de las minusculas
            if textolista[cont] == minuscula[cont1]:
                # es para saber si la letra está en la lista de las minusculas
                flag = 1
                break
            else:
                flag1 = 0

        if flag == 0:
            for cont2 in range(27):  # recorre la lista de las mayusculas
                if textolista[cont] == mayuscula[cont2]:
                    # es para saber si la letra está
                    # en la lista de las mayusculas
                    flag1 = 1
                    break

        if (flag1 == 0) and (flag == 0):
            # si se da esta condición es porque el string no es letra
            for cont3 in range(10):  # recorre la lista de los numeros
                if textolista[cont] == numeros[cont3]:
                    # es para saber si el string está
                    # en la lista de los numeros
                    return "ERROR 404"  # Error porque contiene un  numero
            if flag2 == 0:
                # si se cumple esta condicion es porque el string
                # es un simbolo y no un numero
                return "ERROR 405"  # Error porque contiene un simbolo
    resultadolist = []  # se crea lista donde se va a ir guardando el resultado
    if (flag1 == 1) or (flag == 1):
        # si se cumple esta condición es porque no hay ningun error
        for cont5 in range(tamaño):  # recorre la lista del texto de entrada
            flag3 = 0
            for cont6 in range(27):
                if textolista[cont5] == minuscula[cont6]:
                    resultadolist.append(mayuscula[cont6])
                    flag3 = 1
                    break
            if flag3 == 0:
                for cont7 in range(27):
                    if textolista[cont5] == mayuscula[cont7]:
                        resultadolist.append(minuscula[cont7])
                        break
    resultado = "".join(resultadolist)
    # se transforma la lista donde se encuentra el resultado,
    # en un string para su retorno
    return resultado


def num_to_str(num):
    # Se crean las listas, con las principales palabras para formar los numeros
    # Se deben tener en cuenta los casos especiales
    # dados entre el diez y el veintinueve
    unidades = ["cero", "uno", "dos", "tres", "cuatro",
                "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["cero", "diez", "veinte", "treinta", "cuarenta",
               "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    num10 = ["diez", "once", "doce", "trece", "catorce", "quince",
             "dieciseis", "diecisiete", "dieciocho", "diecinueve"]
    num20 = ["veinte", "veinti"]
    # Se crea la lista en la que se va a dividir el numero ingresado
    numlist = [0, 0]

    # Verificacion de la entrada sea de tipo entero
    if isinstance(num, int):
        if num <= 99:  # Comprueba que el numero sea menor que 99
            if num >= 0:  # Comprueba que el numero es mayor que 0
                # transforma el numero en una lista con sus valores separados.
                numlist[0] = num % 10
                numlist[1] = num // 10
                # Inicia el analisis del numero ingresado
                if numlist[1] == 0:  # Si el numero es menor de diez
                    resultado = unidades[numlist[0]]
                elif numlist[1] == 1:
                    # Si el numero esta entre diez y diecinueve
                    resultado = num10[numlist[0]]
                elif numlist[1] == 2:
                    # Si el numero esta entre veinte y veintinueve
                    if numlist[0] == 0:
                        resultado = num20[0]
                    else:
                        resultado = num20[1] + unidades[numlist[0]]
                else:  # Si el numero es igual o mayor a treinta
                    if numlist[0] == 0:
                        resultado = decenas[numlist[1]]
                    else:
                        resultado = decenas[numlist[1]] + " y " + \
                                    unidades[numlist[0]]
                print(resultado)  # Imprime el nombre del numero ingresado
                return resultado
            else:
                return "Error 2544"
                # Codigo de Error Unico
                # si el numero ingresado se sale de los limites
        else:
            return "Error 2544"
            # Codigo de Error Unico
            # si el numero ingresado se sale de los limites
    else:  # Codigo de Error Unico
        # si el numero ingresado no es entero
        return "Error 8465"
