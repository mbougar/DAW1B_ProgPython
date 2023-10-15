#Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que solicite un nombre y una edad.
#Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirla hasta que introduzca una edad comprendida entre 0 y 125 años.
#El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
#El pseudocódigo debes incluirlo como comentarios en el programa de Python.


"""
Inicio
    Escribe ("Dame un nombre y una edad: ")
    Lee nombre
    Lee edad
    Si (nombre == "") entonces
        nombre = "Desconocido"
    Mientras (edad < 0 or edad > 125) hacer
        Escribe ("Dame una edad compatible (entre 0 y 125 años): ")
        Lee edad

    Escribe ("Te llamas" + nombre + "y tienes" + "edad" + años, te quedan aún" + (125-edad) + "años por cumplir")
Fin
"""

def main():
    print("Dame un nombre y una edad: ")
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))
    if(nombre == ""):
        nombre = "Desconocido"
    while(edad < 0 or edad > 125):
        print("Dame una edad compatible (entre 0 y 125 años): ")
        edad = int(input("Introduce la nueva edad: "))

    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {(125-edad)} años por cumplir")



if __name__ == "__main__":
    main()
    