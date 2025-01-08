import WConio2

def main():
    score = 0
    pokemon = 0
    comum = 0
    lendario = 0
    
    WConio2.clrscr()
    WConio2.textcolor(WConio2.YELLOW)
    
    print("Aperte 'a' pra comum, 's' para lendario, 'p' para parar.")
    print("Score: ", score)
    print("Pokemons capturados: ", pokemon)
    print("Pokemons comuns capturados: ", comum)
    print("Pokemons lendarios capturados: ", lendario)
    
    while True:
        if WConio2.kbhit():
            tecla = WConio2.getkey()
            
            if tecla == 'a':
                comum += 1
                score += 100
                pokemon += 1
            elif tecla == 's':
                lendario += 1
                score += 500
                pokemon += 1
            elif tecla == 'p':
                break
            
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
