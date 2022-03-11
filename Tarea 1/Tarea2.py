#Se importan las librerias
import RPi.GPIO as GPIO   #Importamos el paquete que nos permite utilizar las GPIO
import threading          #Permite el uso de hilos
import argparse           #Permite al programa recibir parametros desde el shell de Linux
import os                 #Permite escribir los tiempos de ejecucion en un archivo .txt
import time               #Se utiliza para medir los tiempos de ejecucion
import logging
from multiprocessing import Process #Permite el uso de multiprocesos y su atributo Process 

GPIO.setmode( GPIO.BCM ) #Establecemos el modo segun el cual nos referimos a los GPIO de las raspberry
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #se configura el pin como entrada y se habilita la resistencia interna de pull up



#Este bloque se encarga de recibir los parametros desde el shell de Linux 
parser = argparse.ArgumentParser(description = 'Tarea 2')
parser.add_argument('X', type = int, help = 'Numero de elementos en la lista')
args = parser.parse_args()

while 1:   #Bucle infinito que pregunta por el boton
    if GPIO.input(18) == GPIO.LOW:
        break #salir del bucle infinito
    
    
#Esta funcion recibe dos parametros de entrada y retorna el arreglo con la cantidad de X elementos diferentes que se pasan como parametro.
def array(elemento,i):
    arreglo = [];
    while i < elemento:
                arreglo.append(i);
                i = i + 1;
    return arreglo
 
 
   
#Esta funcion recibe el arreglo y los parametros de inicio y fin para recorrerlo y realizar el calculo del cuadrado del numero en cada posicion, este es el proceso que realizara el hilo                   
def potencia(inicial,array,final,nombre):

    #inicio = time.time()
    while inicial < final:
        num1 =array[inicial] 
        num2 = array[inicial]
        potencia = num1 * num2
        inicial = inicial + 1;
        time.sleep(0.1)
    #final = time.time()
    #print (nombre,final-inicio)
     


#Se define que este es el codigo principal, se inicializan las variables a utilizar como parametros para los hilos 
if __name__ == '__main__':
    i = 0;
    elemento = args.X;
    lista = array(elemento,i);


#Se relaliza el primer recorrido para un unico hilo y se mide su tiempo de ejecucion
    hilo = Process(target=potencia,args=[i, lista, elemento,'t1.solo'])
    start=time.time()
    hilo.start()
    hilo.join()
    tiempo = time.time()-start
    

#Se realiza el recorrido para los 4 hilos de manera que se reparten el trabajo equitativo y se mide el tiempo de ejecucion de este proceso 
    rango = elemento // 4;
    hilo1 = Process(target=potencia, args=[i, lista, i + rango,'t1.multiple'])
    hilo2 = Process(target=potencia, args=[i + 1 + rango, lista, i + 2 * rango,'t2.multiple'])
    hilo3 = Process(target=potencia, args=[i + 1 + 2 * rango, lista, i + 3 *rango,'t3.multiple'])
    hilo4 = Process(target=potencia, args=[i + 1 + 3 * rango, lista, elemento,'t4.multiple'])
    start=time.time() 
    hilo1.start()
    hilo2.start()
    hilo3.start()
    hilo4.start()
    hilo1.join()
    hilo2.join()
    hilo3.join()
    hilo4.join()
    tiempo4 = time.time()-start
    

#Se revisa si en los parametros iniciales se escogio la opcion de escribir los tiempos de resupuesta en un archivo de texto o si se imprimen los tiempos en pantalla    

    print("Tiempo de ejecucion de un hilo: " )
    print(tiempo)
    print("Tiempo de ejecucion de 4 hilos: " )
    print(tiempo4)
