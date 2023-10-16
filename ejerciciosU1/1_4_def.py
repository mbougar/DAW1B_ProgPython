def gradosConversion():
    celsius = float(input("Introduzca una temperatura en grados Celsius: "))
    return (celsius*1.8) + 32

def main():
    fahrenheit = gradosConversion()
    print(f"Tu temperatura en grados Fahrenheit es: {fahrenheit}°F")

if __name__ == "__main__":
    main()  