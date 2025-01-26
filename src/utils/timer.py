from multiprocessing import Process, Value
from time import sleep as t_Sleep
from math import floor
import winsound

#! Função para traduzir minutos para segundos
def segundo_Para_Minuto(tempo): # Tem como parâmetro o tempo a ser traduzido
    minuto = floor(tempo / 60)
    if (tempo % 60) > 9:
        segundo = str(tempo % 60)
    elif (tempo % 60) <= 9:
        segundo = "0" + str(tempo % 60)
    if (tempo / 60) > 9:
        minuto = floor(tempo / 60)
        minuto = str(minuto)
    elif (tempo / 60) <= 9:
        minuto = floor(tempo / 60)
        minuto = "0" + str(minuto)
    if tempo > 59:
        return minuto + ":" + segundo #! 00:00
    else:
        return "00:" + segundo #! 00:00

#! Esse é o timer
def timer(num):
    num.value = 90 #! Um minuto e meio
    while True:
        if num.value == -100:
            return
        while num.value >= 1:
            t_Sleep(1)
            num.value -= 1
        while num.value <= -2 and num.value != -100:
            t_Sleep(1)
        if num.value <= 1 and num.value >= -1:
            terminar_Timer()
            set_NumValue(-3)


def matar_Timer(): # Faz com que o timer entre n condicional que o termina, 
    #!NÃO utilizar, exceto extremamente necessário (fechar o jogo por completo, num try except...)
    set_NumValue(-100)

def get_NumValue(): # Retorna o valor do tempo atual
    return num.value

def set_NumValue(n): # Modifica o valor do tempo do timer ao tempo inserido como parâmetro
    num.value = n

#! Função main, cuidado
def timer_Main():
    global processo_Timer
    if not processo_Timer.is_alive():  # Verifica se o processo está em execução
        processo_Timer = Process(target=timer, args=(num,))
        processo_Timer.start() # Apenas inicia o timer

def pause_Timer():
    global valor_Pausado
    valor_Pausado = num.value # Guarda o valor do tempo atual
    guardar_valor_Pausado = valor_Pausado
    num.value = -3 # Modifica o valor do timer para entrar em um loop de espera

def despause_Timer():
    global valor_Pausado
    num.value = valor_Pausado # Modifica o valor do timer para o valor que tinha parado anteriormente

def terminar_Timer():
    num.value = 0 # Modifica o valor do timer para 0
    winsound.Beep(250, 1000) #TODO Lembrar de modificar o som de terminar o timer aqui (retire o import do winsound se não for usar)
    return False


#! Globais
num = Value('i', 90) #! Um minuto e meio
processo_Timer = Process(target=timer, args=(num,))
valor_Pausado = 0

if __name__ == "__main__": # Necessário para o Processing ocorrer em Windows
    timer_Main()
