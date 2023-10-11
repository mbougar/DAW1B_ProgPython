#Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que pida un número de inicio, un incremento y un total de la serie.
#El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error u obligar a que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes)
#Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
#El pseudocódigo debes incluirlo como comentarios en el programa de Python.


"""
Inicio
    Escribe ("Intruduzca un número de inicio, un incremento y un total de la serie: ")
    Lee numInicio
    Lee numIncremento
    Mientras (numIncremento == 0) hacer:
        Escribe ("Dame un numero compatible (mayor que 0): ")
        Lee numIncremento
    Lee numTotal
    Mientras (numTotal == 0) hacer:
        Escribe ("Dame un numero compatible (mayor que 0): ")
        Lee numTotal
    contador = 2
    cadenaSerie = numInicio + "-"
    Mientras (contador <= numTotal-1) hacer:
        cadenaSerie = (numInicio+numIncremento*contador) + ".."
        contador += 1

    Escribe (cadenaSerie)
Fin
"""

def main():
    print("Intruduzca un número de inicio, un incremento y un total de la serie: ")
    numInicio = int(input("Intruduzca un número de inicio: "))
    numIncremento = int(input("Intruduzca un número de incremento: "))
    while(numIncremento == 0):
        print("Dame un numero compatible (mayor que 0): ")
        numIncremento = int(input("Intruduzca un número de incremento: "))
    numTotal = int(input("Intruduzca un número de inicio: "))
    while(numTotal == 0):
        print("Dame un numero compatible (mayor que 0): ")
        numTotal = int(input("Intruduzca un número de inicio: "))
    contador = 1
    cadenaSerie = str(numInicio) + "-"
    while(contador <= numTotal-2):
        cadenaSerie = cadenaSerie + str(numInicio+numIncremento*contador)
        if (contador!= numTotal-2):
            cadenaSerie += ".."
        contador += 1
    cadenaSerie += "-" + str(numInicio+numIncremento*contador)
    print(cadenaSerie)


if __name__ == "__main__":
    main()