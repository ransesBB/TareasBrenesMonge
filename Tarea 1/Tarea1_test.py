from Tarea1 import string_work, num_to_str


# Importa de otro archivo las funciones
# string_work y num_to_str

#  test que comprueba que se cambia completamente
#  de minusculas a mayusculas y viceversa
def test_string_work1():  # Hace el llamado a la funcion
    assert string_work(
        'abcdefghijklmnñopqrstuvwxyz') == 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    # Verifica que efectivamente al ingresar letras minusculas
    # Devuelve la mismas letras en mayuscula
    assert string_work(
        'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ') == 'abcdefghijklmnñopqrstuvwxyz'
    # Verifica que efectivamente al ingresar letras mayusculas
    # Devuelve la mismas letras en minusculas


def test_string_work2():  # Hace el llamado a la funcion
    assert string_work('prue1ba') == 'ERROR 404'
    # Comprueba que al ingresar un numero, se genera el error unico


def test_string_work3():  # Hace el llamado a la funcion
    assert string_work('prue!ba') == 'ERROR 405'
    # Comprueba que al ingresar un signo, se genera el error unico


def test_num_to_str_1():  # Hace el llamado a la funcion
    numero = 0
    while numero != 100:  # Ciclo para hacer todas las pruebas
        assert num_to_str(numero)
        # Comprueba la salida de los valores del 0 al 99
        numero += 1
        # Aumenta en 1 el valor para probar todos los numeros


def test_num_to_str_2():  # Hace el llamado a la funcion
    numero = 100
    assert num_to_str(numero) == "Error 2544"
    # Comprueba que al ingresar un numero mayor,
    # se genera el error unico


def test_num_to_str_3():  # Hace el llamado a la funcion
    numero = "Hbnsd"
    assert num_to_str(numero) == "Error 8465"
    # Comprueba que al ingresar un string, se genera el error unico
