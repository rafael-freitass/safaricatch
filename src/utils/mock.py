#! Apenas testes, apagar tudo depois
def chamar_sim():
    print("vc fechou o jogo")

def chamar_nao():
    print("despausou")

def opcoes_sim_e_nao():
    return {"SIM": chamar_sim(),
            "NAO": chamar_nao()}


def carregar_opcoes_saida(sim, nao):
    return {
        """
|-----------------------------------------------------|
|             Gostaria de sair do jogo?               | 
|                        {}                        |
|                        {}                        |
|(Aviso caso irá perder o progresso e sobre falhar    |
| a captura do pokemon caso esteja em combate agora)  |
|-----------------------------------------------------|             
""".format(sim, nao)
}

def main():
    opcoes = list(opcoes_sim_e_nao().keys())
    sim = opcoes[0]
    nao = opcoes[1]
    print(carregar_opcoes_saida(sim, nao))

if __name__ == '__main__':
    main()