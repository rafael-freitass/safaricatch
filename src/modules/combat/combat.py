import WConio2 as wc
import json, winsound, cursor, random, time, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from modules.mapa import mapa

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

def carregar_pokedex(): # abre o json da pokedex com info dos pokemon
    try:
        with open('src/saves/pokedex.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Erro: O arquivo pokedex.json não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo pokedex.json contém erros.")
        return []

def criar_save(nome_pokemon, pokebola, pokemon_pontos):
    caminho_save = "src/saves/save.json"
    dados_novos = {
        "nome":nome_pokemon,
        "pokebola": pokebola['name'],
        "pontos":pokemon_pontos,
        "capturas":1
    }

    try:
        with open(caminho_save, 'r', encoding='utf-8') as arquivo:
            dados_existentes = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        dados_existentes = []

    pokemon_existente = next((pokemon for pokemon in dados_existentes if pokemon['nome'] == nome_pokemon), None)
    if pokemon_existente:
        # Atualiza o contador de pontos
        pokemon_existente['capturas'] += 1
    else:
        # Adiciona um novo Pokémon
        dados_existentes.append(dados_novos)

    with open(caminho_save, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_existentes, arquivo, indent=4, ensure_ascii=False)

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

def barra_precisao(): # barra de captura
    largura = 21  
    posicao = 0  
    direcao = 1  
    ponto_central = (largura // 2) 

    wc.clrscr()
    print("Pressione ENTER quando o marcador estiver no centro!")
    time.sleep(0.5)

    while True:
        wc.gotoxy(0, 2)
    
        barra = ["-"] * largura  # cria a barra
        
        # Substitui o símbolo na posição do marcador com a cor correspondente
        for i in range(largura):
            if i == posicao:
                if i == ponto_central:
                    wc.textcolor(wc.MAGENTA)
                    wc.putch("*")  # Cor roxa no centro
                    time.sleep(0.1)
                else:
                    wc.textcolor(wc.GREEN)  # Cor verde para o marcador
                    wc.putch(barra[i])  # Desenha o marcador na cor correta
            elif i == ponto_central:
                wc.textcolor(wc.RED)  # Cor vermelha para o símbolo do centro
                wc.putch("*")
            else:
                wc.textcolor(wc.WHITE)  # Cor branca para o restante
                wc.putch(barra[i])  # Coloca o restante da barra em branco

        # Move o marcador
        posicao += direcao
        if posicao == 0 or posicao == largura - 1:  # Inverte a direção
            direcao *= -1

        if wc.kbhit():
            _, symbol = wc.getch()
            if symbol == '\r':
                wc.gotoxy(0, 4)
                print(f"Você parou na posição {posicao}!")
                diferenca = abs(posicao - ponto_central)
                return diferenca

        time.sleep(0.1)  # Controle de velocidade

def capturar_pokemon(pokemon_dados, pokebola, pokemon_nome, pokemon_pontos):
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
        criar_save(pokemon_nome, pokebola, pokemon_pontos)
        return f"Parabéns! Você capturou o {pokemon_nome}!", deubom
    else:
        deubom=False
        return f"O {pokemon_nome} escapou! Tente novamente.", deubom

def main(pokeballs: list):
    selecionado = 0
    pokemon_dados = carregar_pokedex()
    pokemon_selecionado = random.choice(pokemon_dados)
    pokemon_nome = pokemon_selecionado["nome"]
    pokemon_pontos = pokemon_selecionado["pontos"]
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
                for pokeball in pokeballs:
                    possui_pokebola = True
                    pass

                pokebola_escolhida = pokeballs[selecionado]
                if pokeballs[selecionado]['quantidade'] <= 0:
                    print(f"\nSuas pokebolas do tipo {pokeballs[selecionado]['name']} acabaram! Escolha outra opção")
                    input("\nPressione ENTER para continuar...")
                    atualizar = True
                    continue

                pokeballs[selecionado]['quantidade'] -= 1

                print(f"\nVocê escolheu {pokeballs[selecionado]['name']}!")
                resultado, deubom = capturar_pokemon(pokemon_dados, pokebola_escolhida, pokemon_nome, pokemon_pontos)
                print(resultado)
                if deubom == True:
                    print("\nPressione ENTER pra continuar...")
                    while True:
                        cursor.hide()
                        if wc.kbhit():
                            _, symbol = wc.getch() 
                            if symbol == '\r':
                                winsound.Beep(900, 100)
                                atualizar = True  
                                break
                    wc.clrscr()
                    break
                else:
                    print("\nPressione ENTER pra continuar...")
                    while True:
                        cursor.hide()
                        if wc.kbhit():
                            _, symbol = wc.getch() 
                            if symbol == '\r':
                                winsound.Beep(900, 100)
                                atualizar = True  
                                break
                    wc.clrscr()
                    atualizar = True
                    

if __name__ == "__main__":
    main()
