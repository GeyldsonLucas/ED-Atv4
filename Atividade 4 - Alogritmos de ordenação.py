import time
import os

# Função para ler um arquivo de texto e retornar um array de linhas
def ler_arquivo_para_array(nome_arquivo):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    arquivo_path = os.path.join(script_dir, nome_arquivo)
    try:
        with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            return linhas
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

# MergeSort in Python
def mergeSort(array):
    if len(array) > 1:
        

        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

        
        

# Bubble sort in Python
def bubbleSort(array):
    start_time = time.time()

    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    end_time = time.time()
    tempo_execucao = end_time - start_time
    print("BubbleSort: Tempo de execução =", tempo_execucao, "segundos")

# Insertion sort in Python
def insertionSort(array):
    start_time = time.time()

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

    end_time = time.time()
    tempo_execucao = end_time - start_time
    print("InsertionSort: Tempo de execução =", tempo_execucao, "segundos")

# Selection sort in Python
def selectionSort(array, size):
    start_time = time.time()

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])

    end_time = time.time()
    tempo_execucao = end_time - start_time
    print("SelectionSort: Tempo de execução =", tempo_execucao, "segundos")

# Shell sort in python
def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


# Heap Sort


def heapify(arr, n, i):
      # Find largest among root and children
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      # If root is not largest, swap with largest and continue heapifying
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
  
def heapSort(arr):
      n = len(arr)
  
      # Build max heap
      for i in range(n//2, -1, -1):
          heapify(arr, n, i)
  
      for i in range(n-1, 0, -1):
          # Swap
          arr[i], arr[0] = arr[0], arr[i]
  
          # Heapify root element
          heapify(arr, i, 0)
  
# Quick sort 

# function to find the partition position
def partition(array, low, high):
    pivot_index = (low + high) // 2
    pivot = array[pivot_index]

    # swap pivot to the end
    array[pivot_index], array[high] = array[high], array[pivot_index]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)



def menu_algoritmo(array):
    while True:
        opcao = int(input("\nEscolha um algoritmo de ordenação:\n"
                          "1. MergeSort\n"
                          "2. BubbleSort\n"
                          "3. InsertionSort\n"
                          "4. SelectionSort\n"
                          "5. QuickSort\n"
                          "6. ShellSort\n"
                          "7. HeapSort\n"
                          "8. Voltar para o menu anterior\n"))

        if opcao == 1:
            start_time = time.time()
            mergeSort(array)
            end_time = time.time()
            tempo_execucao = end_time - start_time
            print("MergeSort: Tempo de execução =", tempo_execucao, "segundos")
        elif opcao == 2:
            bubbleSort(array)
        elif opcao == 3:
            insertionSort(array)
        elif opcao == 4:
            selectionSort(array, len(array))
        elif opcao == 5:
            start_time = time.time()
            quickSort(array, 0, len(array) - 1)
            end_time = time.time()
            tempo_execucao = end_time - start_time
            print("QuickSort: Tempo de execução =", tempo_execucao, "segundos")
        elif opcao == 6:
            start_time = time.time()
            shellSort(array, len(array))
            end_time = time.time()
            tempo_execucao = end_time - start_time
            print("ShellSort: Tempo de execução =", tempo_execucao, "segundos")
        elif opcao == 7:
            start_time = time.time()
            heapSort(array)
            end_time = time.time()
            tempo_execucao = end_time - start_time
            print("HeapSort: Tempo de execução =", tempo_execucao, "segundos")
        elif opcao == 8:
            break
        else:
            print("Opção inválida.")

def menu_arquivo():
    while True:
        print("\nEscolha um arquivo de nomes:\n"
              "1. nomes100k.txt\n"
              "2. nomes250k.txt\n"
              "3. nomes500k.txt\n"
              "4. Sair\n")

        escolha_arquivo = input("Digite o número correspondente à sua escolha: ")

        if escolha_arquivo == '1':
            nome_arquivo = "data/nomes100k.txt"
            break
        elif escolha_arquivo == '2':
            nome_arquivo = "data/nomes250k.txt"
            break
        elif escolha_arquivo == '3':
            nome_arquivo = "data/nomes500k.txt"
            break
        elif escolha_arquivo == '4':
            exit()
        else:
            print("Opção inválida. Por favor, escolha novamente.")

    array_nomes = ler_arquivo_para_array(nome_arquivo)
    if array_nomes:
        menu_algoritmo(array_nomes)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Muda para o diretório do script
    print('dir:', os.getcwd())

    while True:
        menu_arquivo()
