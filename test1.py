import random

letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
num = random.randrange(1, 11)
string = random.choice(letras)

cordenadas = num, string

print(cordenadas)