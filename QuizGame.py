""" ESCRIBIR LAS RESPUESTAS CON LA INICIAL DE CADA PALABRA CON MAYUSCULA EJEMPLO  "What does CPU stands for? respuesta
"Central Processing Unit"

"""

# JUEGO DE PREGUNTAS 

print("Welcome to my computer quiz!")  #Bienvenido al cuestionario de mi PC

playing = input("Do you want to play?")  #Quieres jugar ?

if playing.lower() != "yes":  # Si   
    quit()

print("Okay! let's play:)")  #Bueno Juguemos 
score = 0

answer = input("what does CPU stands for?") #Que significa CPU
if answer.lower() == "central processing unit":  #Unidad central de procesamiento
    print("Correct!") #Correcto
    score += 1
else:
    print("Incorrect!")  #Incorrecto 
    

answer = input("What does GPU stand for?") #Que significa GPU
if answer.lower() == "graphics processing unit": #Unidad de procesamiento grafico 
    print("Correct!")
    score += 1
else:
    print("Incorrect!")  

answer = input("What does RAM stand for?") #Que es la RAM
if answer.lower() == "random access memory ": #Memoria de acceso aleatorio 
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("What does PSU stand for?") #Que significa PSU
if answer.lower() == "power supply ": #Alimentacion electrica
    print("Correct!")
    score += 1
else:
    print("Incorrect!")  


print("You got " + str(score)  + " questions correct!")   #puntos obtenidos 
print("You got " + str((score / 4) * 100) + "%.")         #porcentajes de puntos 

                                                                                                                                                                 
