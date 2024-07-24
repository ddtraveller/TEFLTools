'Unidade Aprendizajen 2

Unidade Aprendizajen 2: Fluxu Kontrolu
- Objetivu:
  * Komprende no uza deklarasaun kondisional
  * Implementa loop ba tarefa repetitivu
- Topiku:
  * Deklarasaun se, elif, no seluk
  * Loop ba no enkuantu
- Atividade:
  * Kria programa ida atu determina se tinan ida maka tinan bissexto iha kalendariu Gregorianu
  * Dezenvolve kuiz kona-ba istória Timor-Leste ho uzu deklarasaun kondisional

Rekursu Unidade

Iha ne'e rekursu detalhadu ba Unidade Aprendizajen 2: Fluxu Kontrolu, formatu iha Markdown:

Unidade Aprendizajen 2: Fluxu Kontrolu - Rekursu Detalhadu

1. Nota Leksiu

Deklarasaun Kondisional

Introdusaun ba Deklarasaun Kondisional
Deklarasaun kondisional permite programa halo desizaun bazeia ba kondisaun sira. Iha Python, ita uza `se`, `elif` (se seluk), no `seluk` ba objetivu ne'e.

Sintaksa Báziku
```python
se kondisaun:
    # kódigu atu ezekuta se kondisaun maka loos
elif kondisaun seluk:
    # kódigu atu ezekuta se kondisaun seluk maka loos
seluk:
    # kódigu atu ezekuta se kondisaun hotu-hotu la loos
```

Ezemplu
```python
idade = 18
se idade < 13:
    print("Ita labarik.")
elif idade < 20:
    print("Ita adolexente.")
seluk:
    print("Ita adultu.")
```

Ekspresaun Boolean
Deklarasaun kondisional depende ba ekspresaun Boolean, ne'ebé avalia ba loos ka falsu. Operadór komparasaun komum inklui:
- `==` (hanesan ho)
- `!=` (la hanesan ho)
- `<` (ki'ik liu)
- `>` (boot liu)
- `<=` (ki'ik liu ka hanesan)
- `>=` (boot liu ka hanesan)

Loop

Introdusaun ba Loop
Loop permite ita repete bloku kódigu balu-barak. Python iha tipo rua prinsipál husi loop: loop `ba` no loop `enkuantu`.

Loop Ba
Loop ba uza atu itera liu husi sekuénsia (hanesan lista, tuple, ka string) ka objetu seluk ne'ebé bele itera.

Sintaksa:
```python
ba item iha sekuénsia:
    # kódigu atu ezekuta ba kada item
```

Ezemplu:
```python
frutas = ["maka", "banana", "seri"]
ba fruta iha frutas:
    print(fruta)
```

Loop Enkuantu
Loop enkuantu repete bloku kódigu too kondisaun sai loos.

Sintaksa:
```python
enkuantu kondisaun:
    # kódigu atu ezekuta too kondisaun sai loos
```

Ezemplu:
```python
konta = 0
enkuantu konta < 5:
    print(konta)
    konta += 1
```

2. Pergunta Diskusaun

1. Oinsaa deklarasaun kondisional ajuda atu programa sai liu tan flexivel?
2. Ita bele hanoin kazu vida real ne'ebé ita uza if-else hodi halo desizaun?
3. Saida diferensa entre loop `ba` no loop `enkuantu`? Bainhira ita sei uza ida liu fali seluk?
4. Oinsaa loop bele uza atu rezolve problema iha vida loroloron iha Timor-Leste?
5. Saida problema potensial ne'ebé bele mosu se kondisaun iha loop enkuantu la sai falsu?

3. Instrusaun Eskersisiu Hakerek

Hakerek parágrafu badak ida atu esplika oinsaa ita sei uza deklarasaun kondision