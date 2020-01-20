import random
from time import time

def TreinadorAritmetico():
    class Inputs:
        Operacao = ""
        dificuldade = ""
        resposta = ""


    def definirOperacao():
        try:
            Inputs.Operacao = input("Digite a operação (*, /, -, +): ")

        except ValueError:
            print("Digite um valor válido")
            definirOperacao()


    definirOperacao()


    def definirDificuldade():
        try:
            Inputs.dificuldade = int(input("Digite a dificulade (1 a 10): "))
        except ValueError:
            print("Digite um valor válido")
            definirDificuldade()

    definirDificuldade()


    def Jogo(Parametro1, Parametro2, casasDecimais):
        score = 0
        parametro1 = Parametro1
        parametro2 = Parametro2

        numero1 = random.randint(parametro1, parametro2) + round(random.random(), casasDecimais)
        numero2 = random.randint(parametro1, parametro2) + round(random.random(), casasDecimais)

        def definirResposta():
            try:
                Inputs.resposta = float(input("Resolva: {} {} {}: ".format(numero1, operacao, numero2)))
            except ValueError:
                definirResposta()

        if Inputs.Operacao == "*":
            tempoInicial = time()

            while True:
                operacao = "*"
                definirResposta()
                resultado = numero1 * numero2

                if Inputs.resposta == resultado:
                    print("Correto")
                    numero1 = random.randint(parametro1, parametro2) + \
                              round(random.random(), casasDecimais)
                    numero2 = random.randint(parametro1, parametro2) + \
                              round(random.random(), casasDecimais)
                    score += 1

                else:
                    tempoFinal = time()
                    tempoTotal = int(tempoFinal - tempoInicial)
                    print("Errado, sua pontuação foi de {} pontos em {} segundos"
                          .format(score, tempoTotal))
                    print("Perfomance: ", score / tempoTotal)
                    print("A resposta certa era:", resultado)

                    perguntaFinal = input("Gostaria de jogar novamente? (S/N): ")
                    if perguntaFinal.lower() == "s":
                        TreinadorAritmetico()
                    else:
                        exit()

        if Inputs.Operacao == "/":
            tempoInicial = time()
            while True:
                operacao = "/"
                definirResposta()
                resultado = numero1 / numero2

                if Inputs.resposta == resultado:
                    print("Correto")
                    numero1 = random.randint(parametro1, parametro2) + \
                              round(random.random(), casasDecimais)
                    numero2 = random.randint(parametro1, parametro2) + \
                              round(random.random(), casasDecimais)
                    score += 1
                else:
                    tempoFinal = time()
                    tempoTotal = int(tempoFinal - tempoInicial)
                    print("Errado, sua pontuação foi de {} pontos em {} segundos"
                          .format(score, tempoTotal))
                    print("Perfomance: ", score / tempoTotal)
                    print("A resposta certa era:", resultado)

                    perguntaFinal = input("Gostaria de jogar novamente? (S/N): ")
                    if perguntaFinal.lower() == "s":
                        TreinadorAritmetico()
                    else:
                        exit()

        if Inputs.Operacao == "+":
            tempoInicial = time()
            while True:
                operacao = "+"
                definirResposta()
                resultado = numero1 + numero2

                if Inputs.resposta == resultado:
                    print("Correto")
                    numero1 = random.randint(parametro1, parametro2) + \
                              round(random.random(), casasDecimais)
                    numero2 = random.randint(parametro1, parametro2) + \
                              round(random.random(), casasDecimais)
                    score += 1
                else:
                    tempoFinal = time()
                    tempoTotal = int(tempoFinal - tempoInicial)
                    print("Errado, sua pontuação foi de {} pontos em {} segundos"
                          .format(score, tempoTotal))
                    print("Perfomance: ", score / tempoTotal)
                    print("A resposta certa era:", resultado)

                    perguntaFinal = input("Gostaria de jogar novamente? (S/N): ")
                    if perguntaFinal.lower() == "s":
                        TreinadorAritmetico()
                    else:
                        exit()

        if Inputs.Operacao == "-":
            tempoInicial = time()
            while True:
                operacao = "-"
                definirResposta()
                resultado = numero1 - numero2

                if Inputs.resposta == resultado:
                    print("Correto")

                    numero1 = random.randint(parametro1, parametro2) + \
                              round(random.random(), casasDecimais)
                    numero2 = random.randint(parametro1, parametro2) + \
                              round(random.random(), casasDecimais)

                    score += 1
                else:
                    tempoFinal = time()
                    tempoTotal = int(tempoFinal - tempoInicial)

                    print("Errado, sua pontuação foi de {} pontos em {} segundos"
                          .format(score, tempoTotal))

                    print("Perfomance: ", score / tempoTotal)

                    print("A resposta certa era:", resultado)

                    perguntaFinal = input("Gostaria de jogar novamente? (S/N): ")
                    if perguntaFinal.lower() == "s":
                        TreinadorAritmetico()
                    else:
                        exit()

    if Inputs.dificuldade == 1:
        Jogo(1, 10, 0)

    if Inputs.dificuldade == 2:
        Jogo(1, 100, 0)

    if Inputs.dificuldade == 3:
        Jogo(1, 100, 1)

    if Inputs.dificuldade == 4:
        Jogo(1, 100, 2)

    if Inputs.dificuldade == 5:
        Jogo(1, 100, 4)

    if Inputs.dificuldade == 6:
        Jogo(1, 100, 8)

    if Inputs.dificuldade == 7:
        Jogo(1, 1000, 10)

    if Inputs.dificuldade == 8:
        Jogo(1, 10000, 10)

    if Inputs.dificuldade == 9:
        Jogo(1, 10000, 15)

    if Inputs.dificuldade == 10:
        Jogo(1, 100000, 30)


TreinadorAritmetico()
