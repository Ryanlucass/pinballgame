#Flíper é um tipo de jogo onde uma bolinha de metal cai por um labirinto de caminhos até chegar na parte de baixo do labirinto. A quantidade de pontos que o jogador ganha depende do caminho que a bolinha seguir. O jogador pode controlar o percurso da bolinha mudando a posição de algumas portinhas do labirinto. Cada portinha pode estar na posição 0, que significa virada para a esquerda, ou na posição 1 que quer dizer virada para a direita. Considere o flíper da figura abaixo, que tem duas portinhas. A portinha P está na posição 1 e a portinha R, na posição 0. Desse jeito, a bolinha vai cair pelo caminho B: Você deve escrever um programa que, dadas as posições das portinhas P e R, neste flíper da figura, diga por qual dos três caminhos, A, B ou C, a bolinha vai cair! Restrições: O número PP pode ser 0 ou 1. O número RR pode ser 0 ou 1.


print('Bem vindo ao jogo de fliperama \n')
print('Digite 1 ou 0 para as portas P e B \n')

print('            |   |\n           0|   |1\n           / P\ \ \n          /  / \ \ \n        0/  /1  \ \ \n        / R/ \   \ \ C\n       /  /\  \ \n      /  /  \  \ \n     /  /    \  \ \n    A         B \n ')

pdoor = int(input('digite um número para a porta P: '))

if (pdoor == 0):
    print('O caminho da bola é o C')
    print('            |   |\n           0|   |1\n           / P\ \ \n          /  / \ \ \n        0/  /1  \ \ \n        / R/ \   \ \ C\n       /  /\  \ \n      /  /  \  \ \n     /  /    \  \ \n    A         B \n')
if (pdoor == 1):
    bdoor = int(input('digite um número para a porta B: '))
    if (bdoor == 1):
        print('O caminho da bola é o A \n')
        print('            |  |\n           0|  |1\n           / P/ \ \n          /  / \ \ \n        0/  /1  \ \ \n        / R/ \   \ \ C\n       /  /\  \ \n      /  /  \  \ \n     /  /    \  \ \n    A         B \n')
    elif (bdoor == 0):
        print('O caminho da bola é o B')
        print('            |  |\n           0|  |1\n           / P/ \ \n          /  / \ \ \n        0/  /1  \ \ \n        / \R \   \ \ C\n       /  /\  \ \n      /  /  \  \ \n     /  /    \  \ \n    A         B \n')
    else:
        print('deixa de ser gaiato, quer quebrar o meu sistema é? presta atenção')


          