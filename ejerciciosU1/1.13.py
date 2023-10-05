#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.




def main():
    n = int(input("Introduzca un número entero: "))
    m = int(input("Introduzca otro número entero: "))
    print(f"La división de {n} entre {m} da un cociente {n // m} y un resto {n % m}")


if __name__ == "__main__":
    main()   