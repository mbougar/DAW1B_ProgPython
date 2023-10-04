def main():
    importe = int(input("Introduce el importe del articulo: "))
    iva = int(input("Introduce el porcentaje de IVA del articulo: "))
    print(f"El precio final del articulo es {int(importe*(iva+100)/100)}€")

if __name__ == "__main__":
    main()    