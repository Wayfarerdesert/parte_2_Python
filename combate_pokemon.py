
from random import randint
import os

VIDA_INICIAL_PIKACHU = 80
VIDA_INICAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICAL_SQUIRTLE

tamaño_barra_vida = 20

while vida_pikachu > 0 and vida_squirtle > 0:
    # se desenvuelven los turnos del combate

    # Turno de Pikachu
    print('\nTurno de Pikachu\n')
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # bola voltio
        print('Pikachu ataca con Bola Voltio')
        vida_squirtle -= 10
    else:
        print('Pikachu ataca con Onda Trueno')
        vida_squirtle -= 11

    if vida_pikachu < 0:
        vida_pikachu = 0

    if vida_squirtle < 0:
        vida_squirtle = 0

    # print('La vida de Picachu es: {}, la vida de squirtle es: {}'.format(vida_pikachu, vida_squirtle))

    barra_de_vida_pikachu = int(vida_pikachu * tamaño_barra_vida / VIDA_INICIAL_PIKACHU)
    print('Pikachu:    [{}{}] ({}/{})'.format('#'*barra_de_vida_pikachu, ' ' * (tamaño_barra_vida - barra_de_vida_pikachu),
                                              vida_pikachu, VIDA_INICIAL_PIKACHU))

    barra_de_vida_squirtle = int(vida_squirtle * tamaño_barra_vida / VIDA_INICAL_SQUIRTLE)
    print('Squirtle:   [{}{}] ({}/{})'.format('#' * barra_de_vida_squirtle, ' ' * (tamaño_barra_vida - barra_de_vida_squirtle),
                                              vida_squirtle, VIDA_INICAL_SQUIRTLE))

    input('\nEnter para continuar...\n')
    os.system('cls')


    # turno Squirtle
    print('\nTurno de Squirtle\n')

    ataque_squirtle = None
    while ataque_squirtle not in ['P', 'A', 'B', 'N']:
        ataque_squirtle = input('¿Que ataque desea realizar?\n'
                                '[P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ')
    if ataque_squirtle == 'P':
        print('\nSquirtle ataca con Placaje')
        vida_pikachu -= 10
    elif ataque_squirtle == 'A':
        print('\nSquirtle ataca con Pistola Agua')
        vida_pikachu -= 12
    elif ataque_squirtle == 'B':
        print('\nSquirtle ataca con Burbuja')
        vida_pikachu -= 9
    elif ataque_squirtle == 'N':
        print('\nSquirtle no hace nada...')

    if vida_pikachu < 0:
        vida_pikachu = 0

    if vida_squirtle < 0:
        vida_squirtle = 0

    #  print('La vida de Picachu es: {}, la vida de squirtle es: {}'.format(vida_pikachu, vida_squirtle))
    barra_de_vida_pikachu = int(vida_pikachu * tamaño_barra_vida / VIDA_INICIAL_PIKACHU)
    print('Pikachu:    [{}{}] ({}/{})'.format('#' * barra_de_vida_pikachu, ' ' * (tamaño_barra_vida - barra_de_vida_pikachu),
                                              vida_pikachu, VIDA_INICIAL_PIKACHU))

    barra_de_vida_squirtle = int(vida_squirtle * tamaño_barra_vida / VIDA_INICAL_SQUIRTLE)
    print('Squirtle:   [{}{}] ({}/{})'.format('#' * barra_de_vida_squirtle, ' ' * (tamaño_barra_vida - barra_de_vida_squirtle),
                                              vida_squirtle, VIDA_INICAL_SQUIRTLE))

    input('\nEnter para continuar...\n')
    os.system('cls')


if vida_pikachu > vida_squirtle:
    print('GAME OVER\n'
          'Pikachu Gana!')
    input('\nEnter para salir\n')
    exit()
else:
    print('Squirtle Gana!')
    input('\nEnter para salir\n')
    exit()

