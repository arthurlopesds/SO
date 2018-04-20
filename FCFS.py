def AlgFCFS():
    with open("so.txt","r") as arquivo:
        arq = arquivo.readlines()

    """
    A lógica apresentada nesse código para o algoritmo FCFS são calculos em um laço com limite para a quantidade de 
    processos, onde são calculados seu tempo de retorno, espera e resposta de acordo com os valores apresentados.
    
    """

    processos = []
    tChegada = []
    duracao = []
    retorno = 0
    TempodeRetorno = 0
    espera=0
    TempodeEspera=0
    resposta =0
    TempodeResposta=0

    for i in range(len(arq)):
        processos.append(arq[i].split())
        tChegada.append(int(processos[i][0])) #adicionando os tempos de Chegada em uma lista
        duracao.append(int(processos[i][1])) #adicionando os tempos de duração em outra lista

    tempoAtual = tChegada[0] #tempo de chegada do primeiro processo
    for i in range(len(arq)):
        retorno += duracao[i] #somando a duração de cada processo
        Tretorno = retorno - tChegada[i] + tempoAtual #tempo de retorno, é o retorno(que foi a soma anterior), menos seu
                                                      #tempo de chegada mais o tempo atual do processo

        espera = Tretorno - duracao[i] #tempo de espera é o tempo de retorno menos a duração do processo
        TempodeEspera += espera #somando os tempos de espera de cada processo

        TempodeResposta=TempodeEspera #e no FCFS o tempo de resposta é igual ao tempo de espera

        TempodeRetorno+=Tretorno #somando os tempos de retorno visto anteriormente

    print('FCFS {:.1f} {:.1f} {:.1f}'.format(TempodeRetorno/len(arq),TempodeResposta/len(arq),TempodeEspera/len(arq)))
    return