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

import random
