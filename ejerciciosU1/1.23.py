#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.



def main():
    email = input("Introduzca su correo electrónico: ")
    email = email.split("@")
    newEmail = email[0]+"@ceu.es"
    print(f"Su nuevo correo asociado al dominio ceu es: {newEmail}")
    
    

if __name__ == "__main__":
    main()