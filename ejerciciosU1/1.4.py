

def main():

    """Esto sale en la definicion de la funcion main()"""

    celsius = int(input("Dame una temperatura en grados Celsius: "))
    print(str(celsius) + " grados Celsius en grados Fahrenheit son: " + str((celsius * 9 / 5) + 32) + " grados Fahrenheit.")

if __name__ == "__main__":
    main()