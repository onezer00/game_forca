"""
Este programa foi desenvolvido por Oner
Jogo de forca criado em python
Considere que o programa esta em desenvolvimento
Considere deixar uma estrela no git se esse programa foi útil para você
"""
import unicodedata

import requests


class GameForca:
    """
    Classe GameForca
    """

    def __init__(self):
        self.palavra = None
        self.tamanho = None
        self.acertos = 0
        self.chances = 6

    def get_palavra(self):
        """
        Retorna uma palavra aleatória da API de dicionário
        Atribui a palavra e tamanho ao objeto
        """
        url = 'https://api.dicionario-aberto.net/random'

        response = requests.get(url)

        self.palavra = ''.join(
            ch
            for ch in unicodedata.normalize('NFKD', response.json()['word'])
            if not unicodedata.combining(ch)
        ).upper()
        self.tamanho = len(response.json()['word'])
        return response.json()

    def get_letra(self, letra):
        """
        Verifica se a letra já foi digitada e retorna True ou False
        """
        if len(letra) > 1 and letra not in self.palavra:
            print('Errou ou digitou mais de uma letra!?')
            self.chances -= 1
            return False
        self.acertos += 1
        print('Acertou dessa vez!')
        return True

    def input_letra(self, lista):
        """
        Recupera a letra digitada pelo usuário através do imput
        """
        letra = input('Digite uma letra: ').upper()
        while letra in lista:
            letra = input('Letra já digitada! Digite outra: ').upper()
            if letra not in lista:
                return False
        result = self.get_letra(letra)
        if result:
            return letra

    # pylint: disable=expression-not-assigned
    def start_game(self):
        """
        Inicializa o jogo
        """
        self.get_palavra()
        lista = ['_' for i in range(self.tamanho)]

        print('Iniciando Jogo da Forca')
        print('----------------')
        print(f'Sua palavra tem {self.tamanho} letras\n\n')

        while True:
            print(f'Você tem {self.chances} chances')

            [print(lista[i], end=' ') for i in range(self.tamanho)]
            print('\n')
            if self.chances > 0:
                letra = self.input_letra(lista)
                if letra:
                    for i in range(self.tamanho):
                        if self.palavra[i] == letra:
                            lista[i] = letra
                if '_' not in lista:
                    print('Parabéns, você ganhou!')
                    return False
            else:
                print('\n\nGame Over!')
                return False
