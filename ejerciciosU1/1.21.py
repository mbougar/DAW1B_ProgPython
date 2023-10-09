#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.






def main():
    sentence = input("Introduzca una frase: ")
    sentenceInverted = str("")
    i = len(sentence)-1
    while i >= 0:
        sentenceInverted += sentence[i]
        i = i - 1
    print(f"La frase invertida es: {sentenceInverted}")
    

if __name__ == "__main__":
    main()