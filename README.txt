Instruções para a correcta execução do programa:

1. Para colocar o jogo a correr é só abrir a aplicação, ou se preferir ver o código por trás é só abrir a aplicação num editor de código or IDE que aceite python, exemplo o PyCharm Community Edition, e clicar em "RUN", e a aplicação iniciará.
 
2. O ficheiro CSV com o nome resultado_jogos.csv, é onde está a ser gravado e consultado os dados de cada jogo ou partida, pode-se limpar o conteudo do ficheiro.



Instruções de Jogo:

//Inicio do jogo:

1. Ao executar o programa, irá ser exibido no ecrã, se existir, os dados referentes aos jogos e partidas anteriores, dados estes como: data, hora, partida número, o nome do jogador 1, o nome do jogador 2, e o respectivo vencedor;

2. Em seguida o programa pergunta "Pretende jogar contra quem? 1 - Máquina (Jogador Virtual)  2 - Outro Jogador Humano   Insire aqui o número 1 ou 2 da sua escolha:" -> Aqui deve inserir o número 1 se prende jogar contra a máquina, ou 2 se pretende jogar contra outro humano, ou seja, jogo entre 2 jogadores humanos, depois da sua escolha deve dar o "Enter" no seu teclado do computador;



//Se inseriu o número 1, ou seja, optou por jogar contra a máquina:

3. Se escolheu o número 1, no ponto anterior, ou seja, escolheu jogar contra a máquina, vai aparecer a seguinte pergunta no ecrâ, "Insire o nome do Jogador 1: ", o jogador 1 é o jogador humano, ou seja, você, aqui deve inserir o seu nome e depois dar o "Enter";

4. Em seguida aparede a seguinte questão, "Qual a peça que deseja usar para jogar, X or O (escreva a letra que pretende, X or O)?", deve escolher a peça com a qual pretende jogar, depois "Enter";

5. É imprimido o tabuleiro de jogo no ecrã, e uma pergunta a questionar onde pretende colocar a sua peça, como indicado abaixo:
"  |   |  
 ---------
   |   |  
 ---------
   |   |  
 É a tua vez. Inserira um número entre o 1 e o 9, para a localização da sua peça: "

Aqui, deve indicar qual a posição no tabuleiro que pretende colocar a sua peça de jogo, seguindo a seguinte logica:

  1 | 2 | 3 
 -----------
  4 | 5 | 6 
 -----------
  7 | 8 | 9

6. Depois de escolher a sua peça, a máquina escolherá a dela, e no ecrâ será apresentado o tabuleiro com a sua peça na posição que escolheu e a peça jogada pela máquina;

7. O programa volta a perguntar onde quer colocar a sua próxima peça, e novamente mostra o tabuleiro do jogo com as peças nas posições escolhidas por si e pela máquina, e assim sucessivamente, até existir um empate ou um vencedor;



//Se inseriu o número 2 no ponto 2, ou seja, optou por jogar o jogo entre 2 jogadores humanos:

8. Se no ponto 2, escolheu a opção 2, jogo entre 2 humanos, vai aparecer no ecrã a pergunta, "Insire o nome do Jogador 1: ", o jogador 1 é o primeiro jogador humano, por exemplo você, aqui deve inserir o seu nome e depois dar o "Enter";

9. Em seguida aparede a seguinte questão no ecrâ, "Qual a peça que deseja usar para jogar, X or O (escreva a letra que pretende, X or O)?", deve escolher a peça com a qual pretende jogar, depois "Enter";

10. Depois aparece no ecrã a pergunta, "Insire o nome do Jogador 2: ", o jogador 2 é o segundo jogador humano, aqui vai inserir o nome do seu adversário humano e depois dar o "Enter";

11. Aparece no ecrã o tabuleiro de jogo, e uma pergunta a questionar onde o jogador 1 pretende colocar a sua peça, como indicado abaixo:
"  |   |  
 ---------
   |   |  
 ---------
   |   |  
 (Jogador 1) é a tua vez. Inserira um número entre o 1 e o 9, para a localização da sua peça: : "

Aqui, o jogador 1, deve indicar qual a posição que pretende colocar a sua peça de jogo, seguindo a seguinte logica:

  1 | 2 | 3 
 -----------
  4 | 5 | 6 
 -----------
  7 | 8 | 9


12. Depois do jogador escolher a sua peça, no ecrâ será apresentado a peça na posição selecionada, e o programa faz a mesma pergunta ao jogador 2, e assim sucessivamente, até existir um empate ou um vencedor;


//Fim da partida:

13. Quando uma partida termina, aparece no programa a seguinte questão, "Pretende voltar a Jogar?  1 - Sim   2 - Não   Insira 1 ou 2 consoante a sua escolha.", se inserir o número 2, o jogo acaba e é impresso no ecrã os dados referentes ao jogo actual e aos jogos anteriores, dados este como: data, hora, partida número, o nome do jogador 1, o nome do jogador 2 e o respectivo vencedor; se inserir o número 1, o jogo continua, ou seja, voltam a jogar outra partida.
