#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.




def main():
    name = str(input("Introduzca su nombre completo: "))
    print(name.lower())
    print(name.upper())
    list = []
    list = name.split(" ")
    counter = 0
    name = ""
    for i in list:
        name = name + list[counter] + " "
        counter +=1
    print(name)
    




if __name__ == "__main__":
    main()   