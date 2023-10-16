def precioFinal(importe: int, iva: int):
    return print(f"El precio final del articulo es {(importe*(iva+100)/100)}€")


def main():
    importe = int(input("Introduce el importe del articulo: "))
    iva = int(input("Introduce el porcentaje de IVA del articulo: "))
    precioFinal(importe, iva)

if __name__ == "__main__":
    main()    