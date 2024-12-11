from pokemon_image.pokemon_images import PIKACHU, CHARMANDER, BULBASAURO 
class Pokedex:
    def get_pokemon():
        return [
            {
                "nome": "Pikachu",
                "tipo": "Elétrico",
                "descricao": "Um Pokémon rato elétrico.",
                "habilidades": ["Choque do Trovão", "Cauda de Ferro"],
                "image": PIKACHU
            },
            {
                "nome": "Charmander",
                "tipo": "Fogo",
                "descricao": "Um pequeno lagarto com chama na cauda.",
                "habilidades": ["Lança-Chamas", "Garra de Dragão"],
                "image": CHARMANDER
            },
            {
                "nome": "Bulbasauro",
                "tipo": "Grama/Veneno",
                "descricao": "Um Pokémon inicial que adora luz solar.",
                "habilidades": ["Folha Navalha", "Chicote de Vinha"],
                "image": BULBASAURO
            }
        ]
