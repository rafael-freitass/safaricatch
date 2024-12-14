import WConio2 as wc
import winsound
import json
import cursor

# Função para carregar o arquivo com os ascii dos pokemons
def carregar_ascii(caminho, imagem_id):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            imagens = conteudo.split("\n[")  # Divide o conteúdo em blocos
            for bloco in imagens:
                if bloco.startswith(imagem_id):  # Procura pelo ID da imagem
                    return bloco.split("]\n", 1)[1].strip()  # Retorna a imagem sem o ID
        return "Imagem não encontrada."
    except FileNotFoundError:
        return "Arquivo de imagens não encontrado."

# Função para carregar o json com os dados dos pokemons
def carregar_pokedex(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Erro: O arquivo pokedex.json não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo pokedex.json contém erros.")
        return []

# Função para exibir os pokemons
def mostrar_pokedex(pokedex, selecionado):
    wc.clrscr()  # Limpa o terminal
    wc.textcolor(wc.RED) # Cor texto vermelho
    print(f"{'Pokédex (Use W/S para navegar e Enter para selecionar, Q para sair)'}")

    for i, pokemon in enumerate(pokedex):
        if i == selecionado:
            wc.textcolor(wc.BLUE) # Cor texto verde claro
            print(f"> {pokemon['nome']}")
        else:
            wc.textcolor(wc.WHITE)
            print(f"  {pokemon['nome']}")
    wc.textcolor(wc.WHITE) # Cor texto padrão

# Função para exibir os detalhes de um Pokémon
def mostrar_detalhes(pokemon):
    wc.clrscr()
    imagem_ascii = carregar_ascii('src/saves/poke_image.txt', pokemon['imagem_id'])
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

    while True:
        if wc.kbhit():
            _, key = wc.getch()
            if key.lower() == '\r': # se apertar enter sai
                winsound.Beep(700, 100)
                return
            elif key.lower() == ' ': # se apertar espaço mostra o ascii
                wc.clrscr()
                print("\nImagem do Pokémon:")
                print(imagem_ascii)
                print("\nPressione Enter para voltar...")

# Função principal
def main():
    # Pokedex recebe as informaçõe do arquivo json
    pokedex = carregar_pokedex('src/saves/pokedex.json')
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