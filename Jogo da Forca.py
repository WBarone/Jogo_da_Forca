#A palavra escolhida
#Obs: para que seu amigo não veja a palavra escolhida iremos criar um novo arquivo python e extrair de lá a variável com a palavra escolhida
from palavraforca import palavra

#Lista com as letras que o usuário já tentou. Inicialmente ela começa vazia
letras_usuario = []

#Quantidade de chances que usuário tem
chances = 4

#Resultado do jogo
ganhou = False

#Criando a lógica do jogo:

while True:
#Vamos exibir quantas letras tem naquela palavra.
#Se a letra em questão estiver dentro da palavra escolhida, vamos exibir a letra [".lower()" para sempre exibir minúscula].
#Senão vamos exibir "-".
    for letra in palavra:
        if letra.lower() in letras_usuario:
            # Por padrão ele printa uma letra em cada linha (como se desse um "enter" ao final de cada print).
            # Queremos que as letras estejam uma do lado da outra, para isso incluiremos o comando [end=" "]
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Voce tem {chances} chances")

#Vamos colocar um input para sugestionar a ação do usuário
    tentativa = input("Escolha uma letra para adivinhar: ")

#Depois que o usuário digitar a letra, queremos adicionar essa letra na lista de tentativas (letras_usuario)
    letras_usuario.append(tentativa.lower())

#Caso a tentativa esteja errada, iremos subtrair em 1 o número de tentativas restantes do usuário.
#Obs:"-=1" é a mesma coisa que chances = chances - 1, só que escrito de maneira mais eficiente.
    if tentativa.lower() not in palavra.lower():
        chances -=1

#Agora vamos verificar caso o usuário ganhe.
#Essa situação é: todas as letras da palavra escolhida estão presentes na lista de letras tentadas ("letras_usuario")
    ganhou = True

#Vamos verificar se dentro da palavra escolhida, existe alguma letra que não foi tentada. Se for o caso, o jogo ainda continua
#Para isso, vamos fazer a lógica invertida: se a letra na "palavra" não estiver na lista das letras tentadas, ganhou é Falso
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

#Caso as chances do usuário se esgotem ou ele ganhe, encerramos o loop com "break"
    if chances == 0 or ganhou:
        break


#Resultado do jogo, de acordo com as ações do usuário
if ganhou:
    print(f"Parabéns, voce ganhou. A palavra era: {palavra}")
else:
    print(f"Voce perdeu! A palavra era: {palavra}")