'# Pandas: Guia Kompletu ho Detallu Explicasaun

## 1. Estrutura Dadus

### Series

Series pandas nian mak array ida-dimensional ne'ebé iha label, ne'ebé bele rai dadus husi tipu ne'ebé de'it (integer, float, string, etc.).

Oinsá nudar:
- Kria ho funsaun `pd.Series()`.
- Iha komponente rua prinsipál: índice (labels) no dadus reál.
- Elementu kada ida iha Series iha label úniku iha índice.

Ezemplu ne'ebé esplika:
```python
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
print(series)
```
Kria Series ho índice integer default (0, 1, 2, 3, 4) no valor sira [1, 2, 3, 4, 5].

Operasaun iha Series:
```python
print("Elementu iha índice 2:", series[2])
```
Aksesu ba elementu iha índice 2 (elementu terseiru tanba índise bazia 0).

```python
print("Adisaun:", series + 2)
```
Aumenta 2 ba elementu kada ida iha Series. Pandas halo operasaun elementu-ba-elementu.

```python
print("Multiplikasaun:", series * 3)
```
Multiplica elementu kada ida ho 3.

```python
print("Exponensiasaun:", series ** 2)
```
Eleva elementu kada ida iha Series.

### DataFrame

DataFrame mak estrutura dadus ida-dimensional ne'ebé iha label ho koluna sira ho tipu ne'ebé bele diferente.

Oinsá nudar:
- Kria ho funsaun `pd.DataFrame()`.
- Bele hanoin nudar tabela ka estrutura hanesan spreadsheet.
- Koluna kada ida iha DataFrame iha esensialmente Series ida.

Ezemplu ne'ebé esplika:
```python
data = {
    "Naran": ["John", "Alice", "Bob", "Claire"],
    "Idade": [25, 30, 35, 40],
    "Sidade": ["New York", "London", "Paris", "Tokyo"]
}
df = pd.DataFrame(data)
print(df)
```
Kria DataFrame husi dicionariu. Xave kada ida iha dicionariu sai hanesan naran koluna, no lista korespondente sai hanesan valor iha koluna ne'ebé.

## 2. Manipulasaun Dadus

### Aksesu Dadus

```python
print(df["Naran"])
```
Aksesu ba koluna "Naran" husi DataFrame, no fila nia hanesan Series ida.

```python
print(df.iloc[1])
```
`iloc` uza ba índise lokalizaun bazeia ba integer. Fila liña segunda (índise 1) husi DataFrame hanesan Series ida.

### Modifika DataFrame

```python
df["Nasaun"] = ["USA", "UK", "France", "Japan"]
```
Aumenta koluna foun "Nasaun" ba DataFrame ho valor sira ne'ebé espesifika ona.

```python
df = df.drop("Sidade", axis=1)
```
Hakuik koluna "Sidade" husi DataFrame. `axis=1` espesifika katak hakuik koluna (la'e liña).

```python
filtered_df = df[df["Idade"] > 30]
```
Kria DataFrame foun ne'ebé inklui de'it liña sira ne'ebé "Idade" liu 30.

### Manipulasaun Dadus Ne'ebé Lakon

```python
print(df.isnull().sum())
```
Verifika ba valor sira ne'ebé falta iha koluna kada ida, no fila total valor ne'ebé falta.

```python
df["Idade"].fillna(df["Idade"].mean(), inplace=True)
```
Troka valor sira ne'ebé falta iha koluna "Idade" ho media idade. `inplace=True` signifika katak alterasaun sira halo ba DataFrame orijinál.

## 3. Analiza Dadus

### Estatístika Bázika

```python
print(df