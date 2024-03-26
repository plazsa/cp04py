# implemente aqui....

class Ordenacao:

    def bubble_def (lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j] ## troca de posição
        return lista
    
    def selection_sort(lista):
        n = len(lista)
        # Percorre a lista.
        for i in range(n):
            # Encontra o elemento mínimo da lista.
            minimo = i
            for j in range(i + 1, n):
                if lista[minimo] > lista[j]:
                    minimo = j
            # Coloca o elemento mínimo na posição correta.
            lista[i], lista[minimo] = lista[minimo], lista[i] ## troca de posição

    def insertion_sort(lista):
        n = len(lista)
        # Percorre a lista.
        for j in range(1, n):
            chave = lista[j]
            i = j - 1
            # Insere o elemento lista[j] na posição correta.
            while i >= 0 and lista[i] > chave:
                lista[i + 1] = lista[i]
                i = i - 1
            lista[i + 1] = chave

        return lista
    
    def mergeSort(alist):
        mergesort(alist, [0] * len(alist), 0, len(alist) - 1)


    def merge(A, aux, esquerda, meio, direita):
        """
        Combina dois vetores ordenados em um único vetor (também ordenado).
        """
        for k in range(esquerda, direita + 1):
            aux[k] = A[k]
        i = esquerda
        j = meio + 1
        for k in range(esquerda, direita + 1):
            if i > meio:
                A[k] = aux[j]
                j += 1
            elif j > direita:
                A[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                A[k] = aux[j]
                j += 1
            else:
                A[k] = aux[i]
                i += 1


    def mergesort(A, aux, esquerda, direita):
        if direita <= esquerda:
            return
        meio = (esquerda + direita) // 2

        # Ordena a primeira metade do arranjo.
        mergesort(A, aux, esquerda, meio)

        # Ordena a segunda metade do arranjo.
        mergesort(A, aux, meio + 1, direita)

        # Combina as duas metades ordenadas anteriormente.
        merge(A, aux, esquerda, meio, direita)
