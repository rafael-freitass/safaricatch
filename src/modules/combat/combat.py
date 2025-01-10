import WConio2 as wc
import json, winsound, cursor, random, time

def carregar_pokebolas(caminho): # abre o json com info das pokeballs 
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Erro: O arquivo pokeballs.json não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo pokeballs.json contém erros.")
        return []

def carregar_pokemonASCII(caminho, nome): # abre txt com os ascii
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            imagens = conteudo.split("\n[")
            for bloco in imagens:
                if bloco.startswith(nome):  
                    return bloco.split("]\n", 1)[1].strip()
        return "Imagem não encontrada."
    except FileNotFoundError:
        return "Arquivo de imagens não encontrado."

def carregar_pokemons(caminho): # abre o json da pokedex com info dos pokemon
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Erro: O arquivo pokedex.json não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo pokedex.json contém erros.")
        return []

def renderizar_combate(pokemon_nome, pokemon_ascii, pokebolas, selecionado): # tela do combate
    wc.clrscr()
    print(f"Um {pokemon_nome} selvagem apareceu!\n")
    print(pokemon_ascii)
    print("\nO que deseja usar?\n")
    for i, pokebola in enumerate(pokebolas):
        if selecionado == i:
            print(f"> {i+1}. {pokebola['name']}","."*10, f"qtd: {pokebola['quantidade']}")
        else:
            print(f"  {i+1}. {pokebola['name']}","."*10, f"qtd: {pokebola['quantidade']}")
    print("\nPressione 'Q' para sair.")

def barra_precisao(): # barra de captura
    largura = 21  
    posicao = 0  
    direcao = 1  
    ponto_central = largura // 2  
    marcador = "|" 

    wc.clrscr()
    print("Pressione ENTER quando o marcador estiver no centro!")
    time.sleep(1)

    while True:
        wc.gotoxy(0, 2)
    
        barra = ["-"] * largura # cria a barra
        barra[posicao] = marcador # coloca o nosso marcador

        for i in range(largura):
            if i == ponto_central:
                wc.textcolor(wc.RED)  
                wc.putch("*")  # coloca o simbolo do centro na cor vermelha
            else:
                wc.textcolor(wc.WHITE)  
                wc.putch(barra[i])  # o restante será branco
        
        wc.textcolor(wc.WHITE)  

        posicao += direcao # move o marcador
        if posicao == 0 or posicao == largura - 1:  # inverte a direção
            direcao *= -1

        if wc.kbhit():
            _, symbol = wc.getch()
            if symbol == '\r':
                wc.gotoxy(0, 4)
                print(f"Você parou na posição {posicao}!")
                diferenca = abs(posicao - ponto_central)
                return diferenca

        time.sleep(0.1) # controle de velocidade 

def capturar_pokemon(pokemon_dados, pokebola, pokemon_nome):
    pokemon = None
    for i in pokemon_dados:
        if i['nome'].lower() == pokemon_nome.lower():  
            pokemon = i
            break
    if pokemon is None:
        return f"Erro: Pokémon '{pokemon_nome}' não encontrado."
    
    catch_rate = pokemon['catch_rate']
    chance_pokebola = pokebola['chance_captura']

    probabilidade_final = min(100, catch_rate * chance_pokebola)

    diferenca = barra_precisao()

    # ajusta a probabilidade com base na precisão
    if diferenca == 0:
        probabilidade_final += 20
    elif diferenca <= 2:
        probabilidade_final += 10
    elif diferenca <= 5:
        probabilidade_final += 5

    probabilidade_final = min(100, probabilidade_final)

    numero_aleatorio = random.uniform(0, 100)

    if numero_aleatorio <= probabilidade_final:
        deubom=True
        return f"Parabéns! Você capturou o {pokemon_nome}!", deubom
    else:
        deubom=False
        return f"O {pokemon_nome} escapou! Tente novamente.", deubom

def main():
    selecionado = 0
    pokeballs = carregar_pokebolas("src/saves/pokeballs.json")
    pokemon_dados = carregar_pokemons("src/saves/pokedex.json")
    pokemon_selecionado = random.choice(pokemon_dados)
    pokemon_nome = pokemon_selecionado["nome"]
    pokemon_ascii = carregar_pokemonASCII("src/saves/poke_image.txt", pokemon_nome)

    if not pokeballs:
        print("Nenhuma Pokébola carregada.")
        return
    
    atualizar = True
    cursor.hide()

    while True:
        if atualizar == True:
            renderizar_combate(pokemon_nome, pokemon_ascii, pokeballs, selecionado)
            atualizar = False

        if wc.kbhit():
            _, symbol = wc.getch()
            if symbol.lower() == 'w':  # sobe no menu
                winsound.Beep(500, 100)
                selecionado = (selecionado - 1) % len(pokeballs)
                atualizar = True

            elif symbol.lower() == 's':  # desce no menu
                winsound.Beep(500, 100)
                selecionado = (selecionado + 1) % len(pokeballs)
                atualizar = True

            elif symbol == '\r':  # seleciona uma opção
                winsound.Beep(900, 100)
                pokebola_escolhida = pokeballs[selecionado]
                print(f"\nVocê escolheu {pokeballs[selecionado]['name']}!")
                resultado, deubom = capturar_pokemon(pokemon_dados, pokebola_escolhida, pokemon_nome)
                print(resultado)

                if deubom == True:
                    break
                else:
                    input("enter pra continuar")
                    atualizar = True
                    

            elif symbol.lower() == 'q':  # sai do menu
                winsound.Beep(700, 100)
                break

if __name__ == "__main__":
    main()
