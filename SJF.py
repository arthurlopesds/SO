def AlgSJF():
    process = []
    process2= []
    ord = []
    retorno = 0
    retorno=0
    TRetorno=0
    TempodeRetorno=0
    TempodeEspera=0
    TempodeResposta = 0
    flag=0

    """
    A lógica apresentada nesse código para o algoritmo SJF, consiste em ordenar os processos por ordem de chegada, 
    depois armazenar  o primeiro processo na lista "process", pegar o seu tempo de chegada e comparar com o restante 
    dos processos para saber quem chegou no mesmo tempo, vendo isso, se algum processo chegou nesse tempo, ele é 
    adicionado a lista "process" , se não, ele é adicionado na lista "process2", que no caso são os processos que vão 
    chegar depois. Após isso, o primeiro processo da lista "process" é removido, e assim ocorre uma comparação entre 
    o tempo de duração desse processo, com os processos que estão em "process2", para saber se chegaram em algum tempo 
    que o primeiro processo está executando, caso algum processo chegue nesse tempo,ele é adicionado a lista de 
    processos na lista "process" e logo após é ordenado por tempo de duração, os processos que não chegarem no tempo 
    em que o primeiro processo está executando é adicionado ao fim na lista "process" e são executados. Os calculos do
    tempo de retorno, espera e resposta, são feitos no fim após a lista de processos está ordenada da forma correta
    para a sua execução, consequentemente para o seu cálculo. 
    """

    with open("so.txt","r") as arquivo:
        arq = arquivo.readlines()

    def Ordena(v,indice): #função para ordenar os processos,tanto por ordem de chegada quando pela duração, isso depende
        for i in range(0, len(v) - 1):                                                         #do parametro
            for j in range(0, len(v) - 1 - i):
                if int(v[j][indice]) > int(v[j + 1][indice]):
                    v[j + 1], v[j] = v[j], v[j + 1]

    for i in range(len(arq)): # passando os valores para o lista ord
        process.append(arq[i].split())
        ord.append(process[i])

    process.clear() #zerando a lista process, porque no fim ele terá a sequencia correta

    Ordena(ord,0) #ordenando os processos por ordem de chegada
    process.append(ord[0])#adicionando o primeiro processo na lista process

    for i in range(1,len(ord)):  #verificando se existe algum processo com o mesmo tempo de chegada do primeiro
        if int(ord[i][0]) == int(process[0][0]):
            process.append(ord[i])
            indice = i
        else: #se nao tiver, é adicionado na lista process2
            process2.append(ord[i])

    Ordena(process,1) #ordena os processos com tempos iguais de acordo com a sua duração
    primeiro = process[0] #recebe o primeiro processo
    process.remove(process[0]) #remove o primeiro processo da lista

    j=0
    tam = len(process2)
    entrou = False  #flag para ajudar na remoção do processo da lista de processos
    for i in range(int(primeiro[1])): #limite da duração do primeiro processo
        j=0
        while j<tam:

            if int(process2[j][0]) == i: #verificando se algum processo da segunda lista, chegou no tempo em que o
                    entrou = True                            #primeiro processo excuta
                    process.append(process2[j]) #adiciona na lista de processos
                    if entrou:
                        process2.remove(process2[j])

                    Ordena(process,1) #ordena de acordo com sua duração
                    flag+=1 #flag para contar quantos processos entraram
                    tam = len(process2)
            j+=1 #incrementa j

            if entrou:
                j = 0 #para nao acessar um indice invalido da lista de process2
                entrou = False

    flag = len(process2) - flag #para verificar se ainda existem processos na lista process2
    process.insert(0,primeiro) #inserindo o primeiro processo na primeira posição da lista

    if flag>=0: #se a flag for maior ou igual a 0 é porque ainda existem processos na lista
        for i in range(len(process2)): #varro a lista
            process.append(process2[i]) #adiciona os processos que sobraram

    tempoAtual = int(process[0][0]) #tempo de chegada do primeiro processo

    for i in range(len(arq)):
        retorno += int(process[i][1]) #somando a duração de cada processo
        Tretorno = retorno - int(process[i][0]) + tempoAtual #tempo de retorno, é o retorno(que foi a soma anterior),
                                                        #menos seu tempo de chegada mais o tempo atual do processo

        espera = Tretorno - int(process[i][1]) #tempo de espera é o tempo de retorno menos a duração do processo
        TempodeEspera += espera #somando os tempos de espera de cada processo

        TempodeResposta = TempodeEspera #e no SFJ o tempo de resposta é igual ao tempo de espera

        TempodeRetorno += Tretorno #somando os tempos de retorno visto anteriormente



    print('SJF {:.1f} {:.1f} {:.1f}'.format(TempodeRetorno/len(arq),TempodeResposta/len(arq),TempodeEspera/len(arq)))

    return