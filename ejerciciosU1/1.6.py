def main():
    importe = int(input("Introduce el importe final del articulo: "))
    print(f"El importe sin IVA del articulo es {int(importe*(100-10)/100)}€, y ha pagado un {int(importe-importe*(100-10)/100)}% de IVA")


if __name__ == "__main__":
    main()    