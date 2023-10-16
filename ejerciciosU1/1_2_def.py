def total(horas: int, precio: float):
    return horas*precio

def main():
    hourWork = int(input("Horas de trabajo: "))
    hourPrice = float(input("Coste por hora: "))
    print(f"Importe total: {total(hourWork,hourPrice)} €")

if __name__ == "__main__":
    main()  