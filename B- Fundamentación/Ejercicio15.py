#Ejercicio 15: Calculadora simple

#Construir un algoritmo que implemente una Calculadora simple. Para ello, deberá tomar como entrada dos numeros reales (a y b) y un 
#caracter que representa la operación a realizar: suma(+), resta(-), multiplicación(*) o division(/). El algoritmo deberá calcular e 
#imprimir el resultado de la operacion correspondiente. Luego deberá preguntar al usuario si desea continuar, a lo cual el usuario 
#responderá con un caracter 's' o 'n'.
#El algoritmo deberá terminar cuando el usuario responda 'n'.
def Calculadora():
    while True:
        try:
            A = float(input("Ingrese el valor de A\n"))
            B = float(input("Ingrese el valor de B\n"))
            C = input("Ingrese el operador de su operacion(+,-,*,/)\n")
            if C == '+' or C == '-' or C == '*' or C == '/':
                break
            else:
                raise TypeError 
        except TypeError:
            print("C debe de ser un operador (+,-,*,/)")    
        except ValueError:
            print("A y B deben de ser numeros para continuar\nIntenta denuevo")
    if C == '+':
        _D = A + B
    elif C == '-':
        _D = A - B
    elif C == '*':
        _D = A * B
    elif C == '/':
        _D = A / B
    print("El resultado de tu operacion es", _D)
    sn = input("Ingrese 's' sí desea continuar, y 'n' si desea finalizar\n")
    if sn == 's':
        Calculadora()
Calculadora()
    
