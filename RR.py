class Processo:

    def __init__(self,tempo,duracao):
       self.tempo = tempo
       self.duracao = duracao

    def TempoEspera(self,espera):
        self.espera = espera

    def obterTChegada(self):
        return self.tempo

    def obterDuracao(self):
        return self.duracao

    def obterEspera(self):
        return self.espera

processos = []
receb = []
esperando = []
prontos = []
finalizados = []
time = 0
Quantum = 2

with open("so.txt","r") as arquivo:
    arq = arquivo.readlines()

for i in range(len(arq)): #adicionando valores do arquivo aos objetos
    receb.append(arq[i].split())
    processos.append(Processo(int(receb[i][0]),int(receb[i][1])))

esperando = sorted(processos,key=Processo.obterTChegada) #ORDENANDO OS PROCESSOS POR TEMPO DE CHEGADA

for i in range (len(esperando)):  #PRINT PRA TESTE
    print(esperando[i].obterTChegada())
    print(esperando[i].obterDuracao())
    print('\n')

i=0
while len(finalizados)!= len(processos):

    for i in range(len(esperando)):#verifica se chegou algum processo no time especificado
        if time == esperando[i].obterTChegada():
            prontos.append(esperando[i])

    if len(prontos) == 0: #se verificou e nao tiver ngm na lista de prontos , passa o tempo, até achar alguém no começo
        time+=1           #serve para o começo quando nao tiver processos que começam no 0
    i=0
    k = 0
    passatempo = 1 #adc +1 no tempo
    while k < len(prontos): #de acordo com o tamanho da lista de prontos
        for j in range(Quantum): #descontar o quantum de 1 por 1
            prontos[i].obterDuracao() - 1
            if prontos[i].obterDuracao() -1 == 0 and prontos[i].obterDuracao() == 0: #em algum caso que só faltar 1 de duração
                passatempo = 1
                break

            else:
                time+=passatempo #passa o tempo

            for i in range(len(esperando)): #verifica se chegou algum processo no tempo atual
                if time == esperando[i].obterTChegada():
                    prontos.append(esperando[i])
            i=0

        if prontos[i].obterDuracao() <= 0: #se a duração do processo for menor ou igual a zero
            finalizados.append(prontos[i])

        else: #colocando o processo atual no fim da fila
            insere=prontos[i]
            prontos.remove(prontos[i])
            prontos.append(insere)
        i=0
        k+=1


