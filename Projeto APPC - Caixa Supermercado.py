#ABRIR O CAIXA
senha = 0
tentativas = 3

while senha != 2987:
    senha = int(input('Digite a senha:\n'))
    if senha != 2987:

        tentativas = tentativas - 1
        print(f'Senha incorreta, você possui {tentativas} tentativas restantes.')

        if tentativas == 0:
            print('Sistema tem que ser reiniciado!')
            exit() #Comando fechar o programa

    else:
        print('Senha Correta, caixa aberto!\n')


print('Bem Vindo!\n')

#LEITURA DAS VENDAS
valorTotal = 0
valorInserido = 0
valorComputado = 0
item = 0
finalizar = 'N'

print("INSERÇÃO DOS ITENS VENDIDOS:")

while finalizar == 'N':
    item += 1
    valorInserido = float(input(f'Digite o valor do item {item}: R$'))
    valorComputado = valorInserido
    valorTotal += valorComputado

    #Opção 0: Continuar ou Finalizar a inserção de valores
    if valorInserido == 0:
       finalizar = str(input("Deseja realmente finalizar? (S = Sim | N = Não): "))

       if finalizar == 'N':
            valorInserido = float(input(f'Digite o valor do item {item}: R$'))
            valorComputado = valorInserido
       elif finalizar == 'S':
            break
       else:
         while finalizar != 'S' and finalizar != 'N':
                finalizar = str(input('Resposta inválida, responda S para Sim ou N para Não: '))
         if finalizar == 'N':
            valorInserido = float(input(f'Digite o valor do item {item}: R$'))
            valorComputado = valorInserido

    #Opção -1: Corrigir o valor inserido
    if valorInserido == -1:
        item -= 1

        valorInserido = float(input(f'Digite o valor correto do item {item}: R$'))
        valorComputado = valorInserido
        valorTotal -= valorComputado

print('\nVenda finalizada!')
print(f'Total R${valorTotal}, {item} itens.')


#FINALIZAÇÃO E CALCULO DO TROCO
cedula200 = 200
caixa = 1280.00
valorPago = float(input('Valor pago: R$'))
troco = 0

if valorPago == valorTotal:
    print('NÃO HÁ TROCO.')

elif valorPago > valorTotal:
    troco = valorPago - valorTotal
    print(f'Troco: R${troco}')













