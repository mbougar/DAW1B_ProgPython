#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.




def main():
    fecha = input("Introduzca su fecha de nacimiento en formato dd/mm/aaaa: ")
    fecha = fecha.split("/")
    print(f"Usted nació el día {fecha[0]}, del mes {fecha[1]}, en el año {fecha[2]}")
    
    

if __name__ == "__main__":
    main()