#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.




def main():
    products = input("Introduzca los productos de su cesta de la compra separados por comas: ")
    products = products.split(",")
    item = ""
    #El siguiente bucle se asegura de imprimir por pantalla los items de la cesta sin un espacio delante
    for i in range(0,len(products)):
        item = products[i]
        itemLetter = ""
        for j in range(0, len(item)):
            if item[j] != " ":
                itemLetter = itemLetter + item[j]
        print(itemLetter)
                
    
    

if __name__ == "__main__":
    main()