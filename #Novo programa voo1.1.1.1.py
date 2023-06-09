#Novo programa voo
import os
os.system('cls')
print("Bem vindo ao programa de controle de voos!!!")
voos = {}
conta = 0
#função da opção 1:
def opcao1(voos):
    os.system('cls')
    while True:
        try:
            num_voos = int(input('Para iniciar me diga quantos voos deseja cadastrar: '))
            break
        except ValueError:
            print(f'Por favor digite um numero inteiro!!')
    for i in range(num_voos):
        dados_voos = []
        while True:
            try:
                cod_voos = int(input(f"Digite o codigo do {i + 1} voo: "))
                break
            except ValueError:
                print("Por favor escreva um numero inteiro!!")
        cidade_origem = str(input("Digite a cidade de origem: ").upper())
        dados_voos.append(cidade_origem)
        cidade_destino = str(input("Digite a cidade destino: ").upper())
        dados_voos.append(cidade_destino)
        while True:
            try:
                num_escalas = int(input("Digite o numero de escalas: "))
                break
            except ValueError:
                print("Por favor digite apenas numeros inteiros!!!")
        dados_voos.append(num_escalas)
        escalas = []
        for i in range(num_escalas):
            cidade_escala = str(input(f"Digite o nome da {i + 1} cidade escala: ").upper())
            escalas.append(cidade_escala)
        dados_voos.append(escalas)
        voos [cod_voos] = dados_voos
    for cod_voo, dados_voo in voos.items():
        if dados_voo[2] > 0:
            print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas e suas respectivas cidades são {dados_voo[3]}")
        else:
            print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas")
    input("Precione qualquer tecla para continuar...")
    os.system('cls')
    return voos

# função opção 2
def opcao2(voos):
    os.system('cls')
    while True:
        alt_voo = str(input('Deseja alterar a informação de algum voo?(sim|não): ').upper())
        if alt_voo == 'SIM':
            for cod_voo, dados_voo in voos.items():
                if dados_voo[2] > 0:
                    print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas e suas respectivas cidades são {dados_voo[3]}")
                else:
                    print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas")
            while True:
                try:
                    cod_busca = int(input("Qual o codigo do voo que deseja alterar: "))
                    break
                except ValueError:
                    print("Por favor digite um numero inteiro")
            for cod_voo, dados_voo in voos.items():
                if cod_voo == cod_busca:
                    while True: 
                        print('\n1 ---- CIDADE ORIGEM'
                        '\n2 ---- CIDADE DESTINO'
                        '\n3 ---- NUM ESCALAS'
                        '\n4 ---- CIDADES ESCALAS'
                        '\n5 ---- SAIR')
                        while True:
                            try:
                                opção = int(input('Qual opção deseja alterar?: '))
                                break
                            except ValueError:
                                print("Por favor insira um numero inteiro")
                        if opção == 1:
                            cidade_origem_alt = str(input("Escreva uma nova cidade origem para o voo: ").upper())
                            voos[cod_busca] [0] = cidade_origem_alt
                        elif opção == 2:
                            cidade_destino_alt = str(input("Escreva o nome da nova cidade destino: ").upper())
                            voos[cod_busca] [1] = cidade_destino_alt
                        elif opção == 3:
                            while True:
                                try:
                                    num_escalas_alt = int(input("Escreva o novo numero de escalas: "))
                                    break
                                except ValueError:
                                    print("Por favor insire um numero inteiro")
                            voos[cod_busca] [2] = num_escalas_alt
                            if num_escalas_alt > 0:
                                voos[cod_busca] [3] = []
                                for i in range(num_escalas_alt):
                                    cidade_escalar_alt = str(input("Digite o nome da nova cidade escala: ").upper())
                                    voos[cod_busca] [3].append(cidade_escalar_alt)
                        elif opção == 4:
                            for cod_voo, dados_voo in voos.items():
                                if cod_busca == cod_voo:
                                    if dados_voo[2] > 0:
                                        print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas e suas respectivas cidades são {dados_voo[3]}")
                                    else:
                                        print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas")
                            while True:
                                try:
                                    indice_escala_alt = int(input("Escrava qual o numero do indice deseja alterar: ").upper())
                                    break
                                except ValueError:
                                    print("Por favor digite um numero inteiro!!!")
                            cidade_escala_alt2 = str(input("Escreva o nome da cidade escala: ").upper())
                            voos[cod_busca][3][indice_escala_alt] = cidade_escala_alt2
                        elif opção == 5:
                            break
        elif alt_voo == 'NÃO':
            for cod_voo, dados_voo in voos.items():
                if dados_voo[2] > 0:
                    print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas e suas respectivas cidades são {dados_voo[3]}")
                else:
                    print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas")
            break
        else:
            print("Por favor responda entre sim ou não")
    input("Precione qualquer tecla para continuar...")
    os.system('cls')
    return voos

#função da opção 3
def opcao3(voos):
    os.system('cls')
    for cod_voo, dados_voo in voos.items():
        if dados_voo[2] > 0:
            print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas e suas respectivas cidades são {dados_voo[3]}")
        else:
            print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas")
    while True:
        deletar = str(input("Deseja deletar algum voo?(sim ou não): ").upper())
        if deletar == "SIM":
            while True:
                try: 
                    cod_busca = int(input("Qual o código do voo que deseja deletar: "))
                    break
                except ValueError:
                    print("Por favor digite um numero inteiro!!!") 
            while True:
                try:
                    del voos [cod_busca]
                    break
                except KeyError:
                    print("O codigo não existe")
                    while True:
                        try: 
                            cod_busca = int(input("Qual o código do voo que deseja deletar: "))
                            break
                        except ValueError:
                            print("Por favor digite um numero inteiro!!!")
            print("Voo deletado!!!")
        elif deletar == "NÃO":
            print("Desta forma os voos cadastrados ficaram assim:")
            for cod_voo, dados_voo in voos.items():
                if dados_voo[2] > 0:
                    print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas e suas respectivas cidades são {dados_voo[3]}")
                elif dados_voo[2] == 0:
                    print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas")
            input("Precione qualquer tecla para continuar...")
            os.system('cls')
            return voos
        else:
            print("Por favor responda entre sim ou não")

#função da opçao 4
def opcao4(voos, conta):
    os.system('cls')
    cidade_origem_busc = str(input("Digite o nome da cidade origem que deseja buscar: ").upper())
    for cod_voo, dados_voo in voos.items():
        if dados_voo[0] == cidade_origem_busc:
            conta = conta + 1
    print(f'Saem {conta} da cidade de {cidade_origem_busc}')
    input("Precione qualquer botão para continuar...")
    os.system('cls') 

#função da opcao 5    
def opcao5(voos):
    os.system('cls')
    for cod_voo, dados_voo in voos.items():
        if dados_voo[2] > 0:
            print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas e suas respectivas cidades são {dados_voo[3]}")
        else:
            print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas")
    cidade_origem_busc_escala = str(input("Escreva o nome da cidade origem: ").upper())
    cidade_destino_busc_escala = str(input("Escreva o nome da cidade destino: ").upper())
    lista_escalas = []
    for cod_voo, dados_voo in voos.items():
        lista_escalas.append(dados_voo[2])
    menor = lista_escalas[0]
    for i in range(len(lista_escalas)):
        if menor > lista_escalas[i]:
            menor = lista_escalas[i]
    for cod_voo, dados_voo in voos.items():
        if dados_voo[0] == cidade_origem_busc_escala and dados_voo[1] == cidade_destino_busc_escala and dados_voo[2] == menor:
            if dados_voo[2] > 0:
                print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas e suas respectivas cidades são {dados_voo[3]}")
            else:
                print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas")
    input("Precione qualquer botão para continuar...")
    os.system('cls')

#Função da opçao 6
def opcao6(voos):
    os.system('cls')
    for cod_voo, dados_voo in voos.items():
        if dados_voo[2] > 0:
            print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas e suas respectivas cidades são {dados_voo[3]}")
        else:
            print(f"O codigo do voo é {cod_voo}, sua cidade origem é {dados_voo[0]}, sua cidade destino é {dados_voo[1]}, ele possui {dados_voo[2]} cidades escalas")
    cidade_destino_busc = str(input("Digite qual cidade destino deseja buscar: ").upper())
    print('As cidades que correspondem a essa cidade destino são:')
    for cod_voo, dados_voo in voos.items():
        if dados_voo[1] == cidade_destino_busc:
            print(f'{dados_voo[0]}')
    input("precione qualquer tecla para continuar...")
    os.system('cls')

print("Seja bem vindo ao sistema!!")
while True:
    print("Opção 1 --- Incluir voos"
      "\nopção 2 --- Alterar as informações sobre um determinado voo"
      "\nOpção 3 --- Apagar um voo"
      "\nOpção 4 --- Dada a cidade origem, determinar quantos voos saem dessa cidade"
      "\nOpção 5 --- Dada a cidade origem e destino, determinar o voo com menor número de escalar e imprimir todas as informações sobre esse voo"
      "\nOpção 6 --- Dada a cidade destino, determinar todos os voos com a respectiva cidade origem que chegam nesse destino"
      "\nOpção 7 --- Sair do sistema")
    while True:
        try:
            opcao = int(input("Digite a opção que deseja usar: "))
            break
        except ValueError:
            print("Digite apenas numeros inteiros")
    if opcao == 1:
        voos = opcao1(voos)
    elif opcao == 2:
        voos = opcao2(voos)
    elif opcao == 3:
       voos = opcao3(voos)
    elif opcao == 4:
        opcao4(voos, conta)
    elif opcao == 5:
        opcao5(voos)
    elif opcao == 6:
        opcao6(voos)
    elif opcao == 7:
        os.system('cls')
        print("Obrigado por usar o sistema!!")
        break
    else:
        os.system('cls')
        print("Por favor digite apenas numeros correspondentes as opções do menu!!")
        input("Precione qualquer tecla para continuar...")
        os.system('cls')    