def main():
    weight = float(input("Introduzca su peso en kilogramos: "))
    height = float(input("Introduzca su altura en metros: "))
    print(f"Su Indice de masa corporal (IMC) es: {round(float(weight/(height**2)),2)} Kg/m**2")


if __name__ == "__main__":
    main()   