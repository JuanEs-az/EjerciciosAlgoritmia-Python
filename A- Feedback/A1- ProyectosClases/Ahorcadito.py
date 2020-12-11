#intrucciones,inicio y terminar
import random
palabras = {
	"TECNOLOGÍA":["programacion","robots","python","javascript","java"],
	"BIOLOGÍA": ["naturaleza","plantas","animales","huesos","organos"],
	"SOCIALES":["guerra","politica","continente","america","europa"],
}
def mainLoop():
	contadorVictorias = 0
	for tematica in palabras:
		palabra = random.choice(palabras[tematica]).upper()
		display = ""
		for _ in palabra:
			display += "_"
		print("Tematica: ",tematica)
		print(display)
		i = 6
		letrasUsadas = []
		while i > 0:
			try:
				letraSeleccionada = input(f"Dime una letra, Te quedan {i} intentos")[0].upper()
			except:
				print("Debes colocar algo")
				continue
			display = ""
			i = i if letraSeleccionada in palabra else i - 1 
			if letraSeleccionada in palabra: 
				letrasUsadas.append(letraSeleccionada) 
			for letra in palabra:
				valorAconcatenar = "_"
				for letra2 in letrasUsadas:
					if letra == letra2:
						valorAconcatenar = letra2
				display += valorAconcatenar
			print(display)
			if i == 0:
				print("Perdite, la palabra era: ",palabra )
			if not "_" in display:
				print("Ganaste, la palabra era: ", palabra)
				contadorVictorias += 1
				i = 0
	return contadorVictorias
							
print("BIENVENIDOS A EL JUEGO AHORCADO,DONDE CADA LETRA CUENTA...")
nombre = input("ingrese su nombre porfavor\t")
print("buena suerte " , nombre , ",espero que ganes")
while True:
	print("ingrese A si desea leer las intrucciones , B para dar inicio o C para terminar el juego")
	intrucciones_iniciar = input("¿Que deseas hacer?\t")[0].upper()
	if intrucciones_iniciar == "A":
		print(
		"""
		1.hay una palabra que tendrás que adivinar, por lo que tendrás que digitar por medio de tu teclado una letra para encontrarla 
		2. Tienes un total de 6 vidas, por lo que cada vez que te equivoques perderás una de ellas, y al perderlas todas el juego habrá terminado 
		3.No cometas alguna trampa 
		4.diviertete
    
      """)
	elif intrucciones_iniciar == "B" :
		print("En breve comenzamos\n")
		print("CARGANDO...")
		for n in range(0,11):
			print(f"{n}% de progreso")
		print("\t\t\tA H O R C A D I T O")
		victorias = mainLoop()
		if victorias > (len(palabras)/2):
			print(f"GANASTE CON {victorias}/{len(palabras)} DE VICTORIAS!!!")
		else:
			print(f"PER CON {victorias}/{len(palabras)} DE VICTORIAS!!!")
	elif intrucciones_iniciar == "C" :
		exit()
	else:
		print("Opcion no valida")
