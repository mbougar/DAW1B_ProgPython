def main():
    n = int(input("Dame un número entero: "))
    suma = 0
    for i in range(1,n+1):   #la formula dada es: suma = int(n*(n+1)/2)
        suma += i
    print(f"La suma de todos los números enteros desde 1 hasta {n} es: {suma}")



if __name__ == "__main__":
    main()    