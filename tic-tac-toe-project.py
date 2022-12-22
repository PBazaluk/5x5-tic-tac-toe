import os


#Cria um nome de jogador
def criarnovojogador():
    nome = input("Digite um nome de usuário: ")
    if os.path.isfile(nome + ".txt"):
        print("Jogador ja registrado!")
    else:
        arquivo = open(nome + ".txt", "w")
        arquivo.write("0\n")
        arquivo.write("0")
        arquivo.close()

#Exclui um nome de jogador e seu histórico
def excluijodador():
    nome = input("Digite o nome de usuario: ")
    if os.path.isfile(nome+".txt"):
        print("Excluindo o jogador " + nome)
        os.remove(nome+".txt")
    else:
        print("Jogador não existente")

#Mostra quantas vitórias e quantas derrotas um jogador tem
def lehistorico():
    nome = input("Digite nome de jogador: ")
    if os.path.isfile(nome+".txt"):
        arquivo = open(nome + ".txt")
        historico = arquivo.readlines()
        vitorias = int(historico[0])
        derrotas = int(historico[1])
        print("Vitórias: {} Derrotas: {}".format(vitorias,derrotas))
    else:
        print("Jogador não existente")


#Matriz com o conteúdo do jogo
matriz = [
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ']
    ]


#Cria o tabuleiro do jogo
def imprimirjogo():
    tabuleiro = """
     {} | {} | {} | {} | {} 
    ---+---+---+---+---
     {} | {} | {} | {} | {} 
    ---+---+---+---+---
     {} | {} | {} | {} | {} 
    ---+---+---+---+---
     {} | {} | {} | {} | {} 
    ---+---+---+---+---
     {} | {} | {} | {} | {} 
    """.format(
    matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], matriz[0][4], 
    matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3], matriz[1][4],
    matriz[2][0], matriz[2][1], matriz[2][2], matriz[2][3], matriz[2][4],
    matriz[3][0], matriz[3][1], matriz[3][2], matriz[3][3], matriz[3][4],
    matriz[4][0], matriz[4][1], matriz[4][2], matriz[4][3], matriz[4][4],
    )

    print(tabuleiro)



#Executa o jogo
def iniciarjogo():
    
    contadorX = 0
    while contadorX < 1:
        nomeX = input("Nome do jogador X: ")
        if os.path.isfile(nomeX + ".txt") == False:
            print("Escreva um jogador existente!")
            contadorX -= 1
        contadorX += 1

    contador0 = 0
    while contador0 < 1:
        nome0 = input("Nome do jogador 0: ")
        if os.path.isfile(nome0 + ".txt") == False:
            print("Escreva um jogador existente!")
            contador0 -= 1
        elif nome0 == nomeX:
            print("Jogador ja selecionado!")
            contador0 -= 1
        contador0 += 1

    
    imprimirjogo()

    jogadas = 0

    while jogadas < 25:
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        
        if linha != 0 and linha != 1 and linha != 2 and linha != 3 and linha != 4:
            print("Digite um número válido!")
            jogadas -= 1
        elif coluna != 0 and coluna != 1 and coluna != 2 and coluna != 3 and coluna != 4:
            print("Digite um número válido!")
            jogadas -= 1
        else:
            if matriz[linha][coluna] == " ":
                if jogadas % 2 == 0:
                    matriz[linha][coluna] = "X"
                elif jogadas % 2 == 1:
                    matriz[linha][coluna] = "0"
            else:
                print("Posição ja ocupada escolha outra posição!")
                jogadas -= 1
        

        imprimirjogo()

        jogadas += 1

        #Funcao para contar a vitória ao X
        def Xganha():
            #Contar a vitoria no arquivo do jogador
            arquivo = open(nomeX + ".txt")
            pontos = arquivo.readlines()
            vitorias = int(pontos[0]) + 1
            derrotas = int(pontos[1])
            arquivo = open(nomeX + ".txt", "w+")
            arquivo.write("%s\n"%(vitorias))
            arquivo.write("%s"%derrotas)
            arquivo.close()
            
            #Contar a derrota no arquivo do jogador
            arquivo = open(nome0 + ".txt")
            pontos = arquivo.readlines()
            vitorias = int(pontos[0])
            derrotas = int(pontos[1]) + 1
            arquivo = open(nome0 + ".txt", "w+")
            arquivo.write("%s\n"%(vitorias))
            arquivo.write("%s"%derrotas)
            arquivo.close()

        #Funcao para contar a vitória ao 0
        def Oganha():
            #Contar a vitoria no arquivo do jogador
            arquivo = open(nome0 + ".txt")
            pontos = arquivo.readlines()
            vitorias = int(pontos[0]) + 1
            derrotas = int(pontos[1])
            arquivo = open(nome0 + ".txt", "w+")
            arquivo.write("%s\n"%(vitorias))
            arquivo.write("%s"%derrotas)
            arquivo.close()
            
            #Contar a derrota no arquivo do jogador
            arquivo = open(nomeX + ".txt")
            pontos = arquivo.readlines()
            vitorias = int(pontos[0])
            derrotas = int(pontos[1]) + 1
            arquivo = open(nomeX + ".txt", "w+")
            arquivo.write("%s\n"%(vitorias))
            arquivo.write("%s"%derrotas)
            arquivo.close()

            
        #28 formas de vencer

        empate = 1

        #X vence na horizontal cada dois if/elif uma linha do jogo
        if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X" and matriz[0][3] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[0][1] == "X" and matriz[0][2] == "X" and matriz[0][3] == "X" and matriz[0][4] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X" and matriz[1][3] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][1] == "X" and matriz[1][2] == "X" and matriz[1][3] == "X" and matriz[1][4] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X" and matriz[2][3] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[2][1] == "X" and matriz[2][2] == "X" and matriz[2][3] == "X" and matriz[2][4] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[3][0] == "X" and matriz[3][1] == "X" and matriz[3][2] == "X" and matriz[3][3] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[3][1] == "X" and matriz[3][2] == "X" and matriz[3][3] == "X" and matriz[3][4] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[4][0] == "X" and matriz[4][1] == "X" and matriz[4][2] == "X" and matriz[4][3] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[4][1] == "X" and matriz[4][2] == "X" and matriz[4][3] == "X" and matriz[4][4] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        

        #X vence na vertical cada dois if/elif uma coluna do jogo
        if matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X" and matriz[3][0] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][0] == "X" and matriz[2][0] == "X" and matriz[3][0] == "X" and matriz[4][0] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X" and matriz[3][1] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][1] == "X" and matriz[2][1] == "X" and matriz[3][1] == "X" and matriz[4][1] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X" and matriz[3][2] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][2] == "X" and matriz[2][2] == "X" and matriz[3][2] == "X" and matriz[4][2] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[0][3] == "X" and matriz[1][3] == "X" and matriz[2][3] == "X" and matriz[3][3] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][3] == "X" and matriz[2][3] == "X" and matriz[3][3] == "X" and matriz[4][3] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[0][4] == "X" and matriz[1][4] == "X" and matriz[2][4] == "X" and matriz[3][4] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][4] == "X" and matriz[2][4] == "X" and matriz[3][4] == "X" and matriz[4][4] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        

        #X vence na diagonal cada if/elif uma diagonal do jogo
        if matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X" and matriz[3][3] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[1][1] == "X" and matriz[2][2] == "X" and matriz[3][3] == "X" and matriz[4][4] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[1][0] == "X" and matriz[2][1] == "X" and matriz[3][2] == "X" and matriz[4][3] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[0][1] == "X" and matriz[1][2] == "X" and matriz[2][3] == "X" and matriz[3][4] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0


        elif matriz[0][4] == "X" and matriz[1][3] == "X" and matriz[2][2] == "X" and matriz[3][1] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[1][3] == "X" and matriz[2][2] == "X" and matriz[3][1] == "X" and matriz[4][0] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[0][3] == "X" and matriz[1][2] == "X" and matriz[2][1] == "X" and matriz[3][0] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[1][4] == "X" and matriz[2][3] == "X" and matriz[3][2] == "X" and matriz[4][1] == "X":
            print("Vitória do jogador: %s"% (nomeX))
            Xganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0



        #0 vence na horizontal cada dois if/elif uma linha do jogo
        if matriz[0][0] == "0" and matriz[0][1] == "0" and matriz[0][2] == "0" and matriz[0][3] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[0][1] == "0" and matriz[0][2] == "0" and matriz[0][3] == "0" and matriz[0][4] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[1][0] == "0" and matriz[1][1] == "0" and matriz[1][2] == "0" and matriz[1][3] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][1] == "0" and matriz[1][2] == "0" and matriz[1][3] == "0" and matriz[1][4] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[2][0] == "0" and matriz[2][1] == "0" and matriz[2][2] == "0" and matriz[2][3] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[2][1] == "0" and matriz[2][2] == "0" and matriz[2][3] == "0" and matriz[2][4] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[3][0] == "0" and matriz[3][1] == "0" and matriz[3][2] == "0" and matriz[3][3] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[3][1] == "0" and matriz[3][2] == "0" and matriz[3][3] == "0" and matriz[3][4] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[4][0] == "0" and matriz[4][1] == "0" and matriz[4][2] == "0" and matriz[4][3] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[4][1] == "0" and matriz[4][2] == "0" and matriz[4][3] == "0" and matriz[4][4] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        

        #0 vence na vertical cada dois if/elif uma coluna do jogo
        if matriz[0][0] == "0" and matriz[1][0] == "0" and matriz[2][0] == "0" and matriz[3][0] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][0] == "0" and matriz[2][0] == "0" and matriz[3][0] == "0" and matriz[4][0] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[0][1] == "0" and matriz[1][1] == "0" and matriz[2][1] == "0" and matriz[3][1] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][1] == "0" and matriz[2][1] == "0" and matriz[3][1] == "0" and matriz[4][1] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[0][2] == "0" and matriz[1][2] == "0" and matriz[2][2] == "0" and matriz[3][2] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][2] == "0" and matriz[2][2] == "0" and matriz[3][2] == "0" and matriz[4][2] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[0][3] == "0" and matriz[1][3] == "0" and matriz[2][3] == "0" and matriz[3][3] == "0":
            print("Vitória do jogador: %s"% (nomeX))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][3] == "0" and matriz[2][3] == "0" and matriz[3][3] == "0" and matriz[4][3] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[0][4] == "0" and matriz[1][4] == "0" and matriz[2][4] == "0" and matriz[3][4] == "0":
            print("Vitória do jogador: %s"% (nomeX))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        elif matriz[1][4] == "0" and matriz[2][4] == "0" and matriz[3][4] == "0" and matriz[4][4] == "0":
            print("Vitória do jogador: %s"% (nomeX))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        

        #0 vence na diagonal cada if/elif uma diagonal do jogo
        if matriz[0][0] == "0" and matriz[1][1] == "0" and matriz[2][2] == "0" and matriz[3][3] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[1][1] == "0" and matriz[2][2] == "0" and matriz[3][3] == "0" and matriz[4][4] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[1][0] == "0" and matriz[2][1] == "0" and matriz[3][2] == "0" and matriz[4][3] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[0][1] == "0" and matriz[1][2] == "0" and matriz[2][3] == "0" and matriz[3][4] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0


        elif matriz[0][4] == "0" and matriz[1][3] == "0" and matriz[2][2] == "0" and matriz[3][1] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[1][3] == "0" and matriz[2][2] == "0" and matriz[3][1] == "0" and matriz[4][0] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0

        elif matriz[0][3] == "0" and matriz[1][2] == "0" and matriz[2][1] == "0" and matriz[3][0] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
        
        elif matriz[1][4] == "0" and matriz[2][3] == "0" and matriz[3][2] == "0" and matriz[4][1] == "0":
            print("Vitória do jogador: %s"% (nome0))
            Oganha()
            #Terminar o jogo
            jogadas += 25
            empate = 0
    if empate != 0:
        print("A partida empatou!")

    #Zerar a matriz qundo termina o jogo
    matriz[0][0]= ' '
    matriz[0][1]= ' '
    matriz[0][2]= ' '
    matriz[0][3]= ' '
    matriz[0][4]= ' '
    matriz[1][0]= ' '
    matriz[1][1]= ' '
    matriz[1][2]= ' '
    matriz[1][3]= ' '
    matriz[1][4]= ' '
    matriz[2][0]= ' '
    matriz[2][1]= ' '
    matriz[2][2]= ' '
    matriz[2][3]= ' '
    matriz[2][4]= ' '
    matriz[3][0]= ' '
    matriz[3][1]= ' '
    matriz[3][2]= ' '
    matriz[3][3]= ' '
    matriz[3][4]= ' '
    matriz[4][0]= ' '
    matriz[4][1]= ' '
    matriz[4][2]= ' '
    matriz[4][3]= ' '
    matriz[4][4]= ' '
    
    
    
        

def main():
    while True:
        print("---------Menu---------")
        print("1 - Criar novo jogador")
        print("2 - Exibir histórico")
        print("3 - Excluir jogador")
        print("4 - Iniciar partida (Crie pelo menos dois jogadores(Opção 1) antes de iniciar uma partida)")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criarnovojogador()
        elif opcao == '2':
            lehistorico()
        elif opcao == '3':
            excluijodador()
        elif opcao == '4':
            iniciarjogo()


main()