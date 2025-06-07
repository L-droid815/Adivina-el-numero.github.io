import random

numeroSecreto = random.randint(1, 100)

intentos = 0

print("Hola intentaras adivinar un numero entre el 1 y el 100")


while True:
    
    try:
        
        Suposicion = int(input("Introduce cualquier numero: "))
        
        intentos = +1
        
        
        if Suposicion < numeroSecreto:
            
            print("Es un numero bajo")
            
        elif Suposicion > numeroSecreto:
            
            print("Es un numero alto")
            
        else:
            
            print("Felicidades ganaste el numero es ", numeroSecreto, "y lo intentaste ", intentos, "veces")
            
            break # <- Salimos del bucle porque ya adivinaste
        
        
    except ValueError:
        
        print("Ingrese un numero valido por favor")