'Unidade Aprendizajen 3

Unidade Aprendizajen 3: Funsaun no Modulu
- Objetivus:
  * Define no uza funsaun
  * Komprende konseitu husi modulu
- Topikus:
  * Definisaun no utilizasaun funsaun
  * Parameter no valor retorno
  * Importasaun no utilizasaun modulu
- Atividades:
  * Hakerek funsaun ba konverte entre dolar Amerika no moeda Timor-Leste (USD)
  * Kria modulu ho funsaun kona-ba geografia Timor-Leste (exemplu, kalkula distansia entre sidade)

Rekursu Unidade

Iha ne'e rekursu detalladu ba Unidade Aprendizajen 3: Funsaun no Modulu, formatu iha Markdown:

Unidade Aprendizajen 3: Funsaun no Modulu - Rekursu Detalladu

1. Nota Lei

Funsaun

Introdusaun ba Funsaun
- Funsaun mak bloku kodigu ne'ebe bele uza fali ne'ebe halo tarefa espesifiku
- Funsaun ajuda organiza kodigu, hamenus repitisaun, no hadia lezibilidade
- Funsaun bele simu inputs (parameters) no fo sai outputs

Sintaksis Funsaun
```python
def function_name(parameter1, parameter2, ...):
    # Isi funsaun
    # Kodigu ne'ebe atu halo
    return result  # Optional
```

Utilizasaun Funsaun
- Funsaun uza liu husi naran funsaun ne'ebe tuir ho parentesis
- Argumentu hatama iha laran parentesis
```python
result = function_name(arg1, arg2)
```

Parameter no Argumentu
- Parameter mak variavel sira ne'ebe lista iha definisaun funsaun
- Argumentu mak valor atual sira ne'ebe pas ba funsaun bainhira funsaun ne'e kalla

Valor Retorno
- Funsaun bele fo sai valor liu husi instrusaun `return`
- Se la uza instrusaun return, funsaun sei fo sai `None`

Exemplu: Area Retangulu
```python
def calculate_area(length, width):
    area = length * width
    return area

rectangle_area = calculate_area(5, 3)
print(f"The area of the rectangle is {rectangle_area}")
```

Modulu

Introdusaun ba Modulu
- Modulu mak arkivu ne'ebe kontein kodigu Python (definisaun, funsaun, variavel)
- Modulu ajuda organiza no reuza kodigu iha programa sira ne'ebe diferente

Importasaun Modulu
```python
import module_name
from module_name import function_name
from module_name import *  # Importa hotu (uza ho kuidadu)
```

Utilizasaun Funsaun Modulu
```python
import math
radius = 5
circumference = 2 * math.pi * radius
```

Kria Modulu Personalizadu
- Salva kodigu Python iha fail .py
- Importa hanesan modulu seluk

Exemplu: Modulu Geografia Timor-Leste
```python
# tl_geography.py
def distance_between_cities(city1, city2):
    # Kalkula distansia logika iha ne'e
    pass

def list_major_cities():
    return ["Dili", "Baucau", "Maliana", "Suai", "Lospalos"]
```

2. Perguntas Diskusaun

1. Oinsaa funsaun bele hadia organizasaun no reusabilidade kodigu?
2. Saida mak diferensa entre parameter no argumentu iha funsaun?
3. Bainhira mak ita sei uza valor retorno iha funsaun, no bainhira ita bele la presiza ida?
4. Oinsaa modulu bele ajuda iha dezenvolvimentu programa Python ne'ebe boot liu?
5. Saida mak vantajen no desvantajen potensial husi uza modulu iha ita nia kodigu?
6. Oinsaa funsaun no modulu bele util iha rezolve problema sira iha mundu real iha Timor-Leste?

3. Instrusaun Ezersisiu Hakerek

Ezersisiu 1: Dokumentasa