'# ## Unidade Aprendizajen 2

## Unidade Aprendizajen 2: Navegasaun no Jestaun Sistema Arkivu
- Objetivu:
  * Dominia navegasaun no manipulasaun sistema arkivu
  * Komprende permissaun no propriedade arkivu
- Topiku:
  * Hierarkia sistema arkivu Linux
  * Komandu manipulasaun arkivu (cp, mv, rm, etc.)
  * Konseitu permissaun no propriedade arkivu
- Atividade:
  * Kria estrutura diretoriu ba projetu simuladu
  * Defini permissaun apropriadu ba papel uzuariu diferente

## Rekursu Unidade

# Nota Leksaun

## Hierarkia Sistema Arkivu Linux

### Introdusaun
- Sistema arkivu Linux organiza iha estrutura ai-hun hierarkia
- Iha Linux, buat hotu konsidera hanesan arkivu, inklui diretoriu no ekipamentu 
- Diretoriu root (/) maka diretoriu nivel leten, husi ne'ebe diretoriu hotu-hotu seluk sai

### Diretoriu Xave
1. / (root):
   - Diretoriu nivel leten
   - Diretoriu no arkivu hotu-hotu iha laran ne'e

2. /home:
   - Kondesa diretoriu home uzuariu
   - Kada uzuariu normalmente iha sira-nia subdiretoriu rasik (ex., /home/username)

3. /etc:
   - Arkivu konfigurasaun sistema
   - Kondesa seting ba aplikasaun no servisu iha nivel sistema

4. /var:
   - Arkivu dadus variavel
   - Inklui arkivu log, arkivu temporariu, no diretoriu spool

5. /usr:
   - Binariu uzuariu, biblioteka, dokumentasaun, no kodigu fonte
   - Kondesa aplikasaun no utilidade maioria ne'ebe uzuariu uza

6. /tmp:
   - Arkivu temporariu
   - Kontein normalmente klean iha reboot sistema

### Komandu Navegasaun
- pwd: Imprime Diretoriu Servisu
- cd: Muda Diretoriu
- ls: Lista kontein diretoriu

## Komandu Manipulasaun Arkivu

### cp (kopia)
- Sintaxe: cp [opsoens] fonte destinu
- Ezemplu:
  - cp file1 file2
  - cp -r dir1 dir2 (kopia rekursivu ba diretoriu)

### mv (muda/rename)
- Sintaxe: mv [opsoens] fonte destinu
- Ezemplu:
  - mv file1 file2 (troka naran file1 ba file2)
  - mv file1 /dalanto/diretoriu/ (muda file1 ba diretoriu espesifikadu)

### rm (hasai)
- Sintaxe: rm [opsoens] arkivu(s)
- Ezemplu:
  - rm file1
  - rm -r diretoriu (hasai rekursivu ba diretoriu)

### mkdir (kria diretoriu)
- Sintaxe: mkdir [opsoens] naran_diretoriu
- Ezemplu: mkdir diretoriu_foun

### touch (kria arkivu mamuk)
- Sintaxe: touch naran_arkivu
- Ezemplu: touch arkivu_foun.txt

## Permissaun no Propriedade Arkivu

### Komprende Permissaun
- Tinan tolu: le (r), hakerek (w), ezekuta (x)
- Kategoria tolu: uzuariu (u), grupu (g), seluk (o)
- Reprezenta hanesan: rwxrwxrwx

### Hare Permissaun
- Uza komandu ls -l
- Output ezemplu: -rw-r--r-- 1 uzuariu grupu 4096 Jan 1 12:00 file.txt

### Troka Permissaun
- Komandu chmod
- Sintaxe: chmod [opsoens] modu arkivu(s)
- Ezemplu:
  - chmod u+x file.txt (tau permissaun ez