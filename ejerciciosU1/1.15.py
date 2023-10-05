#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

#Calcula el interés: capital * (1 + interes)


def main():
    capital = int(input("Introduzca el capital inicial de la cuenta: "))
    print(f"Tras el primer año tu cuenta contara con un capital de {round(capital*1.04,2)}€, tras el segundo año tu cuenta contara con un capital de {round(capital*1.04**2,2)}€, Tras el tercer año tu cuenta contara con un capital de {round(capital*1.04**3,2)}€")


if __name__ == "__main__":
    main()   