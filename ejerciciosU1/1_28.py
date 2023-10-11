#Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuantos números existen entre ellos dos.
#El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
#Si los números son diferentes, por ejemplo 5 y 12 debe mostrar la frase "El número menor es el 5 y entre ellos existen 7 números enteros".
#El pseudocódigo debes incluirlo como comentarios en el programa de Python.


"""
Inicio
    Escribe ("Dame dos numeros enteros: ")
    Lee n1
    Lee n2
    Mientras (n1 == n2) hacer:
        Escribe ("Los números no pueden ser iguales")
        Lee n2

    Si (n1 < n2) entonces:
        Escribe ("El número menor es el" + n1 + "y entre ellos existen" + (n2-n1) + "números enteros")
    Sino:
        Escribe ("El número menor es el" + n2 + "y entre ellos existen" + (n1-n2) + "números enteros")
Fin
"""

def main():
    print("Dame dos numeros enteros: ")
    n1 = int(input())
    n2 = int(input())
    while (n1 == n2):
        print("Los números no pueden ser iguales")
        n2 = int(input())
    if (n1 < n2):
        print(f"El número menor es el {n1} y entre ellos existen {(n2-n1)} números enteros")
    else:
        print(f"El número menor es el {n2} y entre ellos existen {(n1-n2)} números enteros")



if __name__ == "__main__":
    main()