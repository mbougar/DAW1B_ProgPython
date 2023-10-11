#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.



def main():
    sentence = input("Introduzca una frase: ")
    vowel = input("Introduzca una vocal: ")
    sentenceUpperVowel = str("")
    i = len(sentence)-1
    for i in range(len(sentence)):
        variable = sentence[i]
        if sentence[i] == vowel:
            variable = sentence[i].upper()
        sentenceUpperVowel += variable
    print(f"La frase cambiada es: {sentenceUpperVowel}")
    

if __name__ == "__main__":
    main()