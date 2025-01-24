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
            wc.clrscr()
            instrucoes.main()
        elif opcao == "jogar":
            mapa.rodar()
        elif opcao == "score":
            pokedex.main()
            
    return funcao

def carregar_opcoes():
    return {
        """ 
┏┳┏┓┏┓┏┓┳┓
 ┃┃┃┃┓┣┫┣┫
┗┛┗┛┗┛┛┗┛┗
              
""": teste('jogar'),
        """
┏┓┏┓┳┓┏┳┓┳┓┏┓┓ ┏┓┏┓
┃ ┃┃┃┃ ┃ ┣┫┃┃┃ ┣ ┗┓
┗┛┗┛┛┗ ┻ ┛┗┗┛┗┛┗┛┗┛

 """: teste('instrucoes'),
"""
┏┓┏┓┓┏┓┏┓┳┳┓┏┓┳┓┏┓
┃┃┃┃┃┫ ┣ ┃┃┃┃┃┃┃┗┓
┣┛┗┛┛┗┛┗┛┛ ┗┗┛┛┗┗┛
""": teste('score'),
    }

def mostrar_menu(selecionado, opcoes):
    wc.clrscr()
    wc.textcolor(wc.YELLOW)
    print("""
    ___   _   ____  _   ___   __  __   _  _____  __  _ __
  ,' _/ .' \ / __/.' \ / o | / /,'_/ .' \/_  _/,'_/ /// /
 _\ `. / o // _/ / o //  ,' / // /_ / o / / / / /_ / ` / 
/___,'/_n_//_/  /_n_//_/`_\/_/ |__//_n_/ /_/  |__//_n_/  
                                                         
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
main()
