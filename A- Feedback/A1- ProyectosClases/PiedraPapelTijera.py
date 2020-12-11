from random import uniform
contador = {
    "p" : 0,
    "np" : 0
}
nombreBot = input("Elige el nombre de tu oponente:\t")
opciones = ["piedra","papel","tijera"]
while True:
    bot = opciones[int(uniform(0,3))]
    jugador = input("Que eliges?:\t").lower()
    if jugador == opciones[0]:
        if bot == opciones[0]:
            print(f"{nombreBot}bot elige {opciones[0]}")
            print("Empate")
        elif bot == opciones[1]:
            print(f"{nombreBot}bot elige {opciones[1]}")
            print(f"Gana el {nombreBot}bot!")
            contador["np"] += 1
        else:
            print(f"{nombreBot}bot elige {opciones[2]}")
            print("Gana Jugador")
            contador["p"] += 1
    elif jugador == opciones[1]:
        if bot == opciones[1]:
            print(f"{nombreBot}bot elige {opciones[1]}")
            print("Empate")
        elif bot == opciones[2]:
            print(f"{nombreBot}bot elige {opciones[2]}")
            print(f"Gana el {nombreBot}bot!")
            contador["np"] += 1
        else:
            print(f"{nombreBot}bot elige {opciones[0]}")
            print("Gana Jugador")
            contador["p"] += 1
    elif jugador == opciones[2]:
        if bot == opciones[2]:
            print(f"{nombreBot}bot elige {opciones[2]}")
            print("Empate")
        elif bot == opciones[0]:
            print(f"{nombreBot}bot elige {opciones[0]}")
            print(f"Gana el {nombreBot}bot!")
            contador["np"] += 1
        else:
            print(f"{nombreBot}bot elige {opciones[1]}")
            print("Gana Jugador")
            contador["p"] += 1
    else:
        break
if contador["p"] > contador["np"]:
    eresUn = "GANADOR"
elif contador["p"] < contador["np"]:
    eresUn = "PERDEDOR"
else:
    eresUn = "EMPATE"
score = \
f"""
                  SCORE
------------------------------------------
|Jugador                       {contador["p"]}         |
|----------------------------------------|
|{nombreBot}bot                   {contador["np"]}         |
|               {eresUn}                   |
"""
print(score)
