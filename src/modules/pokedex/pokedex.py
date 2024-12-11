import WConio2 as wc
import os
import json
import cursor

# Função para exibir a Pokédex com a seta de seleção
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

# Função para exibir a Pokédex com a seta de seleção e bordas
def mostrar_pokedex(pokedex, selecionado):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal
    largura = 50  # Largura da borda
    print('*' * largura)
    print(f"*{'Pokédex (Use W/S para navegar e Enter para selecionar, Q para sair)':^{largura-2}}*")
    print('*' * largura)

    for i, pokemon in enumerate(pokedex):
        if i == selecionado:
            linha = f"> {pokemon['nome']}"
        else:
            linha = f"  {pokemon['nome']}"
        print(f"* {linha:<{largura-4}} *")  # Alinha os textos à esquerda dentro da borda

    print('*' * largura)  # Linha de fechamento da borda

# Função para exibir os detalhes de um Pokémon com bordas
def mostrar_detalhes(pokemon):
    os.system('cls' if os.name == 'nt' else 'clear')
    largura = 50  # Largura da borda
    print('*' * largura)
    print(f"*{'Detalhes do Pokémon':^{largura-2}}*")
    print('*' * largura)
    print(f"* Nome: {pokemon['nome']:<{largura-10}}*")
    print(f"* Tipo: {pokemon['tipo']:<{largura-10}}*")
    print(f"* Descrição: {pokemon['descricao']:<{largura-13}}*")
    print("* Habilidades:")
    for habilidade in pokemon['habilidades']:
        print(f"* - {habilidade:<{largura-6}}*")
    print('*' * largura)
    print("\nPressione Enter para voltar...")
    while True:
        if wc.kbhit():
            _, key = wc.getch()
            if key.lower() == '\r':
                return

# Função principal
def main():
    # Carrega a Pokédex do arquivo JSON
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
                selecionado = (selecionado - 1) % len(pokedex)
                atualizar = True  # Define para atualizar a tela
            elif symbol.lower() == 's':  # Desce na lista
                selecionado = (selecionado + 1) % len(pokedex)
                atualizar = True  # Define para atualizar a tela
            elif symbol == '\r':  # Enter
                mostrar_detalhes(pokedex[selecionado])  # Exibe os detalhes do Pokémon
                atualizar = True  # Atualiza a tela ao voltar
            elif symbol.lower() == 'q':  # Sai do programa
                break

# Executa o programa
main()