from jogo_forca.forca import GameForca

if __name__ == '__main__':
    game = GameForca()
    game.start_game()
    print(f'Palavra: {game.palavra} - Tamanho: {game.tamanho}')
