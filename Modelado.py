import random

from Persona import Persona
from Grupos import Grupos

dias = 0
contagiados = []
numero_personas = int(input(f'Ingrese el número de personas a evaluar: '))
for i in range(1,numero_personas):
    #creación de las personas a evaluar
    persona = Persona(random.randint(1,3),0)
    for i in range(1,80):
        #número de días en los que la persona asiste al campus
        grupo = Grupos(random.randint(1,6),0)
        #dependiendo del tipo de grupo al que haga parte en ese día, tiene una probabilidad de contagio diferente
        if grupo.tipo == 1:
            grupo.contagio = 0.33
            #dependiendo del número de dosis tiene una mayor o menor posibilidad de contagio teniendo en cuenta los grupos
            if persona._dosis == 1:
                persona._posibilidad = grupo.contagio/1
            elif (persona._dosis == 2):
                persona._posibilidad = grupo.contagio / 2
            else:
                persona._posibilidad = grupo.contagio / 3
        elif(grupo.tipo == 2):
            grupo.contagio = 0.58
            if persona._dosis == 1:
                persona._posibilidad = grupo.contagio/1
            elif (persona._dosis == 2):
                persona._posibilidad = grupo.contagio / 2
            else:
                persona._posibilidad = grupo.contagio / 3
        elif(grupo.tipo == 3):
            grupo.contagio=0.78
            if persona._dosis == 1:
                persona._posibilidad = grupo.contagio/1
            elif (persona._dosis == 2):
                persona._posibilidad = grupo.contagio / 2
            else:
                persona._posibilidad = grupo.contagio / 3
        elif(grupo.tipo == 4):
            grupo.contagio = 0.89
            if persona._dosis == 1:
                persona._posibilidad = grupo.contagio/1
            elif (persona._dosis == 2):
                persona._posibilidad = grupo.contagio / 2
            else:
                persona._posibilidad = grupo.contagio / 3
        elif(grupo.tipo == 5):
            grupo.contagio= 0.95
            if persona._dosis == 1:
                persona._posibilidad = grupo.contagio/1
            elif (persona._dosis == 2):
                persona._posibilidad = grupo.contagio / 2
            else:
                persona._posibilidad = grupo.contagio / 3
        else:
            grupo.contagio = 1
            if persona._dosis == 1:
                persona._posibilidad = grupo.contagio/1
            elif (persona._dosis == 2):
                persona._posibilidad = grupo.contagio / 2
            else:
                persona._posibilidad = grupo.contagio / 3
        dias +=1
        if dias>80:
            dias=0
    #si la persona más del 50% de posibilidad de ser contagiado, pasará a ser persona contagiada
    if persona._posibilidad >= 0.5:
        contagiados.append(persona)

for contagiado in contagiados:
    print(contagiado)
print()
print(f'De {numero_personas} personas se contagiaron {len(contagiados)}, lo que representa que el {len(contagiados)/numero_personas*100}%')
