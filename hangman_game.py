import random
import os

lista_palabras=[]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

with open("./archivos/data.txt","r") as f:


  for i in f:
    lista_palabras.append(i.replace("\n",""))
  # print(lista_palabras)


palabra_aleatoria = random.choice(lista_palabras)
#print(palabra_aleatoria)
#print()


display=[]
for i in range(len(palabra_aleatoria)):
  display+="*"
print(f"{' '.join(display)}")
#print()


juego_activo=True
lives=6

while juego_activo:
 
  letra_usuario=input("Ingrese una letra: ")
  os.system("cls")
  for i in range(len(palabra_aleatoria)):
    
    letras_de_palabra=palabra_aleatoria[i]
    if letras_de_palabra==letra_usuario:
      display[i]=letra_usuario
      print(f"Tienes {lives} vidas")
      
  
  if letra_usuario not in palabra_aleatoria:
    lives-=1
    print(f"Tienes {lives} vidas")

    if lives==0:
      print("¡Perdiste!")
      juego_activo=False
  print(f"{' '.join(display)}")

  if "*" not in display:
    juego_activo=False
    print("¡Ganaste!")

  print(stages[lives])