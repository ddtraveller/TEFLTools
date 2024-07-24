"Unidade Aprendizajen 4

## Unidade Aprendizajen 4: Estrutura Dadus
- Objetivu:
  * Komprende no uza lista, tupla, no dicionáriu
  * Manipula efetivamente estrutura dadus
- Tópiku:
  * Lista no komprensaun lista
  * Tupla no nia uzu
  * Dicionáriu no par xave-valór
- Atividade:
  * Kria programa ida ba maneja inventáriu ba loja Tais lokál
  * Dezenvolve dicionáriu Tetum-Inglés

## Rekursu Unidade

Iha ne'e detallu rekursu ba Unidade Aprendizajen 4: Estrutura Dadus, formatu iha Markdown:

# Unidade Aprendizajen 4: Estrutura Dadus - Rekursu Detallu

## 1. Nota Palestra

### Lista

#### Introdusaun ba Lista
- Lista mak kolesaun ordenadu, mutável husi item sira iha Python
- Kria lista uza hakotuuk kuadradu []
- Item sira iha lista bele husi tipo dadus ne'ebé diferente

```python
# Kriasaun lista
fruits = ["banana", "apple", "orange"]
mixed_list = [1, "two", 3.0, True]
```

#### Aksesu ba Elementu Lista
- Elementu lista nian aksesu uza índise, hahu husi 0
- Índise negativu konta husi rohan lista nian

```python
fruits = ["banana", "apple", "orange"]
print(fruits[0])  # Output: banana
print(fruits[-1])  # Output: orange
```

#### Modifikasaun Lista
- Lista sira mutável, signifika sira bele muda depois kriasaun
- Uza índise ba modifika elementu individuál

```python
fruits = ["banana", "apple", "orange"]
fruits[1] = "mango"
print(fruits)  # Output: ["banana", "mango", "orange"]
```

#### Métodu Lista
- append(): Hatama item ida ba rohan lista nian
- remove(): Halo tuur okorensia primeiru husi item ida
- sort(): Ordena lista iha orden asendente
- reverse(): Halo lista iha orden tuun

```python
fruits = ["banana", "apple", "orange"]
fruits.append("mango")
fruits.remove("apple")
fruits.sort()
fruits.reverse()
```

#### Komprensaun Lista
- Dalan badak ida ba kria lista bazeia ba lista ezistente
- Sintakse: [espresaun ba item iha iterável se kondisaun]

```python
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)  # Output: [1, 4, 9, 16, 25]
```

### Tupla

#### Introdusaun ba Tupla
- Tupla mak kolesaun ordenadu, imutável husi item sira iha Python
- Kria tupla uza parentezes ()
- Item sira iha tupla bele husi tipo dadus ne'ebé diferente

```python
# Kriasaun tupla
coordinates = (10.5, -7.2)
person = ("John", 30, "Engineer")
```

#### Aksesu ba Elementu Tupla
- Aksesu ba elementu tupla nian uza índise, hanesan ba lista

```python
coordinates = (10.5, -7.2)
print(coordinates[0])  # Output: 10.5
```

#### Imutabilidade husi Tupla
- Tupla la bele modifika depois kriasaun
- Tentativa atu muda tupla sei rezulta iha erru

```python
coordinates = (10.5, -7.2)
coordinates[0] = 11.0  # Ne'e sei fo erru TypeError
```

#### Bila Uza Tupla
- Uza tupla ba kolesaun sira-ne'ebé tenke la muda
- Ezemplu: koordenada, valór kór RGB, rekordu bazeia dadus

#### 'Unpacking' Tupla
- A