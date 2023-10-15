#
# Ejercicio 1.34 - Crea un algoritmo que asigne a una variable el número 3 y después pida un número. Debéis mostrar una serie de 3 en 3 tantos números cómo se hayan leído.
#

"""
> Dime cuantos números debe tener la serie: 6
> 3 6 9 12 15 18
	
Inicio

	num = 3
	
	Escribe "Dime cuantos números debe tener la serie: "
	Lee total

	cont = 1
	Mientras (cont <= total) hacer
		Escribe num
		Si (cont < total) entonces
			Escribe " "
		num = num + 3
		cont = cont + 1
		
Fin
"""

num = 3
	
print("Dime cuantos números debe tener la serie: ", end="")
total = int(input())

cont = 1
while (cont <= total):
    print(num, end="")
    if (cont < total):
        print(" ", end="")
    num = num + 3
    cont = cont + 1