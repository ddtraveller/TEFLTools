'# PostgreSQL Basics: Introdusaun ba Jestaun Relational Database

## Introdusaun
PostgreSQL mak sistema jestaun database relacional (RDBMS) ne'ebé opensource, poderoso no konhesidu ba nia robuteza, extensibilidade, no kumpre ho padraun SQL. PostgreSQL oferese konjuntu funsaun ne'ebé riku, inklui suporta ba tipu dadus avansadu, konsulta kompleksu, no transasaun, hodi sai hanesan opsaun populár ba aplikasaun sira ne'ebé presiza solusaun database ne'ebé fiar no bele aumenta.

Iha papel ida ne'e, ita sei introduz konseitu fundamentál sira husi PostgreSQL, inklui nia interface linha komandu, tipu dadus, jestaun database no tabela, no operasaun SQL báziku. Ho komprende konseitu sira ne'e, uza-na'in bele kria, jestaun, no konsulta database hodi uza PostgreSQL.

## 1. Navegasaun husi Interface Linha Komandu PostgreSQL (psql)
Interface linha komandu PostgreSQL, ne'ebé hanaran `psql`, mak ferramenta poderoso ba interasaun ho database PostgreSQL. Psql permite uza-na'in atu ezekuta komandu SQL, haree rezultadu konsulta, no jestaun database diretamente husi linha komandu.

Atu hahu `psql`, loke terminal no hakerek:

```bash
psql -U username -d database_name
```

Troka `username` ho ita-nia username PostgreSQL no `database_name` ho naran husi database ne'ebé ita hakarak konekta. Ita sei hetan pedidu atu hakerek password ba uza-na'in ne'ebé ita hatama.

Hafoin konekta ona, ita bele uza komandu `psql` oioin atu navega no inspesiona estrutura database. Komandu importante balun mak hanesan:

- `\l`: Lista database hotu iha instansia PostgreSQL. Komandu ida ne'e fornese vizualizasaun husi database ne'ebé eziste, inklui sira-nia donu no informasaun enkodigasaun.

- `\c database_name`: Konekta ba database espesífiku. Troka `database_name` ho naran husi database ne'ebé ita hakarak muda ba. Komandu ida ne'e permite ita atu muda database ne'ebé ita servisu iha sesaun `psql`.

- `\dt`: Lista tabela hotu iha database atual. Komandu ida ne'e hatudu naran tabela, inklui sira-nia donu no tablespace ne'ebé sira pertense. Nune'e ita bele haree estrutura husi database.

- `\d table_name`: Deskreve estrutura husi tabela espesífiku. Troka `table_name` ho naran husi tabela ne'ebé ita hakarak inspesiona. Komandu ida ne'e hatudu naran koluna, tipu dadus, restrisaun, no atributu seluk husi tabela, ajuda ita atu komprende nia estrutura no relasaun.

- `\q`: Sai husi sesaun `psql`. Uza komandu ida ne'e bainhira ita hotu ona servisu ho database no hakarak sai husi interface linha komandu.

Ezemplu:
```psql
postgres=# \l
                                  Lista husi database sira
   Naran    |  Na'in   | Encoding |   Collate   |    Ctype    |   Priviléjiu Aksesu
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 eskola    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(4 linhas)

postgres=# \c eskola
Agora ita

Husi forma automática, kria identifikadór únika ida ba kada empregadu.
- Koluna `name` define ona hanesan `VARCHAR(100)`, ne'ebé permite armazenamentu naran empregadu nian to'o karakter 100.
- Koluna `email` mós define ona hanesan `VARCHAR(100)` no iha `UNIQUE` constraint atu asegura katak kada email mak únika.
- Koluna `hire_date` define ona hanesan `DATE` atu armazena loron servisu empregadu nian.
- Koluna `salary` define hanesan `NUMERIC(10,2)`, ne'ebé permite armazenamentu saláriu ho díjitu to'o 10, inklui desimál 2.
- Koluna `is_active` define hanesan `BOOLEAN` atu hatudu se empregadu mak ativu ka lae.

Hili tipu dadus ne'ebé apropriadu ba kada koluna ajuda atu mantein integridade dadus, otimiza armazenamentu, no fasilidade iha búskedas efisiente no manipulasaun dadus. Importante atu konsidera natureza husi dadus, intervalu husi valores, no presizaun ne'ebé presiza bainhira hili tipu dadus ba koluna tabela nian.

## 3. Kria no Jere Bazadadus no Tabela
Iha PostgreSQL, bazadadus mak recipientes iha nível leten ne'ebé rai hotu-hotu dadus no objetu bazadadus, hanesan tabela, índise, no views. Tabela sira mak estrutura fundamentál iha bazadadus ne'ebé dadus atual armazena no organiza.

Atu kria bazadadus foun iha PostgreSQL, bele uza komandu `CREATE DATABASE`:

```sql
CREATE DATABASE school;
```

Komandu ida-ne'e kria bazadadus foun ho naran `school`. bele muda `school` ho naran ne'ebé ita hakarak ba bazadadus.

Ha'u iha ona bazadadus, bele kria tabela iha laran ho komandu `CREATE TABLE`. Komandu `CREATE TABLE` permite atu define estrutura husi tabela, espesifika naran koluna, tipu dadus, no kualke restriksaun ka propriedade adisionál.

Ezemplu ida kria tabela ho naran `students`:

```sql
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE,
  birth_date DATE,
  gpa NUMERIC(3,2)
);
```

Hatu'un diferensia parte husi komandu `CREATE TABLE`:

- `id SERIAL PRIMARY KEY`: Linha ida-ne'e kria koluna ho naran `id` ho tipu dadus `SERIAL`. Tipu dadus `SERIAL` kria númeru sekueńsial únika ida ba kada liña foun ne'ebé insere iha tabela. Restriksaun `PRIMARY KEY` asegura katak koluna `id` identifika liña únika iha tabela.

- `name VARCHAR(100) NOT NULL`: Linha ida-ne'e kria koluna ho naran `name` ho tipu dadus `VARCHAR(100)`, ne'ebé permite armazenamentu naran to'o karakter 100. Restriksaun `NOT NULL` asegura katak tenke iha valór ba koluna `name` iha kada liña.

- `email VARCHAR(100) UNIQUE`: Linha ida-ne'e kria koluna ho naran `email` ho tipu dadus `VARCHAR(100)`. Restriksaun `UNIQUE` asegura katak kada enderezu email iha tabela mak únika, atu evita entrada email duplikadu.

- `birth_date DATE`: Linha ida-ne'e kria koluna ho naran `birth_date` ho tipu dadus `DATE` atu armazena data moris estudante nian.

- `gpa NUMERIC(3,2)`: Linha ida-ne'e kria koluna ho naran `gpa` ho tipu dadus `NUMERIC(3,2)`, ne'ebé permite armazenamentu valór média ho díjitu to'o 3

'Baseia ba kondisaun espesifiku.

   Hanesan ezemplu ida husi hamoos rejistu estudante ho naran espesifiku:

   ```sql
   DELETE FROM students WHERE name = 'John Doe';
   ```

   Iha deklarasaun ne'e, ami mensiona naran tabela (`students`) no usa `WHERE` hodi hatudu kondisaun ne'ebé determina rejistu(s) ne'ebé tenke hamoos. Iha kazu ne'e, nia hamoos rejistu estudante naran 'John Doe'.

   Hanesan `UPDATE`, tenke kuidadu bainhira uza `DELETE` la ho `WHERE`, tanba sei hamoos hotu rejistu sira husi tabela.

Ezemplu:
```sql
-- Hakerek estudante foun
INSERT INTO students (name, email, birth_date, gpa)
VALUES ('Sarah Thompson', 'sarah@example.com', '2002-07-10', 3.95);

-- Halo mudansa ba email estudante
UPDATE students
SET email = 'sarahthompson@example.com'
WHERE name = 'Sarah Thompson';

-- Hamoos rejistu estudante
DELETE FROM students
WHERE id = 5;
```

Iha ezemplu ne'e, ami promeiro hakerek rejistu estudante foun ba tabela `students`. Depois atualiza email estudante naran 'Sarah Thompson'. Iha final, ami hamoos rejistu estudante ho `id` igual ba 5.

Operasaun manipulasaun dadus (`INSERT`, `UPDATE`, `DELETE`) importante tebes ba jestaun dadus ne'ebé armazenadu iha tabela PostgreSQL. Sira permite ita atu hakerek rejistu foun, modifika dadus ezistente, no hamoos rejistu sira ne'ebé la presiza baseia ba kondisaun espesifiku. Importante tebes atu uza operasaun sira ne'e ho kuidadu no asegura katak kondisaun apropriadu especificadu hodi mantein integridade dadus no evita modifikasaun ka eliminasaun sira ne'ebé la iha intensaun.

## 5. Konsulta Báziku ho SELECT
Declarasaun `SELECT` mak ida husi declarasaun SQL importante liu no uza barak iha PostgreSQL. Nia permite ita atu hetan dadus husi ida ka tabela liu tan bazeia ba kritéria espesifiku. Sintax báziku husi declarasaun `SELECT` hanesan tuir mai:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

Ami sei explika tiha ona parte sira diferente husi declarasaun `SELECT`:

1. Hili koluna hotu:
   Atu hetan koluna hotu husi tabela, bele uza karakter asterisk (`*`) iha kláusula `SELECT`.

   ```sql
   SELECT * FROM students;
   ```

   Declarasaun ne'e hili koluna hotu husi tabela `students` no fila hotu rejistu sira.

2. Hili koluna espesifika:
   Karik ita presiza de'it koluna espesifika husi tabela, bele lista sira ida-idak iha kláusula `SELECT`.

   ```sql
   SELECT name, gpa FROM students;
   ```

   Declarasaun ne'e hili de'it koluna `name` no `gpa` husi tabela `students`.

3. Filtra rezultadu ho WHERE:
   Kláusula `WHERE` permite ita atu esplika kondisaun hodi filtra rezultadu bazeia ba kritéria espesifiku.

   ```sql
   SELECT name, gpa FROM students WHERE gpa > 3.5;
   ```

   Declarasaun ne'e hili koluna `name` no `gpa` husi tabela `students` ba rejistu sira ne'ebé `gpa` liu 3.5.

4. Ordema rezultadu:
   Bele uza kláusula `ORDER BY` hodi ordema rezultadu bazeia ba koluna ida ka liu tan. Default, ordem sei asendente. Bele uza `DESC` ba ordem desendente.

   ```sql
   SELECT name, gpa FROM students ORDER BY gpa DESC;
   ```