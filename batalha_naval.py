import random

letras_permitidas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
num = random.randrange(1, 11)
string = random.choice(letras_permitidas)

cordenadas_adversario = num, string

print("Bem-Vindo ao batalha naval!")
print("Para iniciar escolha as suas cordenadas: ")
letra_escolhida = input("Digite a letra escolhida (de A a J em Caps Lock): ")

if letra_escolhida not in letras_permitidas:
    print("Só são permitidas letras de A até J, escolha novamente")
    letra_escolhida = input("Digite a letra escolhida: ")

numero_escolhido = int(input("Digite o número escolhi (de 1 a 10): "))

if numero_escolhido > 10:
    print("Só são permitidos números de 1 a 10, escolha novamente")
    numero_escolhido = int(input("Digite o número escolhi (de 1 a 10): "))

suas_cordenadas = numero_escolhido, letra_escolhida

print(f"Suas cordenadas são: {suas_cordenadas}")
print("Pronto ou não a batalha irá começar!")

def main_game(suas_cordenadas, cordenadas_adversario):

    cordenadas_chute = 0, ""
    cordenadas_geradas = 0, ""

    numeros_chutados = []

    while cordenadas_chute != cordenadas_adversario or cordenadas_geradas != suas_cordenadas:

        print(f"Cordenadas chutadas: {numeros_chutados}")
        cordenadas_letra = input("Digite a cordenada da letra: ")

        if cordenadas_letra not in letras_permitidas:
            print("Letra não permitida")
            cordenadas_letra = input("Digite a cordenada da letra: ")

        cordenadas_numero = int(input("Digite a cordenda do número: "))

        if cordenadas_numero > 10:
            print("Número não permitido")
            cordenadas_numero = int(input("Digite a cordenda do número: "))

        cordenadas_chute = cordenadas_numero, cordenadas_letra

        if cordenadas_chute == cordenadas_adversario:
            print("Você ganhou!")
            print("Fim de jogo!")
            break

        else:
            print("Errado!")
            print("Tente novamente!")
            numeros_chutados.append(cordenadas_chute)

        letra_bot = random.choice(letras_permitidas)
        numero_bot = random.randrange(1, 11)

        cordenadas_geradas = numero_bot, letra_bot

        print("Vez do adversário!")
        print(f"O adversário escolheu as cordenadas: {cordenadas_geradas}")

        if cordenadas_geradas == suas_cordenadas:
            print("O adversário acertou!")
            print("Você perdeu :(")
            break

        else:
            print("O adversário errou!")



main_game(suas_cordenadas, cordenadas_adversario)


