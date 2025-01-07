from multiprocessing import Process
from time import sleep
from math import floor
#import WConio2 as wc
#TODO Eu não precisei usar o WConio2, mas ele simplesmente não funcionava o import e ainda não sei o que tem de errado, help

#! Função para traduzir minutos para segundos
def segundo_Para_Minuto(tempo): # Tem como parâmetro o tempo a ser traduzido
    minuto = floor(tempo / 60) # Precisei sempre arrendondar o número para baixo, e era só feito com esse import de math
    segundo = str(tempo % 60) # Os segundos são apenas o resto de dividir o tempo por 60
    minuto = str(minuto) # Necessário traduzir para string, já que não era possível antes, para a formatação do retorno
    if tempo > 59:
        return minuto + "m : " + segundo + "s" #! 00m : 00s ; retorna essa formatação (é uma string) se tiverem minutos
    else:
        return segundo + "s" #! Retorna 00s (é uma string) se não houverem minutos, posso modificar para os minutos ficarem sempre aparecendo, se necessário

#! Esse é o timer em si, o código de como ele funciona
def timer(tempo_Segundos): 
    contador = tempo_Segundos # Não sabia se era uma boa ideia modificar um parâmetro diretamente
    if contador >= 0: # O timer vai do tempo enviado até zero (quando acaba o jogo)
        sleep(1) # Ele usa esse método do import time para aguardar um segundo
#        print(segundo_Para_Minuto(contador)) #########!Essa linha é para teste, não é necessária o print, apenas a chamada da função, caso queira testar o timer, modifique o valor de segundos abaixo e retire o "#" do começo da linha
        contador -= 1 # Já que se passaram um segundo, ele reduz em um o contador, pois também é uma função recursiva
        timer(contador) # Chama a si mesma, dando o contador como parâmetro, agora que penso, ainda estou tentando lembrar por que não usei um for loop in range, tinha um motivo bom, juro
    else:
        return False # Quando o tempo chega a zero, o timer acaba

#! Função main, cuidado
def main():
    tempo_Segundos = 60 # O tempo do timer, pode ser modificado, isso é só um exemplo, ele funciona com qualquer tempo
    processo_Timer = Process(target=timer, args=(tempo_Segundos,)) # Explico pessoalmente, ou em reunião como funciona, mas basicamente:
    # Utiliza um dos cores do PC para rodar o timer ao mesmo tempo do jogo, para um não afetar o outro ou tudo ficar no mesmo update loop, mas teria como fazer assim também, se quiser, até onde eu sei, dessa maneira deve ser mais eficiente e tecnicamente correto
    processo_Timer.start() # Começa o processo, ou seja o timer


if __name__ == "__main__": # Necessário para o Processing ocorrer em Windows, até hoje não sei porque kkkkkkkk
    main()
