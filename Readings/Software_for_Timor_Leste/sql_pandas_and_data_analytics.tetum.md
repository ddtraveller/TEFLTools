'# SQL, Pandas, no Analiza Dadus: Halo Ligasaun Koneitu Database ho Instrumentu Siénsia Dadus

## Introdusaun

Hanesan ita hakfodak liu ba fundamentu SQL, importante tebes atu komprende oinsá konseitu sira ne'e relasiona ho teknika manipulasaun no analiza dadus ne'ebé ita halo ona antes ne'e ho pandas. Objetivu husi papel ida ne'e atu halo ligasaun entre operasaun SQL no funsaun pandas, hatudu oinsá konseitu database alinha ho instrumentu no prátika siénsia dadus.

## Estrutura Dadus: Tabela vs. DataFrames

Iha SQL, dadus sira hetan organiza iha tabela ho liña no koluna. Estrutura ida ne'e hanesan ho DataFrames iha pandas:

- Tabela SQL ≈ pandas DataFrame
- Liña SQL ≈ DataFrame Liña
- Koluna SQL ≈ DataFrame Koluna

Diferensa importante maka tabela SQL armazena iha database, maibé DataFrames iha mamória durante sesaun Python ida.

## Operasaun Báziku

### 1. Kria Estrutura Dadus

**SQL:**
```sql
CREATE TABLE Estudantes (
    sid CHAR(20) PRIMARY KEY,
    naran VARCHAR(50),
    tinan INTEGER,
    gpa REAL
);
```

**Pandas:**
```python
df_estudantes = pd.DataFrame({
    'sid': ['53666', '53688', '53650'],
    'naran': ['Jones', 'Smith', 'Brown'],
    'tinan': [18, 20, 19],
    'gpa': [3.4, 3.8, 3.2]
})
```

Abordajen rua ne'e hatudu estrutura ida ba armazena dadus kona-ba estudantes.

### 2. Insere Dadus

**SQL:**
```sql
INSERT INTO Estudantes VALUES ('53666', 'Jones', 18, 3.4);
```

**Pandas:**
```python
df_estudantes = df_estudantes.append({'sid': '53666', 'naran': 'Jones', 'tinan': 18, 'gpa': 3.4}, ignore_index=True)
```

Hanesan SQL presiza insersaun explísitu, DataFrames pandas hamosu ho dadus ona inklui.

### 3. Konsulta/Filtra Dadus

**SQL:**
```sql
SELECT naran, gpa FROM Estudantes WHERE gpa > 3.5;
```

**Pandas:**
```python
df_estudantes[df_estudantes['gpa'] > 3.5][['naran', 'gpa']]
```

SQL no pandas permite filtra dadus bazeia ba kondisaun sira.

### 4. Hatama Ordem

**SQL:**
```sql
SELECT naran, gpa FROM Estudantes ORDER BY gpa DESC;
```

**Pandas:**
```python
df_estudantes.sort_values('gpa', ascending=False)[['naran', 'gpa']]
```

Operasaun hatama orden disponivel iha sistema rua, ho funsionalidade hanesan.

## Konseitu Avansadu

### 1. Liga/Merge Dadus

**SQL:**
```sql
SELECT Estudantes.naran, Kursus.titulu
FROM Estudantes
INNER JOIN Insrito ON Estudantes.sid = Insrito.studid
INNER JOIN Kursus ON Insrito.cid = Kursus.cid;
```

**Pandas:**
```python
df_merge = df_inscrito.merge(df_estudantes, left_on='studid', right_on='sid')
df_merge = df_merge.merge(df_kursus, on='cid')
```

SQL no pandas fornese dalan hodi kombina dadus husi tabela/DataFrames sira ne'ebé iha kampu hanesan.

### 2. Agregasaun

**SQL:**
```sql
SELECT Kursus.titulu, AVG(Estudantes.gpa) as avg_gpa
FROM Estudantes
INNER JOIN Insrito ON Estudantes.sid = Insrito.studid
INNER JOIN Kursus ON Insrito.cid = Kursus.cid
GROUP BY Kursus.cid;
```

**Pandas:**
```python
df_agg = df_merge.groupby('titulu')['gpa'].mean().reset_index()
```

Operasaun agregasaun permite atu rezume dadus, konseitu importante