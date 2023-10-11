#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre.

def main():
    name = input("Introduzca su nombre: ")
    print(f"{name.upper()} tiene {len(name)} letras.")

if __name__ == "__main__":
    main()