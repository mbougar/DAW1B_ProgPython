def main():
    print("Introduce un número: ", end="")
    x = int(input())
    print("Introduce otro: ", end="")
    y = int(input())
	
    if (x >= y):
	    numIni = x - 1
	    numFin = y
    else:
	    numIni = y - 1
	    numFin = x
    for i in range(numIni,numFin):
	    print(f"{i}", end="")
	    if (numIni != numFin):
			print("-")

if __name__ == "__main__":
    main()    