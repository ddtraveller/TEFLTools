'## Unidade Aprendizajen 4

## Unidade Aprendizajen 4: Jestaun Uza-na'in no Grupu
- Objetivus:
  * Aprende atu jere uza-na'in no grupus
  * Komprende autentikasaun uza-na'in no sudo
- Tópikus:
  * Konseitu uza-na'in no grupu
  * Komandus jestaun uza-na'in (useradd, usermod, userdel)
  * Konfigurasaun sudo no pratika di'ak liu
- Atividades:
  * Monta kontas uza-na'in ba senáriu eskritóriu ki'ik
  * Konfigura asesu sudo ba tarefas administrativas espesífiku

## Rekursu Unidade

# Nota Palestra

## Konseitu Uza-na'in no Grupu

### Uza-na'in iha Linux
- Definisaun: Uza-na'in maka entidade ida ne'ebé bele asesu no interaje ho sistema 
- Kada uza-na'in iha identifikador úniku (UID) no naran uza-na'in
- Uza-na'in sira bele iha rasik ficheirus no prosesu
- Informasaun uza-na'in armazena iha /etc/passwd

### Grupu iha Linux
- Definisaun: Grupu maka kolesaun husi uza-na'in sira ho permissaun sira ne'ebé partilha
- Kada grupu iha identifikador úniku (GID) no naran grupu
- Uza-na'in sira bele pertense ba grupu barak
- Grupu primáriu kontra grupu suplementar
- Informasaun grupu armazena iha /etc/group

### Relasaun entre Uza-na'in no Grupu
- Kada uza-na'in pertense ba minimu grupu ida (grupu primáriu)
- Uza-na'in sira bele sai membru husi grupu barak
- Grupus uza ona ba organiza uza-na'in no jere permissaun
- Ezemplu: uza-na'in hotu iha grupu "developers" bele iha asesu ba diretóriu projetu ida-idak

### Estrutura husi /etc/passwd
- Formatu: username:x:UID:GID:GECOS:home_directory:shell
- Ezemplu: john:x:1001:1001:John Doe:/home/john:/bin/bash
- Explikasaun kampu:
  * username: Naran login
  * x: Espasu vaziu ba password enkriptadu (armazena iha /etc/shadow)
  * UID: Númeru ID uza-na'in
  * GID: Númeru ID grupu primáriu
  * GECOS: Naran kompletu no detallu sira seluk
  * home_directory: Diretóriu uma uza-na'in
  * shell: Shell default ba uza-na'in

### Estrutura husi /etc/group
- Formatu: group_name:x:GID:user_list
- Ezemplu: developers:x:1002:john,jane,bob
- Explikasaun kampu:
  * group_name: Naran grupu
  * x: Espasu vaziu ba password grupu (raramente uza)
  * GID: Númeru ID grupu
  * user_list: Lista uza-na'in sira iha grupu, separa ho vírgula

## Komandus Jestaun Uza-na'in

### useradd
- Objetivu: Kria konta uza-na'in foun
- Sintaxe báziku: useradd [opsoins] username
- Opsoins komuns:
  * -m: Kria diretóriu uma
  * -s: Espesifika shell login
  * -G: Aumenta ba grupus suplementares
- Ezemplu: useradd -m -s /bin/bash -G developers john

### usermod
- Objetivu: Muda konta uza-na'in ezistente
- Sintaxe báziku: usermod [opsoins] username
- Opsoins komuns:
  * -l: Muda naran uza-na'in
  * -g: Muda grupu primáriu