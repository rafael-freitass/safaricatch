import WConio2 as wc
import json, winsound, cursor, random, time, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from modules.score import score
from modules.mapa import mapa
from modules.mapa import map_functions
from modules.jogador import movimento
from utils.timer import *
from utils.text_functions import *
from saves import gamestate

def set_encontros(num):
    gamestate._nencontros_ += num
    return gamestate._nencontros_

def get_encontros():
    return gamestate._nencontros_

def set_ncapturas(num):
    gamestate._ncapturas_ += num 
    return gamestate._ncapturas_

def get_ncapturas():
    return gamestate._ncapturas_

def set_descobertas(num):
    gamestate._ndescobertas_ += num
    return gamestate._ndescobertas_

def get_descobertas():
    return gamestate._ndescobertas_


def carregar_pokebolas(caminho): # abre o json com info das pokeball_list 
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

def criar_save(nome_pokemon, pokebola, pokemon_pontos): # cria json do save
    global _ndescobertas_
    num = 1

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
        set_descobertas(num)

    with open(caminho_save, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_existentes, arquivo, indent=4, ensure_ascii=False)

def renderizar_combate(pokemon_nome, pokemon_ascii, pokebolas, selecionado,cor,tempo_atual): # tela do combate
    wc.clrscr()
    print(f"Um {pokemon_nome} selvagem apareceu!\n")
    wc.textcolor(getattr(wc, cor))
    print(pokemon_ascii)
    wc.textcolor(wc.WHITE)
    print("\nO que deseja usar?\n")
    for i, pokebola in enumerate(pokebolas):
        if selecionado == i:
            print(f"> {i+1}. {pokebola['name']}","."*10, f"qtd: {pokebola['quantidade']}")
        else:
            print(f"  {i+1}. {pokebola['name']}","."*10, f"qtd: {pokebola['quantidade']}")
    print(tempo_atual)

def animacao_espiral(matriz, borda = 2): # animação quando acha o pokemon
    maxI = len(matriz)
    maxJ = len(matriz[0])

    topo, base = 0, maxI - 1
    esquerda, direita = 0, maxJ - 1

    while topo <= base and esquerda <= direita:
        # Apagar a linha superior
        for col in range(esquerda, direita + 1):
            wc.gotoxy(col+borda, topo+ borda)
            print(" ", end="", flush=True)
        topo += 1

        # Apagar a coluna direita
        for linha in range(topo, base + 1):
            wc.gotoxy(direita + borda, linha+ borda)
            print(" ", end="", flush=True)
        direita -= 1

        # Apagar a linha inferior
        if topo <= base:
            for col in range(direita, esquerda - 1, -1):
                wc.gotoxy(col+ borda, base+borda)
                print(" ", end="", flush=True)
            base -= 1

        # Apagar a coluna esquerda
        if esquerda <= direita:
            for linha in range(base, topo - 1, -1):
                wc.gotoxy(esquerda + borda, linha + borda)
                print(" ", end="", flush=True)
            esquerda += 1

        time.sleep(0.09)

    wc.clrscr()

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

def calcular_probabilidade(catch_rate, chance_pokebola, diferenca_precisao):
    PRECISION_BONUS = {0: 20, 2: 10, 5: 5}  # Bônus baseados na precisão
    probabilidade = min(100, catch_rate * chance_pokebola)
    bonus = next((b for p, b in PRECISION_BONUS.items() if diferenca_precisao <= p), 0)
    probabilidade += bonus
    return min(100, probabilidade)

def capturar_pokemon(pokemon_dados, pokebola, pokemon_nome, pokemon_pontos): # calculo de captura de pokemon
    pokemon = None
    for i in pokemon_dados:
        if i['nome'].lower() == pokemon_nome.lower():  
            pokemon = i
            break
    if pokemon is None:
        return f"Erro: Pokémon '{pokemon_nome}' não encontrado."
    
    catch_rate = pokemon['catch_rate']
    chance_pokebola = pokebola['chance_captura']

    diferenca = barra_precisao()
    probabilidade_final = calcular_probabilidade(catch_rate, chance_pokebola, diferenca)

    if random.uniform(0, 100) <= probabilidade_final:
        criar_save(pokemon_nome, pokebola, pokemon_pontos)
        return f"Parabéns! Você capturou o {pokemon_nome}!", True, False

    if tentar_fuga(catch_rate):        
        return f"O {pokemon_nome} fugiu!", False, True

    return f"O {pokemon_nome} escapou da captura! Tente novamente.", False, False

def tentar_fuga(catch_rate):
    fuga_chance = 100 - catch_rate
    return random.uniform(0, 100) <= fuga_chance

def aguardar_acao():
    print("\nPressione ENTER para continuar...")
    while True:
        cursor.hide()
        if wc.kbhit():
            _, symbol = wc.getch()
            if symbol == '\r':
                winsound.Beep(900, 100)
                break

def redesenhar_mapa(mapa_game, pos_mapa_atual, portais):
    wc.clrscr()
    att_container(mapa_game, 0, pos_mapa_atual[0])
    mapa.impressao_matriz_m(mapa_game, True, 2)
    movimento.movimentar_jogador(mapa_game[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, 0, 0, portais, 2, mapa_game)

pokeball_list = carregar_pokebolas("src/saves/pokeballs.json")

def main():
    
def main(pokeballs: list, pos_mapa_atual):
    global _nencontros_, _ncapturas_

    num = 1
    set_encontros(num)
    selecionado = 0
    pokemon_dados = carregar_pokedex()
    pokemon_selecionado = random.choice(pokemon_dados)
    pokemon_nome = pokemon_selecionado["nome"]
    pokemon_pontos = pokemon_selecionado["pontos"]
    cor = pokemon_selecionado["cor"]
    pokemon_ascii = carregar_pokemonASCII("src/saves/poke_image.txt", pokemon_nome)
    
    mapa.alinhar_add_margem_tela(2)
    mapa_game = map_functions.carregar_mapa("mapa.txt")
    mapa.alinhar_add_margem_tela(0)

    if not pokeball_list:
        print("Nenhuma Pokébola carregada.")
        return
    
    atualizar = True
    cursor.hide()

    despause_Timer()

    while True:
        tempo = get_NumValue()
        tempo_atual = segundo_Para_Minuto(tempo)

        if atualizar == True:
            renderizar_combate(pokemon_nome, pokemon_ascii, pokeball_list, selecionado, cor, tempo_atual)
            atualizar = False

        if wc.kbhit():
            _, symbol = wc.getch()
            if symbol.lower() == 'w':  # sobe no menu
                winsound.Beep(500, 100)
                selecionado = (selecionado - 1) % len(pokeball_list)
                atualizar = True

            elif symbol.lower() == 's':  # desce no menu
                winsound.Beep(500, 100)
                selecionado = (selecionado + 1) % len(pokeball_list)
                atualizar = True

            elif symbol == '\r':  # seleciona uma opção
                winsound.Beep(900, 100)

                pokebola_escolhida = pokeball_list[selecionado]
                if pokeball_list[selecionado]['quantidade'] <= 0:
                    print(f"\nSuas pokebolas do tipo {pokeball_list[selecionado]['name']} acabaram! Escolha outra opção")
                    aguardar_acao()
                    wc.clrscr()
                    atualizar = True
                    continue

                pokeball_list[selecionado]['quantidade'] -= 1

                print(f"\nVocê escolheu {pokeball_list[selecionado]['name']}!")
                time.sleep(1)
                resultado, deubom, fugiu = capturar_pokemon(pokemon_dados, pokebola_escolhida, pokemon_nome, pokemon_pontos)
                print(resultado)

                if deubom:
                    score.aumentar_score(pokemon_pontos)
                    print(f"Você ganhou {pokemon_pontos} pontos!")
                    aguardar_acao()
                    wc.clrscr()

                    set_ncapturas(num)
                    portais = map_functions.encontrar_coord_portais(mapa_game)
                    redesenhar_mapa(mapa_game, pos_mapa_atual, portais)


                    break
                else:
                    if fugiu:
                        aguardar_acao()
                        wc.clrscr()
                        
                        pos_mapa_atual = map_functions.encontrar_mapa_atual(mapa_game)
                        portais = map_functions.encontrar_coord_portais(mapa_game)
                        redesenhar_mapa(mapa_game, pos_mapa_atual, portais)
                        break
                    else:
                        aguardar_acao()
                        wc.clrscr()
                        atualizar = True

if __name__ == "__main__":
    main()