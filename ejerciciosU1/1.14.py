#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.





def main():
    payasos = int(input("Introduzca el número de payasos vendidos en el último pedido: "))
    muñecas = int(input("Introduzca el número de muñecas vendidos en el último pedido: "))
    print(f"El pedido contiene {payasos} payasos y {muñecas} muñecas con un peso total de {int(payasos*112 + muñecas*75)} gramos")


if __name__ == "__main__":
    main()   