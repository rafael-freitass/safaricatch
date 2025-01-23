import WConio2 as wc
import winsound
import sys
import os
import cursor


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from modules.instrucoes import instrucoes
from modules.mapa import mapa
from modules.pokedex import pokedex

def teste(opcao):
    def funcao():
        if opcao == "instrucoes":
            instrucoes.main()
        elif opcao == "jogar":
            mapa.main()
        elif opcao == "score":
            pokedex.main()
            
    return funcao

def carregar_opcoes():
    return {
        """
     .-./`)     ,-----.      .-_'''-.      ____   .-------.     
     \ '_ .') .'  .-,  '.   '_( )_   \   .'  __ `.|  _ _   \    
    (_ (_) _)/ ,-.|  \ _ \ |(_ o _)|  ' /   '  \  \ ( ' )  |    
      / .  \;  \  '_ /  | :. (_,_)/___| |___|  /  |(_ o _) /    
 ___  |-'`| |  _`,/ \ _/  ||  |  .-----.   _.-`   | (_,_).' __  
|   | |   ' : (  '\_/ \   ;'  \  '-   .'.'   _    |  |\ \  |  | 
|   `-'  /   \ `"/  \  ) /  \  `-'`   | |  _( )_  |  | \ `'   / 
 \      /     '. \_/``".'    \        / \ (_ o _) /  |  \    /  
  `-..-'        '-----'       `'-...-'   '.(_,_).'''-'   `'-'
""": teste('jogar'),
        """
.-./`) ,---.   .--.   .-'''-.,---------. .-------.      ___    _     _______      ,-----.        .-''-.    .-'''-.  
\ .-.')|    \  |  |  / _     \          \|  _ _   \   .'   |  | |   /   __  \   .'  .-,  '.    .'_ _   \  / _     \ 
/ `-' \|  ,  \ |  | (`' )/`--'`--.  ,---'| ( ' )  |   |   .'  | |  | ,_/  \__) / ,-.|  \ _ \  / ( ` )   '(`' )/`--' 
 `-'`"`|  |\_ \|  |(_ o _).      |   \   |(_ o _) /   .'  '_  | |,-./  )      ;  \  '_ /  | :. (_ o _)  (_ o _).    
 .---. |  _( )_\  | (_,_). '.    :_ _:   | (_,_).' __ '   ( \.-.|\  '_ '`)    |  _`,/ \ _/  ||  (_,_)___|(_,_). '.  
 |   | | (_ o _)  |.---.  \  :   (_I_)   |  |\ \  |  |' (`. _` /| > (_)  )  __: (  '\_/ \   ;'  \   .---.---.  \  : 
 |   | |  (_,_)\  |\    `-'  |  (_(=)_)  |  | \ `'   /| (_ (_) _)(  .  .-'_/  )\ `"/  \  ) /  \  `-'    |    `-'  | 
 |   | |  |    |  | \       /    (_I_)   |  |  \    /  \ /  . \ / `-'`-'     /  '. \_/``".'    \       / \       /  
 '---' '--'    '--'  `-...-'     '---'   ''-'   `'-'    ``-'`-''    `._____.'     '-----'       `'-..-'   `-...-'
 """: teste('instrucoes'),
"""
   .-'''-.    _______      ,-----.    .-------.        .-''-.   
  / _     \  /   __  \   .'  .-,  '.  |  _ _   \     .'_ _   \  
 (`' )/`--' | ,_/  \__) / ,-.|  \ _ \ | ( ' )  |    / ( ` )   ' 
(_ o _).  ,-./  )      ;  \  '_ /  | :|(_ o _) /   . (_ o _)  | 
 (_,_). '.\  '_ '`)    |  _`,/ \ _/  || (_,_).' __ |  (_,_)___| 
.---.  \  :> (_)  )  __: (  '\_/ \   ;|  |\ \  |  |'  \   .---. 
\    `-'  (  .  .-'_/  )\ `"/  \  ) / |  | \ `'   / \  `-'    / 
 \       / `-'`-'     /  '. \_/``".'  |  |  \    /   \       /  
  `-...-'    `._____.'     '-----'    ''-'   `'-'     `'-..-'   
""": teste('score'),
    }

def mostrar_menu(selecionado, opcoes):
    wc.clrscr()
    wc.textcolor(wc.YELLOW)
    print("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌
▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀      ▐░▌     ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌
          ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌      ▐░▌  ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀            ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
""")
    print("-"*142)
    wc.textcolor(wc.WHITE)
    lista_opcoes = list(opcoes.keys())

    for i, opcao in enumerate(lista_opcoes):
        if i == selecionado:
            wc.textcolor(wc.BROWN)
            print(f"""{opcao.capitalize()}""")
        else:
            wc.textcolor(wc.WHITE)
            print(f"  {opcao.capitalize()}")

    wc.textcolor(wc.WHITE)
    print("Use W/S para navegar - Enter para selecionar - Q para sair")

# Função principal
def main():
    opcoes = carregar_opcoes()
    selecionado = 0
    atualizar = True 

    while True:
        cursor.hide()
        if atualizar:
            mostrar_menu(selecionado, opcoes)
            atualizar = False

        if wc.kbhit():
            _, symbol = wc.getch()

            if symbol.lower() == 'w':
                winsound.Beep(500, 100)
                selecionado = (selecionado - 1) % len(opcoes)
                atualizar = True
            elif symbol.lower() == 's':
                winsound.Beep(500, 100)
                selecionado = (selecionado + 1) % len(opcoes)
                atualizar = True
            elif symbol == '\r':
                winsound.Beep(900, 100)
                lista_opcoes = list(opcoes.keys())
                opcoes[lista_opcoes[selecionado]]()
                atualizar = True
            elif symbol.lower() == 'q':
                winsound.Beep(700, 100)
                break

if __name__ == "__main__":
    main()
