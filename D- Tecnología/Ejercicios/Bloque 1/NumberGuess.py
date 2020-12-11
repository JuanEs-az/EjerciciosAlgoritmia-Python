from random import randint
#Ana Cárdenas
#Manuela Cardona 
#Paulina Lopera
#Juan Arango
intentos = 10
numero = randint(1,200)
while True:
    if intentos == 0:
        print(f"Fallaste, el numero era {numero}")
        break
    adivina = int(input("Adivina el numero que estoy pensando: "))
    if adivina == numero:
        print(f"Felicitaciones, adivinaste!!")
        break
    elif adivina > numero:
        print("Tu numero es muy grande")
    elif adivina < numero:
        print("Tu numero es muy pequeño")
    intentos -= 1
    