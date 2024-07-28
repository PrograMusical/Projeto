import random

choices = ['rock' , 'paper' , 'scissor']

while True:
    player = None
    pc = random.choice(choices)
    while not player in choices:
        player = input('rock, paper ou scissor? ').lower()

    if player == pc:
        print('pc :{}'.format(pc))
        print('jogador : {}'.format(player))
        print('empate')

    elif player == 'rock':
        if pc == 'paper':
            print('pc :{}'.format(pc))
            print('jogador : {}'.format(player))
            print('o pc ganhou')
        elif pc == 'scissor':
            print('pc :{}'.format(pc))
            print('jogador : {}'.format(player))
            print('o player ganhou')

    elif player == 'paper':
        if pc == 'scissor':
            print('pc :{}'.format(pc))
            print('jogador : {}'.format(player))
            print('o pc ganhou')
        elif pc == 'rock':
            print('pc :{}'.format(pc))
            print('jogador : {}'.format(player))
            print('o player ganhou')

    else:
        if pc == 'rock':
            print('pc :{}'.format(pc))
            print('jogador : {}'.format(player))
            print('o pc ganhou')
        elif pc == 'paper':
            print('pc :{}'.format(pc))
            print('jogador : {}'.format(player))
            print('o player ganhou')

    if input('sair? ') == 's':
        break
    