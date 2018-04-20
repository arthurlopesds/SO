def AlgRR ():
    class Processo:

        def __init__(self,tempo,duracao,retorno,espera,resposta,tUlt,pExec,pico):
           self.tempo = tempo
           self.duracao = duracao
           self.retorno = retorno
           self.espera = espera
           self.resposta = resposta
           self.tUlt = tUlt
           self.pExec = pExec
           self.pico = pico

        def obterTChegada(self):
            return self.tempo

        def obterDuracao(self):
            return self.duracao

        def obterRetorno(self):
            return self.retorno

        def obterEspera(self):
            return self.espera

        def obterReposta(self):
            return self.resposta

        def obtertempoUlt(self):
            return self.tUlt

        def obterPexec(self):
            return self.pExec

        def obterPico(self):
            return  self.pico
        """
        A lógica apresentada nesse código para o algoritmo RR, consiste em dividir os processos em 4 filas,
        a fila de processos, que contém todos os processos, a fila de esperando que vai conter todos processos que estão
        esperando para serem executados, a fila de prontos que são os procesos pronto para a execução, e a fila de
        finalizados que são os processos que ja acabaram as suas execuções. Primeiro, os processos são ordenados por 
        tempo de chegada. O tempo começa a contar e acontece uma verificação para saber qual processo chegou em qual 
        tempo, os processos que chegaram em seu tempo, são movidos para a fila de prontos, lá, quando chegam a sua vez, 
        eles são executados, ou seja, descontando o valor do quantum em sua duração e logo após colocando-os atrás de 
        todos na fila,quando um processo,acaba sua execução ele é removido da fila de prontos e movido para a lista de 
        finalizados. O tempo de retorno e espera são calculados assim que o processo termina de ser executado, e o tempo
        de resposta logo no inicio quando ocorre a primeira execução.
        
        """

    processos = []
    receb = []
    esperando = []
    prontos = []
    finalizados = []
    time = 0
    Quantum = 2
    TempoRetorno = 0
    TempoEspera = 0
    TempoResposta = 0

    with open("so.txt","r") as arquivo:
        arq = arquivo.readlines()

    for i in range(len(arq)): #adicionando valores do arquivo aos objetos
        receb.append(arq[i].split())
        processos.append(Processo(int(receb[i][0]),int(receb[i][1]),0,0,0,0,False,int(receb[i][1]))) #inicializando
                                        # e adicionando os processos numa lista de objetos

    esperando = sorted(processos,key=Processo.obterTChegada) #ordenando os processos por tempo de chegada


    while len(finalizados) != len(processos):

        for i in range(len(esperando)):  # verifica se chegou algum processo no time especificado
            if time == esperando[i].obterTChegada():
                prontos.append(esperando[i])

        if len(prontos) == 0: #se verificou e nao tiver ngm na lista de prontos , passa o tempo, até achar alguém no começo
            time+=1           #serve para o começo quando nao tiver processos que começam no 0
        i=0
        k = 0
        passatempo = 1 #adc +1 no tempo

        while k < len(prontos): #de acordo com o tamanho da lista de prontos
            for j in range(Quantum): #descontar o quantum de 1 por 1

                    if prontos[i].obterPexec() == False: #verificando se é a primeira execução do processo
                        prontos[i].pExec = True #trocando valor para verdadeiro, indicando que não é mais a primeira Exec
                        prontos[i].resposta = time - prontos[i].obterTChegada() #calculando o tempo de resposta, ou seja,
                        #desde quando o processo aparece, até a primeira resposta, que é quando começa a executar

                    prontos[i].duracao = prontos[i].obterDuracao() - 1 #desconto 1 do quantum
                    entra = prontos[i].obterDuracao() #flag para verificar quando um processo falta apenas 1 de pico
                                                      #para acabar a execução

                    if entra == 0: #em algum caso que só faltar 1 de duração
                        time += passatempo
                        for i in range(len(esperando)):  # verifica se chegou algum processo no tempo atual
                            if time == esperando[i].obterTChegada():
                                prontos.append(esperando[i])
                        i = 0
                        break #para parar o for do quantum para não descontar mais no valor de duração do processo, ja
                              #que ele chegou a 0

                    else:
                        time+=passatempo #passa o tempo
                        for i in range(len(esperando)):  # verifica se chegou algum processo no tempo atual
                            if time == esperando[i].obterTChegada():
                                prontos.append(esperando[i])
                        i = 0


            #print('Processo{} = {}'.format(i+k,prontos[i].obterDuracao()))

            if prontos[i].obterDuracao() <= 0: #se a duração do processo for menor ou igual a zero

                prontos[i].retorno = time - prontos[i].obterTChegada() #calculando o retorno de cada processo
                                                                       #o tempo atual - o tempo de chegada dos mesmo
                prontos[i].espera = prontos[i].obterRetorno() - prontos[i].obterPico() #calculando o tempo de espera
                                                                                       #o tempo de retorno - o pico do
                                                                                       # processo correspondente

                finalizados.append(prontos[i])  #assim que acabou sua execução é movido para fila de finalizados
                prontos.remove(prontos[i])      # e removendo da fila de prontos


            else: #colocando o processo atual no fim da fila
                insere=prontos[i]
                prontos.remove(prontos[i])
                prontos.append(insere)
            i=0
            k+=1

    for i in range(len(finalizados)):  #calculo das somas de todos os retornos,esperas e respostas dos processos
        TempoRetorno += finalizados[i].obterRetorno()
        TempoEspera += finalizados[i].obterEspera()
        TempoResposta += finalizados[i].obterReposta()

    print('RR {:.1f} {:.1f} {:.1f}'.format(TempoRetorno/len(finalizados),TempoResposta/len(finalizados),TempoEspera/len(finalizados)))

    return