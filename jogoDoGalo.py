import random
import csv
from datetime import datetime
from abc import ABC, abstractmethod

today_aux = datetime.now()
today = today_aux.strftime("%d/%m/%Y %H:%M:%S")

tabuleiro_jogo = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


class Tabuleiro:

    def __init__(self):
        self.tabuleiro_jogo = tabuleiro_jogo

    # Imprimir o tabuleiro no ecrã
    def imprimir_tabuleiro(self):
        print(self.tabuleiro_jogo[0] + " | " + self.tabuleiro_jogo[1] + " | " + self.tabuleiro_jogo[2])
        print("---------")
        print(self.tabuleiro_jogo[3] + " | " + self.tabuleiro_jogo[4] + " | " + self.tabuleiro_jogo[5])
        print("---------")
        print(self.tabuleiro_jogo[6] + " | " + self.tabuleiro_jogo[7] + " | " + self.tabuleiro_jogo[8])

    # Verificar quem ganhou ou se foi um empate - Verificar Linha Horizontal, Verificar Linha Vertical e Verificar Linha Obliqua
    def verificar_linha_horizontal(self, jogador1, jogador_nome1, jogador_nome2):
        global vencedor
        if self.tabuleiro_jogo[0] == self.tabuleiro_jogo[1] == self.tabuleiro_jogo[2] and self.tabuleiro_jogo[0] != " ":
            if self.tabuleiro_jogo[0] == jogador1:
                vencedor = jogador_nome1 + " (Jogador 1)"
            else:
                vencedor = jogador_nome2 + " (Jogador 2)"
            return 1
        elif self.tabuleiro_jogo[3] == self.tabuleiro_jogo[4] == self.tabuleiro_jogo[5] and self.tabuleiro_jogo[3] != " ":
            if self.tabuleiro_jogo[3] == jogador1:
                vencedor = jogador_nome1 + " (Jogador 1)"
            else:
                vencedor = jogador_nome2 + " (Jogador 2)"
            return 1
        elif self.tabuleiro_jogo[6] == self.tabuleiro_jogo[7] == self.tabuleiro_jogo[8] and self.tabuleiro_jogo[6] != " ":
            if self.tabuleiro_jogo[6] == jogador1:
                encedor = jogador_nome1 + " (Jogador 1)"
            else:
                vencedor = jogador_nome2 + " (Jogador 2)"
            return 1

    def verificar_linha_vertical(self, jogador1, jogador_nome1, jogador_nome2):
        global vencedor
        if self.tabuleiro_jogo[0] == self.tabuleiro_jogo[3] == self.tabuleiro_jogo[6] and self.tabuleiro_jogo[0] != " ":
            if self.tabuleiro_jogo[0] == jogador1:
                vencedor = jogador_nome1 + " (Jogador 1)"
            else:
                vencedor = jogador_nome2 + " (Jogador 2)"
            return 1
        elif self.tabuleiro_jogo[1] == self.tabuleiro_jogo[4] == self.tabuleiro_jogo[7] and self.tabuleiro_jogo[1] != " ":
            if self.tabuleiro_jogo[1] == jogador1:
                vencedor = jogador_nome1 + " (Jogador 1)"
            else:
                vencedor = jogador_nome2 + " (Jogador 2)"
            return 1
        elif self.tabuleiro_jogo[2] == self.tabuleiro_jogo[5] == self.tabuleiro_jogo[8] and self.tabuleiro_jogo[2] != " ":
            if self.tabuleiro_jogo[2] == jogador1:
                vencedor = jogador_nome1 + " (Jogador 1)"
            else:
                vencedor = jogador_nome2 + " (Jogador 2)"
            return 1

    def verificar_linha_obliqua(self, jogador1, jogador_nome1, jogador_nome2):
        global vencedor
        if self.tabuleiro_jogo[0] == self.tabuleiro_jogo[4] == self.tabuleiro_jogo[8] and self.tabuleiro_jogo[0] != " ":
            if self.tabuleiro_jogo[0] == jogador1:
                vencedor = jogador_nome1 + " (Jogador 1)"
            else:
                vencedor = jogador_nome2 + " (Jogador 2)"
            return 1
        elif self.tabuleiro_jogo[2] == self.tabuleiro_jogo[4] == self.tabuleiro_jogo[6] and self.tabuleiro_jogo[2] != " ":
            if self.tabuleiro_jogo[2] == jogador1:
                vencedor = jogador_nome1 + " (Jogador 1)"
            else:
                vencedor = jogador_nome2 + " (Jogador 2)"
            return 1

    def verificar_vencedor(self, jogador1, jogador_nome1, jogador_nome2, jogo_numero):
        if self.verificar_linha_horizontal(jogador1, jogador_nome1, jogador_nome2) == 1 or self.verificar_linha_vertical(jogador1, jogador_nome1, jogador_nome2) == 1 or self.verificar_linha_obliqua(jogador1, jogador_nome1, jogador_nome2) == 1:
            self.imprimir_tabuleiro()
            txt = "O vencedor é {}"
            print(txt.format(vencedor))

            # abrir  o arquivo para gravar os resultados da partida terminada
            f = open('resultado_jogos.csv', 'a', encoding='utf-8', newline='')

            with f:
                # criar o objeto de gravação
                w = csv.writer(f)

                # gravar as linhas
                w.writerow([today, jogador_nome1, jogador_nome2, jogo_numero, vencedor])

            # fechar o arquivo
            # w.close()

            # Jogo Acabou
            return 0
        else:
            # Jogo Continua
            return 1

    def verificar_empate(self, jogador_nome1, jogador_nome2, jogo_numero):
        if " " not in self.tabuleiro_jogo:
            self.imprimir_tabuleiro()
            print("É um empate!!!")

            # abrir  o arquivo para gravar os resultados da partida terminada
            f = open('resultado_jogos.csv', 'a', encoding='utf-8', newline='')

            with f:
                # criar o objeto de gravação
                w = csv.writer(f)
                # gravar as linhas
                w.writerow([today, jogador_nome1, jogador_nome2, jogo_numero, 'Empate!'])

            # fechar o arquivo
            # w.close()

            # Jogo Acabou
            return 0
        else:
            # Jogo Continua
            return 1

    # Limpar o tabuleiro - voltar a colocar o tabuleiro com as posições a vazio
    def limpar_tabuleiro(self, tabuleiro):
        i=0
        while i<9:
            tabuleiro[i] = " "
            i+=1

# Classe Pai - Super Classe - Aplicação de Herança, Abstração e Encapsulamento
class Jogador:
    def __init__(self, nome="Sónia Costa", id=1, peca_escolhida="X"):
        self.nome = nome
        self.id = id
        self.peca_escolhida = peca_escolhida

    # Imprimir no ecrã os dados do jogador
    def imprimir_jogador(self):
        print(self.id, self.nome, self.peca_escolhida)

    # Returnar o nome do jogador no ecrã
    def get_nome(self):
        return self.nome

    # Actualizar os dados do jogador
    def actualizar_jogador(self, res_nome, re_id, res_peca):
        self.nome = res_nome
        self.id = re_id
        self.peca_escolhida=res_peca
        print(self.id, self.nome, self.peca_escolhida)

    # Jogada do Jogador - Médodo abstrato e polimorfismo
    @abstractmethod
    def joga_jogador(self):
        pass


# Classe Filha da classe Jogador - Subclasse - Aplicação da Herança
class JogadorHumano(Jogador):
    def __init__(self, nome, id, peca_escolhida):
        Jogador.__init__(self, nome, id, peca_escolhida)

    # Get o input dos jogadores humanos 1 e 2 - Jogada do Jogador Humano - Aplicação de polimorfismo
    def joga_jogador(self, tabuleiro, tipo_jogador):
        if tipo_jogador == 2:
            if self.id == 1:
                jogador_nome = self.nome + " (Jogador 1) é a tua vez. "
            else:
                jogador_nome = self.nome + " (Jogador 2) é a tua vez. "
        else:
            jogador_nome = "É a tua vez. "
        entrada = input(jogador_nome + "Inserira um número entre o 1 e o 9, para a localização da sua peça: ")
        if entrada.isnumeric():
            if 1 <= int(entrada) <= 9 and tabuleiro[int(entrada) - 1] == " ":
                tabuleiro[int(entrada) - 1] = self.peca_escolhida
                return 1
            elif 1 > int(entrada) > 9:
                print("Casa " + entrada + " não existe no tabuleiro!!!")
                return 0
            else:
                print("Casa " + entrada + " ocupada!!!")
                return 0
        else:
            print("Por favor, insire um número inteiro entre 1 e 9.")
            return 0


# Classe Filha da classe Jogador - Subclasse - Aplicação da Herança
class JogadorMaquina(Jogador):
    def __init__(self, nome='Jogador Virtual', id=1, peca_escolhida='x'):
        Jogador.__init__(self, nome, id, peca_escolhida)

    # Jogar contra a Máquina - Jogada do Jogador Virtual - Aplicação de polimorfismo
    def joga_jogador(self, tabuleiro, tipo_jogador):
        voltar_a_lancar_posicao=1
        if tipo_jogador == self.peca_escolhida:
            while voltar_a_lancar_posicao == 1:
                posicao_jogador_virtual = random.randint(0, 8)
                if tabuleiro[posicao_jogador_virtual] == " ":
                    tabuleiro[posicao_jogador_virtual] = tipo_jogador
                    voltar_a_lancar_posicao = 0
                else:
                    if " " in tabuleiro:
                        voltar_a_lancar_posicao = 1
                    else:
                        voltar_a_lancar_posicao = 0
            if voltar_a_lancar_posicao == 0:
                return 1  # Pode mudar para o próximo jogador
            else:
                return 0
        else:
            return 0  # Não pode mudar para o próximo jogador


# Classe só criada para demonstrar a aplicação de sobrecraga de operadores - na realidade não preciso dela para a execução da aplicação
class Avaliacao:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # subrecarga do operador "==" - Só para exemplo de sobrecarga de operadores
    def __eq__(self, z):
        aux1 = self.x + self.y
        aux2 = z.x + z.y
        print(aux1)
        print(aux2)
        if int(aux1) == int(aux2):
            print("Jogo equilibrado!")
        else:
            print("Jogo não equilibrado!")


class Jogar:

    def __init__(self):
        # Outras variáveis importates para o jogo correr

        jogador_maquina = jogador2 = None
        jogador1 = jogador_actual = None
        muda_de_jogador = jogo_em_andamento = voltar_ao_inicio = voltar_a_escolha = muda_para_jogador_humano = 1   # -> 1 = True ; 0 = False
        adversario = jogador_numero = jogo_numero = 1
        jogadas_jogador_A = jogadas_jogador_B = jogadas_por_partida = 0 # -> Inicialização de valores a zero que serão encrementados durante o jogo

        self.mostrar_resultados_anteriores()

        tabuleiro_obj = Tabuleiro()

        while voltar_a_escolha == 1 :
            adversario = self.escolha_adversario()

            if adversario == 2:
                print("\nJogo Do Galo para jogar 2 jogadores humanos.\n")
                voltar_a_escolha = 0
            elif adversario == 1:
                print("\nJogo Do Galo para jogar contra máquina.\n")
                voltar_a_escolha = 0
            else:
                print("Tipo de adversário não foi escolhido. Escolha novamente.")
                voltar_a_escolha = 1

        if adversario != 0:
            # Jogador 1 escolhe a peça
            jogador1_dados = input("Insire o nome Jogador 1: ")

            while voltar_ao_inicio == 1:
                escolha = input("Qual a peça que deseja usar para jogar, X or O (escreva a letra que pretende, X or O)? ")

                if escolha == "O" or escolha == "o":
                    jogador_actual = jogador1 = "O"
                    jogador_maquina = jogador2 = "X"
                    if adversario == 2:
                        jogador2_dados = input("Insire o nome Jogador 2: ")
                        jogadores = [JogadorHumano(jogador1_dados, 1, jogador_actual),
                                     JogadorHumano(jogador2_dados, 2, jogador2)]
                    else:
                        jogadores = [JogadorHumano(jogador1_dados, 1, jogador_actual)]
                        maquina = [JogadorMaquina('Jogador Virtual', 1, jogador_maquina)]
                    voltar_ao_inicio = 0
                elif escolha == "X" or escolha == "x":
                    jogador_actual = jogador1 = "X"
                    jogador_maquina = jogador2 = "O"
                    if adversario == 2:
                        jogador2_dados = input("Insire o nome Jogador 2: ")
                        jogadores = [JogadorHumano(jogador1_dados, 1, jogador_actual),
                                     JogadorHumano(jogador2_dados, 2, jogador2)]
                    else:
                        jogadores = [JogadorHumano(jogador1_dados, 1, jogador_actual)]
                        maquina = [JogadorMaquina('Jogador Virtual', 1, jogador_maquina)]
                    voltar_ao_inicio = 0
                else:
                    print("Valor Incorreto!!!.")
                    voltar_ao_inicio = 1

            while jogo_em_andamento:
                jogadas_por_partida += 1

                if jogador_actual == 'X':
                    jogadas_jogador_A += 1
                else:
                    jogadas_jogador_B += 1

                tabuleiro_obj.imprimir_tabuleiro()
                tabuleiro = tabuleiro_obj.tabuleiro_jogo

                jogador_nome1 = jogadores[0].get_nome()
                muda_de_jogador = jogadores[jogador_numero - 1].joga_jogador(tabuleiro, adversario)

                if muda_de_jogador == 1:
                    if adversario == 2:
                        if jogador_numero == 1:
                            jogador_numero = 2
                        else:
                            jogador_numero = 1

                        jogador_nome2 = jogadores[1].get_nome()

                        jogo_em_andamento = tabuleiro_obj.verificar_vencedor(jogador1, jogador_nome1, jogador_nome2, jogo_numero)
                        if jogo_em_andamento == 1:
                            jogo_em_andamento = tabuleiro_obj.verificar_empate(jogador_nome1, jogador_nome2, jogo_numero)
                            # jogo_em_andamentojogo_em_andamento = self.continuar_jogar()
                            if jogo_em_andamento == 0:
                                self.mostrar_resultados_anteriores()
                                break

                        else:
                            print("Jogo terminado!!!")
                            jogo_numero += 1

                            # Sobrecargar exemplo - Início
                            a = [Avaliacao(jogadas_por_partida, jogadas_jogador_A)]
                            b = [Avaliacao(jogadas_por_partida, jogadas_jogador_B)]
                            a == b
                            # Sobrecargar exemplo - Fim

                            jogo_em_andamento = self.continuar_jogar()
                            if jogo_em_andamento == 1:
                                tabuleiro_obj.limpar_tabuleiro(tabuleiro)
                            else:
                                self.mostrar_resultados_anteriores()
                                break

                    jogador_actual = self.alterar_jogador1_para_jogador2(jogador_actual, muda_de_jogador, jogo_em_andamento)

                    if adversario == 1:

                        muda_para_jogador_humano = maquina[0].joga_jogador(tabuleiro, jogador_actual)

                        if muda_para_jogador_humano == 1:
                            jogador_actual=self.alterar_jogador1_para_jogador2(jogador_actual, muda_de_jogador, jogo_em_andamento)
                        else:
                            print("Aconteceu algum erro! Jogo Terminado! Desculpe, pelo encomedo. Tente jogar novamente.")
                            jogo_numero += 1
                            jogo_em_andamento = self.continuar_jogar()
                            if jogo_em_andamento == 1:
                                tabuleiro_obj.limpar_tabuleiro(tabuleiro)
                            else:
                                self.mostrar_resultados_anteriores()
                                break

                        jogo_em_andamento = tabuleiro_obj.verificar_vencedor(jogador1, jogador_nome1, "Jogador Virtual", jogo_numero)
                        if jogo_em_andamento == 1:
                            jogo_em_andamento = tabuleiro_obj.verificar_empate(jogador_nome1, "Jogador Virtual", jogo_numero)
                            # jogo_em_andamento = self.continuar_jogar()
                            if jogo_em_andamento == 1:
                                jogo_numero += 1
                            else:
                                self.mostrar_resultados_anteriores()
                                break
                        else:
                            print("Jogo terminado!!!")
                            jogo_numero += 1

                            # Sobrecargar exemplo - Início
                            a = [Avaliacao(jogadas_por_partida, jogadas_jogador_A)]
                            b = [Avaliacao(jogadas_por_partida, jogadas_jogador_B)]
                            a == b
                            # Sobrecargar exemplo - Fim

                            jogo_em_andamento = self.continuar_jogar()
                            if jogo_em_andamento == 1:
                                tabuleiro_obj.limpar_tabuleiro(tabuleiro)
                            else:
                                self.mostrar_resultados_anteriores()
                                break

    # Jogador 1 escolhe tipo de adversário
    def escolha_adversario(self):
        adversario = input("Pretende jogar contra quem?\n1 - Máquina (Jogador Virtual)\n2 - Outro Jogador Humano\nInsire aqui o número 1 ou 2 da sua escolha: ")
        if adversario == str(1):
            return 1
        elif adversario == str(2):
            return 2
        else:
            return 0

    # Mudar de Jogado 1 para o Jogador 2 - Jogar entre Jogadores Humanos e Máquina
    def alterar_jogador1_para_jogador2(self, jogador_actual, muda_de_jogador, jogo_em_andamento):
        if muda_de_jogador == 1 and jogo_em_andamento == 1:
            if jogador_actual == "O":
                return "X"
            else:
                return "O"
        else:
            pass

    # Perguntar ao jogador se pretende acabar ou continuar o jogo
    def continuar_jogar(self):
        voltar_a_jogar_resposta = input("Pretende voltar a Jogar?\n1 - Sim\n2 - Não\nInsira 1 ou 2 consoante a sua escolha. ")
        if voltar_a_jogar_resposta == str(1):
            return 1
        else:
            return 0

    # Abrir o ficheiro CSV, que tem os dados dos jogos anteriores e imprimir no ecrã
    def mostrar_resultados_anteriores(self):
        # abrir o arquivo
        with open('resultado_jogos.csv', encoding='utf-8') as arquivo_referencia:

            # ler o arquivo
            tabela = csv.reader(arquivo_referencia)

            print("\n\n---------------------")
            print("Lista dos jogos, jogadores e vencedores")
            print("Data e Horas do Jogo ------ Jogo Número ------ Jogador 1 ------ Jogador 2 ------ Vencedor")

            # navegar pelo arquivo
            for l in tabela:
                if len(l) > 0:
                    jogo_data = l[0]
                    jogador_jogo1 = l[1]
                    jogador_jogo2 = l[2]
                    id_jogo = l[3]
                    nome_vencedor = l[4]

                    print(jogo_data, '------', id_jogo, '------', jogador_jogo1, '------', jogador_jogo2, '------', nome_vencedor)
            print("---------------------\n\n")


# main -> Chamar as funçóes que criam e correm o jogo, para os jogadores poderem jogar
if __name__ == '__main__':
    Jogar()
