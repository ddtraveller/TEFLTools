'Unidade Aprendizajen 2

Unidade Aprendizajen 2: Modelu Rede no Protokolu
- Objetivu:
  * Hatene klean liu kona-ba modelu OSI no TCP/IP
  * Komprende funsaun husi kada kapa protokolu
- Topiku:
  * Kapa modelu OSI
  * Modelu TCP/IP
  * Protokolu komun (HTTP, FTP, SMTP)
- Atividade:
  * Kompara modelu OSI ho TCP/IP
  * Analiza pakote rede ho aplikasaun Wireshark (bainhira iha rekursu)

Unidade Rekursu

Notas Aula

Modelu OSI

Modelu OSI (Open Systems Interconnection) mak estrutura konseituál ne'ebé uza hodi deskreve funsaun husi sistema networking. Modelu ne'e uza kapa atu hatene vizuálmente kona-ba sistema networking ida-idak.

Kapa 7 husi Modelu OSI

1. Kapa Físiku
   - Trata kona-ba koneksaun físiku entre dispositivu
   - Defini spesifikasaun ba kabel, konektor, no kartu interface rede
   - Responsável ba transmisaun bit liu média físiku

2. Kapa Ligasaun Dadus
   - Fornese transferénsia dadus husi nodu ba nodu
   - Deteta no posivelmente korrige eror sira ne'ebé bele mosu iha kapa físiku
   - Defini oinsá dadus formatadu ba transmisaun no oinsá kontrola asesu ba rede

3. Kapa Rede
   - Fornese teknolojia routing no switching
   - Jere enderesu, monitorizasaun, no determina dalan di'ak liu ba transferénsia dadus

4. Kapa Transporte
   - Fornese transferénsia dadus transparante entre sistema final
   - Responsável ba rekuperasaun eror husi ponta ba ponta no kontrolu fluxu

5. Kapa Sesaun
   - Estabelese, jere, no termina koneksaun entre aplikasaun
   - Fornese operasaun full-duplex, half-duplex, ka simplex

6. Kapa Apresentasaun
   - Garante katak informasaun ne'ebé aplikasaun husi sistema ida haruka bele le'e husi aplikasaun husi sistema seluk
   - Jere enkripsaun dadus, kompresun, no konversaun formatu

7. Kapa Aplikasaun
   - Fornese servisu rede direta ba utilizador final ka aplikasaun
   - Inklui protokolu hanesan HTTP, FTP, SMTP, etc.

Enkapsulasaun iha Modelu OSI

Enkapsulasaun mak prosesu ne'ebé dadus sai pakote hanesan nia desse ba kapa OSI:
1. Dadus husi utilizador husi kapa aplikasaun desse ba kapa sira seluk
2. Kada kapa hatama informasaun header nia (no dalaruma informasaun trailer)
3. Iha tempu dadus to'o ba kapa físiku, nia enkapsula ona ba frame

Modelu TCP/IP

Modelu TCP/IP mak versaun prátika liu, kondensa husi modelu OSI, ne'ebé uza iha networking mundu real.

Kapa 4 husi Modelu TCP/IP

1. Kapa Aksesu Rede (kombina kapa Físiku no Ligasaun Dadus OSI)
   - Trata infraestrutura físika no oinsá dadus haruka liu rede

2. Kapa Internet (ekivalente ba kapa Rede OSI)
   - Jere enderesu no routing pakote dadus

3. Kapa Transporte (ekivalente ba kapa Transporte OSI)
   - Garante transmisaun dadus ne'ebé fiar

4. Kapa Aplikasaun (kombina kapa Sesaun, Apresentasaun, no Aplikasaun OSI)
   - Trata protokolu nivel as, representasaun, no funsaun kontrolu

Komparasaun ho Modelu OSI

- TCP/IP mak simples liu, kombina kapa balu OSI
- TCP/IP mak prátiku liu no uza barak