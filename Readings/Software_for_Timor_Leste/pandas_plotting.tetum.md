'# Guia Kompletu ba Vizualizasaun Dadus ho Pandas

## Introdusaun

Vizualizasaun dadus importante tebes iha analiza dadus, permite analista sira hetan komprensaun, identifika padraun, no komunika rezultadu ho efetivu. Pandas, biblioteka manipulasaun dadus ne'ebé forte tebes ba Python, oferese funsionalidade desenhu ne'ebé integra ho di'ak ho DataFrame no Series. Documentu ida ne'e explora kapasidade desenhu varias husi Pandas, diskute tipu desenhu sira, opsaun personalizasaun, no prátika di'ak liu ba kria gráfiku informativu no atrativu.

## Plote Báziku ho Pandas

Pandas uza Matplotlib, biblioteka desenhu ne'ebé populár, atu kria vizualizasaun direta husi DataFrame no Series. Metodu `.plot()` mak metodu primáriu atu kria tipu desenhu sira.

### Gráfiku Linha

Gráfiku linha di'ak tebes atu vizualiza tendénsia liu hosi tempu ka dadus kontínuu. Atu kria gráfiku linha iha Pandas:

```python
df.plot(x='x_column', y='y_column')
```

Gráfiku linha bele hatudu séria sira barak liu hosi espesifika koluna sira barak ba axis y:

```python
df.plot(x='x_column', y=['y1_column', 'y2_column'])
```

### Gráfiku Barra

Gráfiku barra útil atu kompara dadus kategorikál. Atu kria gráfiku barra:

```python
df.plot(x='category_column', y='value_column', kind='bar')
```

Ba gráfiku barra horizontál, uza `kind='barh'`.

### Histograma

Histograma hatudu distribuisaun husi dadus numerikál. Atu kria histograma:

```python
df['column'].plot(kind='hist', bins=30)
```

Parameter `bins` kontrola númeru husi barra sira iha histograma.

### Gráfiku Dispersaun

Gráfiku dispersaun uza atu vizualiza relasaun entre variável numerikál rua:

```python
df.plot(x='x_column', y='y_column', kind='scatter')
```

## Téknika Avansadu Desenhu

### Subplots

Pandas permite kriasaun husi gráfiku sira barak iha figura ida ho subplots:

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
df.plot(ax=axes[0, 0], kind='line')
df.plot(ax=axes[0, 1], kind='bar')
df.plot(ax=axes[1, 0], kind='scatter')
df['column'].plot(ax=axes[1, 1], kind='hist')
```

### Personaliza Gráfiku

Gráfiku Pandas bele personaliza ho parámetru Matplotlib:

```python
df.plot(title='My Plot', xlabel='X Axis', ylabel='Y Axis', 
        figsize=(10, 6), grid=True, legend=True)
```

Kór, marker, no estilo linha mós bele ajusta:

```python
df.plot(color='red', marker='o', linestyle='--')
```

### Gráfiku Séria Temporál

Pandas di'ak tebes atu desenhu dadus séria temporál. Bainhira índise maka DatetimeIndex, Pandas automaticamente formatu axis x:

```python
df.plot(x='date_column', y='value_column')
```

## Gráfiku Espesializadu

### Gráfiku Kaixa

Gráfiku kaixa hatudu distribuisaun dadus no identifika outlier sira:

```python
df.boxplot(column=['col1', 'col2', 'col3'])
```

### Gráfiku Área

Gráfiku área útil atu hatudu total akumulativu liu hosi tempu:

```python
df.plot(kind='area', stacked=True)
```

### Gráfiku Torta

Gráfiku torta hatudu kompozisaun husi totalidade:

```python
df.plot(kind='pie', y='value_column')
```

## Integrasaun ho Seaborn

Maske Pandas nia desenhu