#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.


def main():
    price = input("Introduzca el precio del producto en euros con 2 decimales: ")
    priceDecimal = price[len(price)-2]+price[len(price)-1]
    price = float(price)-(int(priceDecimal)/100)
    print(f"El precio del producto es {int(price)} € y {priceDecimal} céntimos")
    
    

if __name__ == "__main__":
    main()