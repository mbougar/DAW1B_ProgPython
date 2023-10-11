#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.




def main():
    productName = input("Introduzca el nombre del producto: ")
    productPrice = float(input("Introduzca el precio del producto: "))
    productUnitNum = int(input("Introduzca el úmero de unidades del producto: "))
    print(f"El nombre del producto es: {productName}.\n El precio del producto es: {productPrice:06.2f} €.\n El número de unidades es: {productUnitNum:03.0f} unidades.\n El coste total de todas esas unidades es: {(productPrice*productUnitNum):08.2f} €")
    
                
    
    

if __name__ == "__main__":
    main()