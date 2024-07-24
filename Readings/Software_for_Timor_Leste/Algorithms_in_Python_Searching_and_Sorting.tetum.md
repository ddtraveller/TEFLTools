'# Introdução

Procurar e ordenar são operações fundamentais na ciência da computação. Estes algoritmos formam a base de muitas operações complexas e são essenciais para a manipulação eficiente de dados e recuperação. 

## Vocabulário

- **Algoritmo**: Uma sequência de instruções bem definidas para resolver um problema específico.
- **Estrutura de Dados**: Uma maneira de organizar e armazenar dados para acesso e modificação eficientes.
- **Complexidade de Tempo**: Uma medida de como o tempo de execução de um algoritmo aumenta com o tamanho dos dados de entrada.
- **Complexidade de Espaço**: Uma medida de como o uso de memória de um algoritmo aumenta com o tamanho dos dados de entrada.
- **Força Bruta**: Uma abordagem direta para resolver um problema, geralmente tentando todas as soluções possíveis. 
- **Dividir e Conquistar**: Uma estratégia de decompor um problema em dois ou mais sub-problemas do mesmo tipo ou relacionado, até que estes se tornem simples o suficiente para serem resolvidos diretamente.
- **No local (In-place)**: Um algoritmo é dito no local se não precisa de um espaço extra e produz uma saída na mesma memória que contém os dados, transformando a entrada 'no local'. 
- **Estável**: Um algoritmo de ordenação é dito estável se dois objetos com chaves iguais aparecem na mesma ordem na saída ordenada como aparecem na matriz de entrada a ser ordenada.
- **Determinístico**: Um algoritmo que, dado uma entrada específica, sempre produz a mesma saída, com a máquina subjacente sempre passando pela mesma sequência de estados.
- **Não Determinístico**: Um algoritmo que, dado uma entrada específica, poderia exibir comportamentos diferentes em diferentes execuções devido a aleatoriedade ou outros fatores.

## Algoritmos de Pesquisa

Os algoritmos de pesquisa são projetados para verificar ou recuperar um elemento de qualquer estrutura de dados onde ele é armazenado.

### Pesquisa Linear 

A pesquisa linear é o algoritmo de pesquisa mais simples que verifica sequencialmente cada elemento na lista até que uma correspondência seja encontrada ou a lista inteira tenha sido pesquisada.

```python
def linear_search(arr, x):
    """
    Realiza uma pesquisa linear em uma matriz.
    
    :param arr: A matriz para pesquisar
    :param x: O valor para procurar
    :return: O índice da primeira ocorrência de x em arr, ou -1 se x não for encontrado
    """
    for i in range(len(arr)):
        if arr[i] == x:  
            return i   # Retorna o índice se x for encontrado
    return -1   # Retorna -1 se x não for encontrado
```

- **Complexidade de Tempo**: O(n) - onde n é o número de elementos
  - Melhor caso: O(1) se o elemento alvo for encontrado na primeira posição
  - Pior caso: O(n) se o elemento alvo estiver na última posição ou não estiver presente
  - Caso médio: O(n)
- **Complexidade de Espaço**: O(1) - apenas algumas variáveis são usadas, independentemente do tamanho da entrada
- **Caso de Uso**: Apropriado para listas pequenas ou dados não ordenados

#### Exemplo

Suponha que você tenha uma matriz de números `[5, 2, 4, 6, 1, 3]` e você queira procurar o número 4.

Com a pesquisa linear:
1. Compare 4 com o primeiro elemento, 5. Não é igual, então passe para o próximo elemento.  
2. Compare 4 com 2. Não é igual, passe para o próximo.
3. Compare 4 com o terceiro elemento, 4. É igual, então retorne o índice 2.

A função de pesquisa linear retornará 2, indicando que 4 está no índice 2 na matriz.

Se o alvo fosse 7, a pesquisa linear compararia com cada elemento e, não encontrando uma correspondência, retornaria -1 para indicar que 7 não está na matriz.

### Pesquisa Binária

A pesquisa binária é um algoritmo eficiente para pesquisar uma matriz ordenada, dividindo repetidamente o intervalo de pesquisa pela metade. 

```python
def binary_search(arr, x):
    """
    Realiza uma

'Presiza motivus.

## Algoritmu Ordenasaun

Algoritmu ordenasaun hodi habelar elementu sira iha lista ida iha ordem espesífiku, normalmente kresimentu ka desendente.

### Ordenasaun Bubble

Bubble sort mak algoritmu ordenasaun ida ne'ebé simples ne'ebé bazeia ba komparasaun ne'ebé repete nafatin hodi tama ba lista, kompara elementu sira ne'ebé besik malu no troka sira se sira iha ordem sala. Halo dalan hirak ne'e liu husi lista repete to'o lista sai ordenadu.

```python
def bubble_sort(arr):
    """
    Ordena array uza ordenasaun bubble.
    
    :param arr: Array ne'ebé presiza atu ordena
    """
    n = len(arr)
    
    # Habelar liu husi elementu hotu iha array
    for i in range(n):
        
        # Elementu ikus iha tiha ona iha sira nia fatin
        for j in range(0, n-i-1):
            
            # Troka se elementu ne'ebé hetan maka boot liu duke elementu tuir mai
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

- **Komplexidade Tempu**: O(n^2) 
  - Kazu di'ak liu: O(n) bainhira array tiha ona ordenadu
  - Kazu naruk liu: O(n^2)
  - Kazu média: O(n^2)
- **Komplexidade Espasu**: O(1)
- **Estável**: Sin
- **Kazu Uza**: Fins edukativu, datasets boot liu

#### Ezemplu

Halo ordenasaun ba array `[64, 34, 25, 12, 22, 11, 90]` uza ordenasaun bubble.

Dalan Primeiru:
- `[64, 34, 25, 12, 22, 11, 90]` -> `[34, 64, 25, 12, 22, 11, 90]`, troka 64 ho 34
- `[34, 64, 25, 12, 22, 11, 90]` -> `[34, 25, 64, 12, 22, 11, 90]`, troka 64 ho 25
- `[34, 25, 64, 12, 22, 11, 90]` -> `[34, 25, 12, 64, 22, 11, 90]`, troka 64 ho 12
- `[34, 25, 12, 64, 22, 11, 90]` -> `[34, 25, 12, 22, 64, 11, 90]`, troka 64 ho 22
- `[34, 25, 12, 22, 64, 11, 90]` -> `[34, 25, 12, 22, 11, 64, 90]`, troka 64 ho 11
- La troka 90 tanba nia mak elementu boot liu.

Elementu boot liu, 90, halai ba parte direita. Array seidauk ordenadu kompletu, tanba ne'e ita kontinua ba dalan tuir mai.

Dalan Segundu:
- `[34, 25, 12, 22, 11, 64, 90]` -> `[25, 34, 12, 22, 11, 64, 90]`, troka 34 ho 25
- `[25, 34, 12, 22, 11, 64, 90]` -> `[25, 12, 34, 22, 11, 64, 90]`, troka 34 ho 12
- `[25, 12, 34, 22, 11, 64, 90]` -> `[25, 12, 22, 34, 11, 64, 90]`, troka 34 ho 22
- `[25, 12, 22, 34, 11, 64, 90]` -> `[25, 12, 22, 11, 34, 64, 90]`, troka 34 ho 11
- La

'dx , arr i
- **Komplexidade Tempu**: O(n^2)
  - Kazu di'ak liu: O(n^2) 
  - Kazu aat liu: O(n^2)
  - Kazu média: O(n^2) 
- **Komplexidade Espasiu**: O(1)
- **Estável**: Lae (bele halo estável ho espasiu adisionál)
- **Kazu Uza**: Datasets ki'ik, situasaun sira-ne'ebé iha ne'ebé eskrita memória karun

#### Ezemplu

Fali, hau sei sorta array `[64, 34, 25, 12, 22, 11, 90]` uza sort seleksaun.

Pasa Primeiru:
- Elementu minimu maka 11. Troka nia ho elementu primeiru.
- Rezultadu: `[11, 34, 25, 12, 22, 64, 90]`

Pasa Segundu:
- Elementu minimu iha array unsorted remanesente maka 12. Troka nia ho elementu segundu.
- Rezultadu: `[11, 12, 25, 34, 22, 64, 90]`

Pasa Terseru:
- Elementu minimu iha array unsorted remanesente maka 22. Troka nia ho elementu terseru.
- Rezultadu: `[11, 12, 22, 34, 25, 64, 90]`

Prosesu kontinua to'o array hotu-hotu sorta ona iha pasa ne'ebé hitu:
`[11, 12, 22, 25, 34, 64, 90]`

Iha kada pasu, sort seleksaun hili elementu minimu husi parte unsorted iha array no troka nia ho elementu unsorted ne'ebé iha karuk liu, gradualmente harii parte sorta husi karuk ba loos.

Maske sort seleksaun hadia liu sort borbulha liuhusi halo menus trokas (ne'ebé bele karun se elementu sira boot), nia nunka efisiente tebes tanba nia komplexidade tempu kwadrátiku.

### Merge Sort

Sort Merge ne'e algoritmu ida divide-and-conquer, ne'ebé fahe lista unsorted ba iha n sublistas, ida-idak iha elementu ida (lista ida ho elementu ida konsidera ona nudar sorta), depois kontinuamente une sublistas atu produz sublista foun ne'ebé sorta to'o iha sublista ida de'it remanesente, ne'ebé lista sorta.

```python
def merge_sort(arr):
    if len(arr) > 1:
        # Hetan metade husi array
        mid = len(arr)//2
        
        # Divide elementu array ba metade karuk no loos
        L = arr[:mid]
        R = arr[mid:]
        
        # Sorta metade primeiru
        merge_sort(L)
        
        # Sorta metade segundu
        merge_sort(R)
        
        i = j = k = 0
        
        # Kopia dadus ba array temporáriu L[] no R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
arr[k] = L[i]
i += 1
else:
arr[k] = R[j]
j += 1
k += 1
Copy    # Verifika se elementu ida seidauk
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
Copy
- **Komplexidade Tempu**: O(n log n) iha kazu hotu
  - Kazu di'ak liu: O(n log n)
  - Kazu aat liu: O(n log n) 
  - Kazu média: O(n log n)
- **Komplexidade Espasiu**: O(n) 
- **Estável**: Sin
- **Kazu Uza**: Bainhira presiza estabilidade, ba listas ligadas, ba sort esterna

#### Ezemplu

Hau sei sorta array `[64, 34, 25, 12, 22, 11,

Inicialmente até termos sub-arrays de tamanho 1, que são, por definição, ordenados. Em seguida, combinamos os sub-arrays ordenados: [11, 12, 22, 25, 34, 64, 90]. O Quick sort é frequentemente mais rápido na prática do que outros algoritmos O(n log n), porque seu loop interno pode ser implementado de maneira eficiente na maioria das arquiteturas. No entanto, sua pior complexidade de tempo O(n^2) torna-o susceptível a entradas adversas e não é um tipo de ordenação estável.

Comparação de Algoritmos
Algoritmos de Busca
Busca Linear vs. Busca Binária:

A busca linear é mais simples, mas menos eficiente para grandes conjuntos de dados.
A busca binária é muito mais rápida para grandes conjuntos de dados, mas requer que os dados estejam ordenados.

Algoritmos de Ordenação
Bubble Sort vs. Insertion Sort vs. Selection Sort:

Todos têm complexidade de tempo O(n^2), tornando-os ineficientes para grandes conjuntos de dados.
O Insertion sort geralmente tem melhor desempenho do que o bubble sort e é adaptativo (eficiente para dados quase ordenados).
A Selection sort faz o menor número de trocas e pode ser preferível quando a escrita na memória é cara.

Algoritmos de Ordenação Mais Eficientes (não implementados no script, mas vale a pena mencionar):

Merge Sort: complexidade de tempo O(n log n), estável, mas requer espaço extra O(n).
Quick Sort: complexidade de tempo médio O(n log n), in-place, mas instável e tem pior caso O(n^2).
Heap Sort: complexidade de tempo O(n log n), in-place, mas instável.

Aplicações no Mundo Real
Busca:

Consultas de banco de dados
Funções de busca em editores de texto
Localização de itens em plataformas de comércio eletrónico

Ordenação:

Organização de dados em planilhas
Organização de itens no e-commerce (por preço, classificação, etc.)
Otimização de indexação de banco de dados

Notação Big O
A notação Big O é uma notação matemática que descreve o comportamento limitante de uma função quando o argumento tende para um valor específico ou infinito. Na ciência da computação, é usada para classificar algoritmos de acordo com o crescimento do tempo de execução ou dos requisitos de espaço à medida que o tamanho da entrada aumenta.
Aqui estão algumas complexidades de tempo comuns e suas notações:

O(1) (tempo constante): O tempo de execução do algoritmo é constante, independentemente do tamanho dos dados de entrada. Exemplo: acessar um elemento de um array pelo seu índice.
O(log n) (tempo logarítmico): O tempo de execução do algoritmo cresce logaritmicamente com o tamanho dos dados de entrada. Exemplo: busca binária.
O(n) (tempo linear): O tempo de execução do algoritmo cresce linearmente com o tamanho dos dados de entrada. Exemplo: busca linear, percorrer um array.
O(n log n) (tempo quase linear): O tempo de execução do algoritmo é uma combinação de linear e logarítmico. Muitos algoritmos eficientes de ordenação, como o Merge sort e o Quick sort, têm uma complexidade média de tempo O(n log n).
O(n^2) (tempo quadrático): O tempo de execução do algoritmo é proporcional ao quadrado do tamanho dos dados de entrada. Exemplo: algoritmos simples de ordenação como bubble sort, insertion sort e selection sort.
O(2^n) (tempo exponencial): O tempo de execução do algoritmo dobra para cada elemento adicional nos dados de entrada. Exemplo: cálculo recursivo dos números de Fibonacci.
O(n!) (tempo factorial): O tempo de execução do algoritmo multiplica por um fator adicional para cada elemento. Exemplo: gerar todas as permutações de uma lista.

c é uma constante fixa que depende dos detalhes da implementação, hardware, etc., mas não muda com o tamanho da entrada.
A notação Big O fornece um limite superior para a taxa de crescimento de uma função e é usada para descrever o pior cenário. Por exemplo, a pior complexidade de tempo do Quick Sort é O(n^2), mas sua complexidade méd