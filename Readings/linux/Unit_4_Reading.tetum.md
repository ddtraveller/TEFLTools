'Jestaun Uzuáriu no Grupu iha Sistema Linux

Introdusaun

Jestaun uzuáriu no grupu mak aspetu fundamentál husi administrasaun sistema Linux. Nia fornese estrutura ba organizasaun no kontrolu asesu ba rekursu sistema, asegura seguransa, no fasilidade kolaborasaun entre uzuáriu sira. Iha papel ida ne'e, ami esplora kona-ba konseitu uzuáriu no grupu iha Linux, diskute kona-ba ferramenta jestaun esensiál, no salienta prátika di'ak liu ba implementasaun polítika uzuáriu no grupu efetivu.

Hahú Komprende Uzuáriu no Grupu

Iha Linux, uzuáriu mak entidade ida ne'ebé bele interage ho sistema no iha ficheiro rasik. Kada uzuáriu iha identifikador úniku (UID) no normalmente reprezenta ema ida individual ka servisu sistema ida. Uzuáriu sira bele log in, ezekuta komandu, no asesu rekursu tuir sira nia permissaun ne'ebé atribuí.

Grupu, iha parte seluk, mak koleksaun husi uzuáriu sira ne'ebé fahe direitu asesu komún. Sira simplifika prosesu atribuisaun permissaun ba uzuáriu barak iha tempu hanesan. Kada grupu iha identifikador grupu únika (GID), no uzuáriu sira bele pertense ba grupu ida ka liu.

Relasaun entre uzuáriu no grupu define iha ficheiro sistema rua ne'ebé importante: /etc/passwd no /etc/group. Ficheiro /etc/passwd kontein informasaun importante kona-ba kada uzuáriu, inklui sira nia username, UID, grupu primáriu, direktóriu uma, no shell default. Ficheiro /etc/group lista grupu hotu iha sistema, sira nia GID, no sira nia membru.

Komandu Jestaun Uzuáriu

Linux fornese komandu linha ferramenta balu ba jestaun uzuáriu no grupu. Komandu primáriu ba jestaun uzuáriu mak:

1. useradd: Kria konta uzuáriu foun
2. usermod: Muda konta uzuáriu ne'ebé eziste ona
3. userdel: Hapus konta uzuáriu

Hanesan ezemplu, atu kria uzuáriu foun ho naran "john," administrador ida tenke uza:

useradd -m -s /bin/bash john

Komandu ida ne'e kria uzuáriu "john" ho direktóriu uma (-m) no define shell default ba bash (-s /bin/bash).

Atu muda konta uzuáriu, hanesan atu tau sira iha grupu foun, komandu usermod uza:

usermod -aG developers john

Komandu ida ne'e tau "john" iha grupu "developers" la halo nia sai husi grupu seluk.

Jestaun password halo tuir parte ho komandu passwd:

passwd john

Komandu ida ne'e husu atu tau password foun ba uzuáriu "john."

Jestaun Grupu

Parese ho jestaun uzuáriu, Linux fornese komandu ba jestaun grupu:

1. groupadd: Kria grupu foun
2. groupmod: Muda grupu ne'ebé eziste ona
3. groupdel: Hapus grupu

Hanesan ezemplu, atu kria grupu foun ho naran "marketing":

groupadd marketing

Uzuáriu sira bele tau iha grupu liu husi komandu usermod ne'ebé hateten iha leten ka liu husi edita ficheiro /etc/group diretamente.

Sudo no Asesu Administrativu

Komandu sudo mak ferramenta ida ne'ebé poderózu ne'ebé permite uzuáriu sira ezekuta komandu ho priviléji