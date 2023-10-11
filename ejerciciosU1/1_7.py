def main():
    suma = 0
    for i in range(0,3):
        num = int(input("Dame un número entero:"))
        suma += num
    print(f"La suma de tus tres números enteros es: {suma}")    

if __name__ == "__main__":
    main()