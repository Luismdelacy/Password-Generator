# Librerias
import random
import string
import sys
import subprocess
import time
import hashlib

# Variables
Continuar = True
ops=sys.platform

# Funciones
def Menu():
    print("""
    __________________________________________
    |----------------------------------------|
    |--- Generador de Contraseñas Seguras ---|
    |----------------------------------------|
    |1. Generar contraseña segura            |
    |2. Salir                                |
    |0. Instrucciones                        |
    |________________________________________|
    """)

def Banner():
    print("""
    --------------------------
    |GENERADOR DE CONTRASEÑAS|
    --------------------------
    """)

def Limpiar():
    print("\n"*50)

def ns(r):
    while r!="n" and r!="s":
        r=input("Escriba solo \'n\' o \'s\' según su opción: ")
    return r

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

def opt(o,l):
    while o not in l:
        o=input("Escriba solo una de las opciónes posibles: ")
    return o

# Código
while Continuar:

    Menu()
    opcion = input("Seleciona una opción: ")


    if opcion == "1":
        print("Iniciando Programa")
        time.sleep(1)
        Limpiar()
        print("Iniciando Programa.")
        time.sleep(1)
        Limpiar()
        print("Iniciando Programa..")
        time.sleep(1)
        Limpiar()
        print("Iniciando Programa...")
        time.sleep(1)
        Limpiar()
        print("Iniciando Programa....")
        time.sleep(1)
        Limpiar()
        print("Bienvenido al generador de contraseñas seguras. Siga las instrucciones.")
        time.sleep(2.5)
        Limpiar()

        Banner()
        minus=OKI(input("Indique el número mínimo de minusculas: "))
        Limpiar()
        Banner()
        mayus=OKI(input("Indique el número mínimo de mayusculas: "))
        Limpiar()
        Banner()
        numeros=OKI(input("Indique el número mínimo de caracteres numéricos: "))
        Limpiar()
        Banner()
        longitud=OKI(input("Indique la longitud de la contraseña: "))
        Limpiar()
        Banner()
        suma=minus+mayus+numeros #SUMA DE MINIMOS
        while longitud<suma: #COMPROBACION ADECUACIÓN DE LA "longitud".
            longitud=OKI(input("Longitud inadecuada: "))
        caract=string.ascii_letters+string.digits
        while True:
            contra=("").join(random.choice(caract)for i in range(longitud))
            if(sum(c.islower() for c in contra)>=minus
                and sum(c.isupper() for c in contra)>=mayus
                and sum(c.isdigit() for c in contra)>=numeros):
                break
        print("Generando su contraseña segura")
        time.sleep(1.5)
        Limpiar()
        Banner()
        print("Generando su contraseña segura.")
        time.sleep(1.5)
        Limpiar()
        Banner()
        print("Generando su contraseña segura..")
        time.sleep(1.5)
        Limpiar()
        Banner()
        print("Generando su contraseña segura...")
        time.sleep(1.5)
        Limpiar()
        Banner()
        print("Generando su contraseña segura....")
        time.sleep(1.5)
        Limpiar()
        Banner()
        print("\nSU CONTRASEÑA SEGURA ES: ",contra)

        cifrado = hashlib.new("SHA512")
        contra = contra.encode("UTF-8")
        cifrado.update(contra)

        Hash_Contraseñas = open("Contraseñas.txt","a+",encoding="UTF-8")
        Hash_Contraseñas.write("La contraseña generada y su hash son: " + str(contra) + " <----> " + cifrado.hexdigest() + "\n")
        Hash_Contraseñas.close()

    elif opcion =="2":
        print("Se esta cerrando el programa")
        time.sleep(1)
        print("Se esta cerrando el programa.")
        time.sleep(1)
        print("Se esta cerrando el programa..")
        time.sleep(1)
        print("Se esta cerrando el programa...")
        time.sleep(1)
        print("Se esta cerrando el programa....")
        time.sleep(1)
        print("Hasta pronto.")
        Continuar = False

    elif opcion == "0":
        print(""""
        Programa que genera contraseñas seguras.
        El programa pide el número minimo de letras mayusculas.
        El programa pide el número mínimo de letras minúsculas.
        El programa pide el número mínimo de caracteres.
        El programa pide la longitudo de la contraseña y con esos datos la contraseña se genera.
        Para salir pulsa 99
        """)
        opcion = input("Selecione una opción: ")
    
    elif opcion == "99":
        Menu()

    else:
        print("Elige una opcion valida.")
        time.sleep(1)
        print("Valores númericos validos 0 1 2 99")

    Continuar = bool(input("¿Continuar? Pulsa cualquier tecla para continuar o por el contrario pulsa Enter para finalizar: "))
