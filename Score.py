import WConio2

def main():
    score = int(0)
    pokemon = int(0)
    comum = int(0)
    lendario = int(0)
    x = True
    
    WConio2.clrscr()
    WConio2.textcolor(WConio2.YELLOW)
    WConio2.textbackground(WConio2.BLACK)
    
    print("Aperte 'a' pra comum, 's' para lendario, 'p' para parar.")
    print("Score: ", score)
    print("Pokemons capturados: ", pokemon)
    print("Pokemons comuns capturados: ", comum)
    print("Pokemons lendarios capturados: ", lendario)
    
    while x:
        if WConio2.kbhit():
            tecla = WConio2.getkey()
            
            if tecla == 'a':
                comum += 1
                if comum >= 0:
                    score += 100
                    if score >= 0:
                        pokemon += 1
            elif tecla == 's':
                lendario += 1
                if lendario >= 0:
                    score += 500
                    if score >= 0:
                        pokemon += 1
            elif tecla == 'p':
                x = False
            
            WConio2.gotoxy(0, 1)
            print(f"Score: {score:<10}")
            WConio2.gotoxy(0, 2)
            print(f"Pokemons Capturados: {pokemon:<4}")
            WConio2.gotoxy(0, 3)
            print(f"Pokemons Comuns Capturados: {comum:<4}")
            WConio2.gotoxy(0, 4)
            print(f"Pokemons Lendarios Capturados: {lendario:<4}")
        
    WConio2.clrscr()
    print("Saindo...")

if __name__ == "__main__":
    main()