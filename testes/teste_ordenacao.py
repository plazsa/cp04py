# implemente aqui....

import sys
import os

# Adiciona o diretório pai ao sys.path para que seja possível importar o módulo que será testado
# (nesse caso, o módulo busca.py)
# referencia para o código abaixo: https://diveintopython.org/learn/file-handling/directories 
# O `sys.path` é uma lista de diretórios onde o Python procura por módulos
# O `os.path.abspath` retorna o caminho absoluto do arquivo que está sendo executado
# O `os.path.dirname` retorna o diretório onde o arquivo que está sendo executado está localizado
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../") # resolve o problema de import do módulo busca.py

from algoritmos.ordenacao import Ordenacao


class TestOrdenacao:
    def __init__(self):
        self.test_cases = [
            ([3, 7, 33, 59, 71], [3, 7, 33, 59, 71]), # Vetor ordenado crescente
            ([71, 7, 3, 9, 7], [3, 7, 7, 9, 71]), # Vetor não ordenado
            ([71, 59, 33, 7, 3], [3, 7, 33, 59, 71]), # Vetor ordenado descrescente
            ([], []), # Vetor vazio
            ([42], [42]), # Vetor com um único elemento
            ([3, 7, 3, 9, 7], [3, 3, 7, 7, 9]), # Vetor com elementos repetidos
            ([-5, -3, -9, -1], [-9, -5, -3, -1]) # Vetor com elementos negativos
        ]

    def test_ordenacao(self):
        for test_case, expected_result in self.test_cases:
            try:
                assert Ordenacao.ordenar(test_case) == expected_result
                print(f"Teste de ordenação ({test_case}) passou.")
            except AssertionError:
                print(f"Teste de ordenação ({test_case}) falhou.")

    def run_tests(self):
        self.test_ordenacao()
        print("Fim dos testes.")

if __name__ == '__main__':
    testes = TestOrdenacao()
    testes.run_tests()

