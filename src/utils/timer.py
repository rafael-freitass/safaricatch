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
        print(segundo_Para_Minuto(num.value)) ####!Essa linha é para teste, não é necessária o print, apenas a chamada da função, caso queira testar o timer, modifique o valor de segundos abaixo e retire o "#" do começo da linha
        num.value -= 1
    if num.value <= 1:
        t_Sleep(1)
        terminar_Timer()

def get_NumValue():
    return num.value

#! Função main, cuidado
def timer_Main():
    processo_Timer.start()


def terminar_Timer():
    num.value = 0
    winsound.Beep(700, 800)
    return False

#! Globais
num = Value('i', 180) #! Três minutos
processo_Timer = Process(target=timer, args=(num,))

if __name__ == "__main__": # Necessário para o Processing ocorrer em Windows
    timer_Main()