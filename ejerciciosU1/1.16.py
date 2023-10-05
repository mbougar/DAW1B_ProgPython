#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.





def main():
    precioHabitual = float(3.49)
    barras = int(input("Introduzca la cantidad de barras de pan no fresco que se han vendido: "))
    print(f"El precio habitual de una barra de pan es {precioHabitual}€, el descuento al pan no fresco es 60%, y el coste final de las barras de pan es {round(barras*(precioHabitual*0.4),2)}€")


if __name__ == "__main__":
    main()   