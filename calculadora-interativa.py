n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('=-=' * 20)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair')
    opcao= int(input('OQUE VOCÊ DESEJA FAZER?: '))
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('{} x {} é = {}'.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior entre {} e {} é {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
print('Finalizando programa...')