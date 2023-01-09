import random

secret_num = random.randint(1, 10)
guess = int(input("ESCOLHA UM NÚMERO ENTRE 1 E 10: "))
guesses_left = 3
while guesses_left > 0 and guess != secret_num:
  if guess > secret_num:
    print("MUITO ALTO TENTA DE NOVO")
    guesses_left -= 1
    guess = int(input("ESCOLHA UM NÚMERO ENTRE 1 E 10: "))
  elif guess < secret_num:
    print("MUITO BAIXO TENTA DE NOVO")
    guesses_left -= 1
    guess = int(input("ESCOLHA UM NÚMERO ENTRE 1 E 10: "))
if guesses_left == 0:
  print("VOCE PERDEU ERA", secret_num)
else:
  print("VC GANHOU ERA", secret_num)
