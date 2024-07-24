'Unidade Aprendizajen 5

## Unidade Aprendizajen 5: Manipulasaun Arkivu no Manipulasaun Esepsaun
- Objetivus:
  * Lee husi no hakerek ba arkivus
  * Manipula eseptuas iha programa Python
- Topikus:
  * Abertura, leitura, no hakerek arkivus
  * Blokus Try-except ba manipulasaun erru
- Atividades:
  * Kria programa ida atu lee no analiza dadus husi arkivu CSV kona-ba produsaun agrikultura Timor-Leste
  * Implementa manipulasaun erru iha programa sira ne'ebe antes ne'e

## Rekursu Unidade

Iha ne'e mak rekursu detalhadu ba Unidade Aprendizajen 5: Manipulasaun Arkivu no Manipulasaun Esepsaun, formatu iha Markdown:

# Unidade Aprendizajen 5: Manipulasaun Arkivu no Manipulasaun Esepsaun

## 1. Nota Palestra

### Manipulasaun Arkivu

#### Abertura Arkivus
```python
# Abertura báziku arkivu
file = open('filename.txt', 'r')  # 'r' ba modu leitura

# Uza deklarasaun 'with' (rekomendadu)
with open('filename.txt', 'r') as file:
    # Operasaun arkivu iha ne'e
```

Modu Arkivu:
- 'r': Leitura (default)
- 'w': Hakerek (sobrepoe konteudu ezistente)
- 'a': Akresenta (adisiona ba konteudu ezistente)
- 'r+': Leitura no Hakerek

#### Leitura Arkivus
```python
# Lee arkivu tomak
content = file.read()

# Lee liña husi liña
for line in file:
    print(line)

# Lee númeru karater espesífiku
chunk = file.read(10)  # Lee 10 karateres
```

#### Hakerek Arkivus
```python
with open('output.txt', 'w') as file:
    file.write("Ola, Timor-Leste!")
    file.writelines(["Linia 1\n", "Linia 2\n"])
```

### Manipulasaun Esepsaun

#### Estrutura Báziku
```python
try:
    # Kódigo ne'ebé bele levanta eseptu
    result = 10 / 0
except ZeroDivisionError:
    # Manipula eseptu espesífiku
    print("La bele fahe husi zero!")
except Exception as e:
    # Manipula eseptu seluk
    print(f"Ocorre erru ida: {e}")
else:
    # Executa se laiha eseptu
    print("Operasaun suksesu")
finally:
    # Sempre executa, independentemente husi eseptu
    print("Kódigo limpeza")
```

#### Eseptu Komúns
- `FileNotFoundError`: Bainhira tenta acessu ba arkivu ne'ebé laiha
- `ValueError`: Bainhira operasaun simu argumentu ho tipu loos maibé ho valor inapropriádu
- `TypeError`: Bainhira operasaun hala'o iha objetu ho tipu inapropriádu
- `IndexError`: Bainhira tenta acessu ba índise ne'ebé liu husi range

### Traballu ho Arkivu CSV
```python
import csv

# Leitura CSV
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Hakerek CSV
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Naran', 'Idade', 'Cidade'])
    csv_writer.writerow(['Ana', 25, 'Dili'])
```

## 2. Perguntas Diskusaun

1. Oinsa manipulasaun arkivu bele útil iha jestaun dadus agrikultura iha Timor-Leste?
2. Saida mak risku potensiál sira husi la implementa manipulasaun eseptu propriadu iha programa ida?
3. Oinsa arkivus CSV bele uza ba monitoriza