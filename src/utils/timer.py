from multiprocessing import Process, Value
from time import sleep as t_Sleep
from math import floor
import winsound

#! Função para traduzir minutos para segundos
def segundo_Para_Minuto(tempo): # Tem como parâmetro o tempo a ser traduzido
    minuto = floor(tempo / 60)
    segundo = str(tempo % 60)
    minuto = str(minuto)
    if tempo > 59:
        return minuto + "m : " + segundo + "s" #! 00m : 00s
    else:
        return segundo + "s" #! 00s


#! Esse é o timer
def timer(num):
    num.value = 180 #! Três minutos
    while num.value >= 1:
        t_Sleep(1)
        num.value -= 1
        while num.value <= -2:
            t_Sleep(1)
    if num.value <= 1 and num.value >= -1:
        t_Sleep(1)
        terminar_Timer()

def get_NumValue():
    return num.value

#! Função main, cuidado
def timer_Main():
    processo_Timer.start() # Apenas inicia o timer

def pause_Timer():
    global valor_Pausado
    valor_Pausado = num.value # Guarda o valor do tempo atual
    num.value = -3 # Modifica o valor do timer para entrar em um loop de espera

def despause_Timer():
    global valor_Pausado
    num.value = valor_Pausado # Modifica o valor do timer para o valor que tinha parado anteriormente

def terminar_Timer():
    num.value = 0 # Modifica o valor do timer para 0
    winsound.Beep(250, 1000) #TODO Lembrar de modificar o som de terminar o timer aqui (retire o import do winsound se não for usar)
    return False

#! Globais
num = Value('i', 180) #! Três minutos
processo_Timer = Process(target=timer, args=(num,))
valor_Pausado = 0

if __name__ == "__main__": # Necessário para o Processing ocorrer em Windows
    timer_Main()