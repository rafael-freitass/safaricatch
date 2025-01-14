import WConio2 as wc
import winsound
import json
import cursor

# Função para carregar o arquivo com os ascii dos pokemons
def carregar_ascii(caminho, nome):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            imagens = conteudo.split("\n[")  # Divide o conteúdo em blocos
            for bloco in imagens:
                if bloco.startswith(nome):  # Procura pelo ID da imagem
                    return bloco.split("]\n", 1)[1].strip()  # Retorna a imagem sem o ID
        return "Imagem não encontrada."
    except FileNotFoundError:
        return "Arquivo de imagens não encontrado."

def carregar_save(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo_save:
            return json.load(arquivo_save)
    except FileNotFoundError:
        return []  # Retorna lista vazia se o arquivo não existir
    except json.JSONDecodeError:
        print("Erro: O arquivo save.json contém erros.")
        return []

# Função para carregar o json com os dados dos pokemons
def carregar_pokedex(caminho_pokedex, caminho_save):
    try:
        with open(caminho_pokedex, 'r', encoding='utf-8') as arquivo:
            pokedex = json.load(arquivo)
    except FileNotFoundError:
        print("Erro: O arquivo pokedex.json não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo pokedex.json contém erros.")
        return []

    capturados = carregar_save(caminho_save)
    nomes_capturados = {pokemon['nome'] for pokemon in capturados}
    
    for pokemon in pokedex:
        pokemon['encontrou'] = pokemon['nome'] in nomes_capturados

    return pokedex

# Função para exibir os pokemons
def mostrar_pokedex(pokedex, selecionado):
    wc.clrscr()  # Limpa o terminal
    wc.textcolor(wc.RED) # Cor texto vermelho
    print(f"{'Pokédex (Use W/S para navegar e Enter para selecionar, Q para sair)'}")

    for i, pokemon in enumerate(pokedex):
        if pokemon['encontrou']:
            if i == selecionado:
                wc.textcolor(wc.BLUE) # Cor texto verde claro
                print(f"> {pokemon['nome']}")
            else:
                wc.textcolor(wc.WHITE)
                print(f"  {pokemon['nome']}")
        else:
            if i == selecionado:
                wc.textcolor(wc.BLUE)  # Cor texto azul
                print(f"> ???")
            else:
                wc.textcolor(wc.WHITE)
                print(f"  ???")

    wc.textcolor(wc.WHITE) # Cor texto padrão

# Função para exibir os detalhes de um Pokémon
def mostrar_detalhes(pokemon):
    if pokemon['encontrou']:
        wc.clrscr()
        imagem_ascii = carregar_ascii('src/saves/poke_image.txt', pokemon['nome'])
        wc.textcolor(wc.RED)
        print(f"{'Detalhes do Pokémon'}")
        wc.textcolor(wc.WHITE)
        print(f"Nome: {pokemon['nome']}")
        print(f"Tipo: {pokemon['tipo']}")
        print(f"Descrição: {pokemon['descricao']}")
        print("Habilidades:")
        wc.textcolor(wc.LIGHTCYAN)
        for habilidade in pokemon['habilidades']:
            print(f"- {habilidade}")
        wc.textcolor(wc.WHITE)
        print("Pressione *Espaço* para ver sua Imagem ou *Enter* para Voltar!")
    else:
        wc.clrscr()
        wc.textcolor(wc.RED)
        print(f"{'Detalhes do Pokémon'}")
        wc.textcolor(wc.WHITE)
        print("Pokemon ainda Não Encontrado!")
        print("\nPressione ENTER para Voltar")

    while True:
        if wc.kbhit():
            _, key = wc.getch()
            if key.lower() == '\r': # se apertar enter sai
                winsound.Beep(700, 100)
                return
            elif key.lower() == ' ': # se apertar espaço mostra o ascii
                try:
                    wc.clrscr()
                    wc.textcolor(wc.RED)
                    print("Imagem do Pokémon")
                    wc.textcolor(wc.WHITE)
                    print(imagem_ascii)
                    print("\nPressione ENTER para voltar...")
                except(UnboundLocalError):
                    print("Você ainda não descobriu esse Pokémon")
                    print("\nPressione ENTER para voltar...")

# Função principal
def main():
    # Pokedex recebe as informaçõe do arquivo json
    
    caminho_pokedex = 'src/saves/pokedex.json'
    caminho_save = 'src/saves/save.json'
    
    pokedex = carregar_pokedex(caminho_pokedex, caminho_save)
    if not pokedex:  # Se a Pokédex estiver vazia, encerra o programa
        print("A Pokédex não pôde ser carregada. Encerrando o programa.")
        return

    selecionado = 0  # Posição inicial da seta
    atualizar = True  # Flag para controle da renderização

    while True:
        cursor.hide()
        if atualizar:
            mostrar_pokedex(pokedex, selecionado)  # Renderiza a Pokédex
            atualizar = False  # Não renderiza novamente até uma ação ocorrer

        # Verifica se uma tecla foi pressionada
        if wc.kbhit():
            _, symbol = wc.getch()  # Captura a tecla pressionada

            if symbol.lower() == 'w':  # Sobe na lista
                winsound.Beep(500, 100)
                selecionado = (selecionado - 1) % len(pokedex)
                atualizar = True  
            elif symbol.lower() == 's':  # Desce na lista
                winsound.Beep(500, 100)
                selecionado = (selecionado + 1) % len(pokedex)
                atualizar = True  
            elif symbol == '\r':  # Enter
                winsound.Beep(900, 100)
                mostrar_detalhes(pokedex[selecionado])  # Exibe os detalhes do Pokémon
                atualizar = True  
            elif symbol.lower() == 'q':  # Sai do programa
                winsound.Beep(700, 100)
                break

# Executa o programa
main()