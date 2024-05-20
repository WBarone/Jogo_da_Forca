# Jogo da Forca (Python)
Para construir o jogo da forca só precisamos utilizar as ferramentas básicas de Python, não é necessário baixar nenhuma biblioteca.

O primeiro parâmetro do jogo da forca é que existe uma palavra para ser adivinhada, então vamos acrescentar essa palavra em uma variável.

_Obs: para que seu amigo não veja a palavra escolhida, iremos criar um novo arquivo python (palavraforca) e extrair de lá a variável com a palavra escolhida_

    palavra = "python"

    from palavraforca import palavra

O segundo e terceiro passo é que temos que considerar as letras que o usuário já jogou e quantas chances ele tem para jogar (para fins de teste escolhi 4).

    letras_usuario = []

    chances = 4

Vamos criar também uma variável que vai receber verdadeiro ou falso dependendo do resultado do jogo -> ganhou = true -> perdeu = false

Vamos iniciar essa variável que vai se chamar -> “ganhou” como false.

    ganhou = False

# Criando a lógica do jogo

Todo o jogo essencialmente é um looping infinito, por isso vamos usar a estrutura de repetição While.

Vamos precisar de dois If’s, um If para quando o usuário perder e um If para quando o usuário ganhar, ambos os If’s encerram o jogo.

    While True:
  
    if ganhou:

        encerra o jogo

    if perdeu:

        encerra o jogo
        
Vamos criar um código que crie um espaço para representar cada letra da palavra que estiver na nossa variável “palavra”.

    for letra in palavra:

Exemplo: Se a palavra é Python o resultado será 6 espaços.

Por padrão o print vai deixar cada letra uma abaixo da outra na resposta, para corrigir isso acrescentamos nos parênteses do print o end, assim os espaços vão ficar um ao lado do outro.

No momento em que o usuário chutar uma letra correta, vamos substituir o espaço pela letra, caso contrário vamos colocar novamente o espaço.

Para melhorar o código vamos exibir para o usuário a cada tentativa a quantidade de chances que ele ainda tem:

    for letra in palavra:
        if letra.lower() in letras_usuario:
           print(letra, end=" ")
        else:
           print("_", end=" ")
    print(f"Voce tem {chances} chances")
  
_Obs: Usamos o lower() para que as letras fiquem todas minúsculas._

# Criando a estrutura
Vamos colocar um input para sugestionar a ação do usuário. Neste input o usuario consegue colocar uma letra.

    tentativa = input("Escolha uma letra para adivinhar: ")

Temos que adicionar essa letra na variável letras_usuario.

    letras_usuario.append(tentativa.lower())

Agora, se o usuário errar a letra, temos que tirar dele uma chance.

    if tentativa.lower() not in palavra.lower():
        chances -=1

Feito isso, agora temos que analisar a situação caso o usuário ganhe o jogo.

A situação em que ele ganha é **quando todas as palavras que ele jogou estão contidas na nossa variável letras_usuario**, ou seja, todas as letras da palavra “Python”, sendo a palavra que escolhemos para ser adivinhada, estão contidas na variável letras_usuario. **Mas como fazer esta verificação?**

Aqui vamos aplicar a lógica contrária que já usamos. Vamos iniciar dizendo que ele ganhou, ou seja, que a variável ganhou começa verdadeira.

Depois vamos verificar se alguma letra da palavra está faltando na variável letras_usuario então o resultado é falso e se todas estiverem o resultado é verdadeiro e o usuário ganhou o jogo.

    ganhou = True

    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

Até aqui ele pode ou ganhar o jogo, ou esgotar suas chances. De qualquer forma, encerramos o loop com “break”.

    if chances == 0 or ganhou:
        break
    
Por fim, finalizamos com um print, informando o resultado do jogo de acordo com as ações do usuário.

    if ganhou:
        print(f"Parabéns, voce ganhou. A palavra era: {palavra}")
    else:
        print(f"Voce perdeu! A palavra era: {palavra}")

# Conclusão
Quando estamos criando um jogo existem duas lógicas que temos que nos preocupar, uma delas é como o jogo vai ser organizado para funcionar como esperamos e a segunda é o que vamos mostrar para o usuário e o que o usuário vai inserir no jogo.
