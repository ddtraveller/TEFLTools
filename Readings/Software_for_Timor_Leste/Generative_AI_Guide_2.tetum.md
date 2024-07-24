'# Gía ba Uzu AI ba Asisténsia Kódigu no Rezolve Problema

Gía ne'e explora maneira oin-oin atu uza AI ba asisténsia kódigu no rezolve problema, ho ezemplu 12 ne'ebé diferente hosi aplikasaun prátiku to'o aplikasaun divertidu.

## Tabela Husi Konteúdu
1. [Kompletamentu Kódigu ho GPT-3](#1-kompletamentu-kódigu-ho-gpt-3)
2. [Hadia Bug Automátika](#2-hadia-bug-automátika)
3. [Lian Naturál ba Konsulta SQL](#3-lian-naturál-ba-konsulta-sql)
4. [Jeneradór Esplikasaun Kódigu](#4-jeneradór-esplikasaun-kódigu)
5. [Dezaiñu Algoritmu ho Asisténsia AI](#5-dezaiñu-algoritmu-ho-asisténsia-ai)
6. [Refaktorizasaun Kódigu Automátika](#6-refaktorizasaun-kódigu-automátika)
7. [Revizaun Kódigu ho AI](#7-revizaun-kódigu-ho-ai)
8. [Jerasaun Kazu Teste](#8-jerasaun-kazu-teste)
9. [Tradusaun Kódigu Entre Língua Programasaun](#9-tradusaun-kódigu-entre-língua-programasaun)
10. [Dokumentasaun Kódigu Jeneradu husi AI](#10-dokumentasaun-kódigu-jeneradu-husi-ai)
11. [Interpretadór Kódigu Emoji](#11-interpretadór-kódigu-emoji)
12. [Simuladór Programadór Par ho AI](#12-simuladór-programadór-par-ho-ai)

## 1. Kompletamentu Kódigu ho GPT-3

GPT-3 bele uza atu kompletu fragmentu kódigu, ajuda dezenvolvedór atu hakerek kódigu liu husi lalais.

```python
importa openai

openai.api_key = 'itu-nia-api-xave-iha-ne\'e'

def kompletu_kódigu(prompt):
    resposta = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return resposta.choices[0].text.strip()

# Uzu ezemplu
fragmentu_kódigu = """
def fibonacci(n):
    # Kompletu funsaun sekénsia Fibonacci
"""

kódigu_kompletu = kompletu_kódigu(fragmentu_kódigu)
print(kódigu_kompletu)
```

Ezemplu output:
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

Esplikasaun: Ezemplu ne'e uza modelu GPT-3 husi OpenAI atu kompletu fragmentu kódigu. Modelu ne'e hetan asinatura funsaun no komentáriu, no nia jera implementasaun kompletu husi funsaun sekénsia Fibonacci.

## 2. Hadia Bug Automátika

AI bele uza atu deteta automaticamente no hadia bug iha kódigu.

```python
importa openai

openai.api_key = 'itu-nia-api-xave-iha-ne\'e'

def hadia_bug(buggy_code):
    prompt = f"Hadia bug iha kódigu tuir mai:\n\n{buggy_code}\n\nKódigu ne'ebé hadia ona:"
    resposta = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return resposta.choices[0].text.strip()

# Uzu ezemplu
kódigu_bug = """
def kalkula_média(númeru):
    total = 0
    ba num iha númeru:
        total += num
    return total / len(númeru)

# Testa funsaun
print(kalkula_média([1, 2, 3, 4,

Halo translate ba Tetum:
'sponse.choices[0].text.strip()

# Ezemplu uzu
problema = "Hakat ba longest palindromic substring iha string ida ne'ebé hatete ona."

algorithm = design_algorithm(problema)
print(algorithm)

Ezemplu output:
```
Algorithmu:
1. Inisia variável 'longest_palindrome' hodi rai longest palindrome ne'ebé hetan, inisialmente string mamuk.
2. Ba karater kada ida iha string:
   a. Konsidera nudar sentru husi palindrome ne'ebé nia naruk ímpar:
      - Expand ba liur husi sentru, kompara karater iha naruk rua.
      - Para bainhira karater la tuir malu ka to'o iha limites string nian.
      - Update 'longest_palindrome' bainhira palindrome atuál boot liu.
   b. Konsidera nudar sentru husi palindrome ne'ebé nia naruk par ho karater tuir mai:
      - Expand ba liur husi sentru, kompara karater iha naruk rua.
      - Para bainhira karater la tuir malu ka to'o iha limites string nian.
      - Update 'longest_palindrome' bainhira palindrome atuál boot liu.
3. Fó fila 'longest_palindrome'.

Algorithmu ne'e iha kompleksidade tempu O(n^2) no kompleksidade espasu O(1), nune'e n mak naruk husi string entrada.
```

Esplikasaun: Ezemplu ne'e hatudu oinsá AI bele asistensia iha desenha algorithmu sira. Ho deskrisaun problema ne'ebé hatete ona, modelu AI halo algorithmu ida ho pasu-pasu hodi rezolve problema hakat ba longest palindromic substring.

## 6. Refaktor Kodigu Automatikamente

AI bele sujere melloramentu refaktor ba kodigu ezistente.

```python
import openai

openai.api_key = 'ita-nia-api-key-iha-ne'e'

def refactor_code(kodigu):
    prompt = f"""
Refaktor kodigu tuir mai hodi hadia nia lejibilidade no efisiénsia:

{kodigu}

Kodigu refaktor:
"""
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Ezemplu uzu
code_to_refactor = """
def f(x, y):
    z = x + y
    if z > 10:
        print("Boot")
    else:
        if z < 5:
            print("Ki'ik")
        else:
            print("Médiu")
    return z
"""

refactored_code = refactor_code(code_to_refactor)
print(refactored_code)
```

Ezemplu output:
```python
def klasifika_suma(x, y):
    total = x + y
    if total > 10:
        kategoria = "Boot"
    elif total < 5:
        kategoria = "Ki'ik"
    else:
        kategoria = "Médiu"
    print(kategoria)
    return total
```

Esplikasaun: Ezemplu ne'e uza AI atu refaktor kodigu ida ne'ebé hatete ona. Modelu AI sujere melloramentu sira hanesan naran funsaun no variável ne'ebé deskriptivu liu, flukso kontrolu ne'ebé simplifika, no estrutura ne'ebé di'ak liu.

## 7. Revisaun Kodigu ho AI

AI bele halo revisaun kodigu automatikamente, sujere melloramentu sira no kaptura problema sira ne'ebé potensial.

```python
import openai

openai.api_key = 'ita-nia-api-key-iha-ne'e'

def review_code(kodigu):
    prompt = f"""
Halo revisaun kodigu ba kodigu tuir mai. Sujere melloramentu sira no hatudu problema sira ne'ebé potensial:

{kodigu}

Revisaun kodigu:
"""
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=200,