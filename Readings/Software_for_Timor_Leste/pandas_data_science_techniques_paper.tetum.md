'Teknikasaun Sientifiku Dadus: Husi Kódigu ba Karreira 

## Introdusaun 

Iha mundu ne'ebé konsentra ba dadus iha loron-loron, abilidade atu manipula, analiza, no visualiza dadus sai hanesan valor di'ak liu iha profisaun sira ne'ebé la hanesan. Papel ida ne'e examina skript Python ne'ebé hatudu teknikasaun avansadu spreadsheet uza biblioteka pandas, no esplika aspetu tékniku husi kódigu no implikasaun barak husi habilidade sira ne'e iha dalan karreira ne'ebé la hanesan.

## Analiza Skript no Fundamentu Sientifiku Dadus 

### 1. Kriasaun Dadus no Input 

```python 
data = ''' 
Date,Municipality,Product,Sales,Price 
2023-01-01,Dili,Rice,100,1.5 
... 
''' 
df = pd.read_csv(StringIO(data)) 
``` 

Parte ida ne'e simula input dadus, ne'ebé sai hanesan fundamentu iha sientifiku dadus. Iha situsaun mundo real, dadus bele mai husi fonte sira ne'ebé la hanesan hanesan database, API, ka sistema arkivu. Abilidade atu lee no prosesa dadus husi fonte sira ne'ebé la hanesan sai importante tebes ba papel ne'ebé iha konesimentu kona-ba dadus.

### 2. Hamlaha Dadus 

```python 
def clean_product_name(name): 
    return re.sub(r'[^a-zA-Z]', '', name).lower() 

df['CleanProduct'] = df['Product'].apply(clean_product_name) 
``` 

Hamlaha dadus sai hanesan parte ne'ebé konsumu tempu barak liu husi analiza dadus. Kódigu ida ne'e uza espressaun regular atu padroniza naran produtu. Dadus ne'ebé moos no konsistente sai esensial ba analiza ne'ebé presizu no sai hanesan habilidade importante ba analista dadus no sientista.

### 3. Tabela Pivot 

```python 
pivot_table = pd.pivot_table(df, values='Sales', index=['Municipality'], columns=['CleanProduct'], aggfunc=np.sum, fill_value=0) 
``` 

Tabela pivot sai hanesan meiu ida ne'ebé potent ba sumariza no analiza dadus. Sira autoriza atu hetan insight lalais husi dataset sira ne'ebé kompleksu, habilidade ida ne'e valiozu la'ós de'it iha sientifiku dadus maibé mós iha analiza negósiu no planeamentu finanseira.

### 4. Haree Dadus 

```python 
price_lookup = df.set_index('CleanProduct')['Price'].to_dict() 
df['LookedUpPrice'] = df['CleanProduct'].map(price_lookup) 
``` 

Kódigu ida ne'e hatudu operasaun hanesan VLOOKUP, ne'ebé komunmente uza iha spreadsheet. Abilidade atu bele hetan informasaun efisiente no kombina dadus sai krusial iha tarefa kona-ba dadus barak, husi operasaun negósiu to'o peskiza sientifiku.

### 5. Agregasaun Dadus 

```python 
aggregated_data = df.groupby('Municipality').agg({ 
    'Sales': ['sum', 'mean'], 
    'Price': ['min', 'max'] 
}) 
``` 

Agregasaun permite sumariza dadus husi dimensaun barak. Habilidade ida ne'e sai esensial iha kampu sira hanesan intelijensia negósiu, ne'ebé atu komprende trend no padraun jerál sai importante tebes.

### 6. Visualizasaun Dadus 

```python 
plt.figure(figsize=(12, 6)) 
df.groupby('Municipality')['Sales'].sum().plot(kind='bar') 
plt.title('Total Sales by Municipality') 
``` 

Visualizasaun dadus sai hanesan maneira ida ne'ebé potent atu komunika insight. Habilidade ida ne'e valor di'ak iha profisaun barak, husi