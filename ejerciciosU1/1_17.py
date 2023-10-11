#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.






def main():
    name = input("Introduzca su nombre: ")
    n = int(input("Introduzca la cantidad de veces que quiere que repita su nombre: "))
    for i in range(0,n):
        print(name)


if __name__ == "__main__":
    main()   