import random


def inicio():
    print('----------------------------------------')
    print('Bienvenido a este juego')
    print('----------------------------------------')

def juego():
    play = True
    while play:
        # Generar un nuevo número aleatorio cada vez que se juega
        cpu = random.randint(0, 10)
        
        while True:
            user = int(input('Ingresa un numero: '))
            if user > cpu:
                print(' ')
                print('El numero es muy alto, ingresa un numero menor')
                print(' ')
            elif user < cpu:
                print(' ')
                print('El numero es muy bajo, ingresa un numero mayor')
                print(' ')
            elif user == cpu:
                print(' ')
                print('   Ganaste!    ')
                print(' ')
                break  # Sale del bucle interno cuando el jugador adivina el número
        
        # Preguntar si el jugador quiere volver a jugar
        question = input('Quieres volver a jugar? y/n: ')
        if question.lower() == 'y':
            print('Ok! Volvamos a empezar.')
            print(' ')
        else:
            print('Gracias por jugar. Hasta la próxima!')
            print(' ')
            play = False  # Sale del bucle externo y termina el juego

# Iniciar el juego
inicio()
juego()

                
