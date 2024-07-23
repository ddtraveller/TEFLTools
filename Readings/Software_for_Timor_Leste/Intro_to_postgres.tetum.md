'# Prinsípiu básiku PostgreSQL: Introdusaun ba jestaun base de dadus relasionál 

## Introdusaun

PostgreSQL mak sistema jestaun base de dadus relasionál ne'ebé potente, opensource, ne'ebé konhesidu ho nia robustness, extensibilidade, no kumprimentu ba padrões SQL. Artigu ida ne'e atu introdús konseitu fundamentál sira husi PostgreSQL, inklui nia interface linha de komandu, tipu dadus, jestaun base de dadus no tabela, no operasaun SQL básiku.

## 1. Navega iha Interface Linha de Komandu PostgreSQL (psql)

Interface linha de komandu psql mak ferramenta potente ba interasaun ho base de dadus PostgreSQL. Komandu sira ne'ebé importante inklui:

- `\l`: Lista base de dadus hotu
- `\c database_name`: Konekta ba base de dadus ida espesífiku
- `\dt`: Lista tabela sira iha base de dadus atual
- `\d table_name`: Deskreve estrutura husi tabela ida espesífiku
- `\q`: Sai husi psql

Komandu sira ne'e permite uza-na'in sira atu navega no inspeksionaun estrutura base de dadus ho efisiensia.

## 2. Tipu Dadus PostgreSQL

PostgreSQL suporta tipu dadus ne'ebé varia, inklui:

1. **Tipu Numériku**:
   - INT: Númeru tomak
   - SERIAL: Númeru integer ne'ebé auto-incrementa
   - NUMERIC(p,s): Númeru desimal exatu ho presizaun no eskala ne'ebé espesífiku

2. **Tipu Karater**:
   - VARCHAR(n): String ne'ebé nia naruk variável ho naruk máximu
   - TEXT: String ne'ebé nia naruk variável ho laiha limit

3. **Tipu Data/Tempu**:
   - DATE: Data kalendáriu
   - TIME: Tempu loron
   - TIMESTAMP: Data no tempu

4. **Tipu Booleanu**:
   - BOOLEAN: Valor loos ka sala

Hili tipu dadus ne'ebé apropriadu mak importante tebes ba integridade dadus no efisiensia konsulta.

## 3. Kria no Jestaun Base de Dadus ho Tabela

Kria base de dadus iha PostgreSQL simplu:

```sql
CREATE DATABASE eskola;
```

Tabela sira kria uza deklarasaun CREATE TABLE, ne'ebé espesifika estrutura tabela no regras:

```sql
CREATE TABLE estudante (
  id SERIAL PRIMARY KEY,
  naran VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE,
  data_nasimentu DATE,
  gpa NUMERIC(3,2)
);
```

Ezemplu ida ne'e demonstra konseitu sira importante:
- Uza SERIAL ba chave primária ne'ebé auto-incrementa
- Regras hanesan PRIMARY KEY, NOT NULL, no UNIQUE
- Uza tipu dadus sira ne'ebé varia

## 4. Manipulasaun Dadus: INSERT, UPDATE, DELETE

Operasaun manipulasaun dadus básiku iha PostgreSQL inklui:

1. **INSERT**: Hatama rekordu foun ba tabela
   ```sql
   INSERT INTO estudante (naran, email, data_nasimentu, gpa)
   VALUES ('John Doe', 'john@example.com', '2000-01-15', 3.75);
   ```

2. **UPDATE**: Modifika rekordu ezistente
   ```sql
   UPDATE estudante SET gpa = 3.80 WHERE naran = 'John Doe';
   ```

3. **DELETE**: Hasai rekordu husi tabela
   ```sql
   DELETE FROM estudante WHERE naran = 'John Doe';
   ```

Klausa WHERE iha operasaun UPDATE no DELETE importante tebes atu espesifika rekordu sira ne'ebé tenke afetadu.

## 5. Konsulta Básiku ho SELECT

Deklarasaun SELECT uza atu hetan dadus husi tabela. Uza komun inklui:

1. Selesionaun koluna hotu:
   ```sql
   SELECT * FROM estudante;
   ```

2.