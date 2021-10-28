from typing import Counter

# Input para inserção de palavra
palavra = str(input("Qual é a palavra? "))

# função principal a ser chamada
def main(palavra):
# Criação de um contador
    contador = Counter(palavra)
# Utilização do contador para letras da palavra utilizando a lib Counter
    for letra in palavra:
        if(contador[letra] == 1):
             print(letra)
             break

# chamando função principal
main(palavra)