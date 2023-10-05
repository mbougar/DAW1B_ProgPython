def main():
    importe = float(input("Introduce el importe del articulo: "))
    iva = float(input("Introduce el porcentaje de IVA del articulo: "))
    print(f"El precio final del articulo es {float(importe*(iva+100)/100)}€")

if __name__ == "__main__":
    main()    