'Iha ne'e mak material suporta ba planu lição kona ba Konfigurasaun Rede no Seguransa, ne'ebé formatu iha Markdown:

# Material Suporta ba Lição Konfigurasaun Rede no Seguransa

## 1. Lista Vokabuláriu Prinsipál ho Definisaun

- **Endereçu IP**: Identifikadór numeriku únika ne'ebé atribui ba kada dispositivu iha rede komputador.
- **Máskara Subnet**: Númeru bit 32 ne'ebé kobre endereçu IP, divide ba parte rede no parte anfitriãun.
- **Gateway**: Nó rede ne'ebé serve hanesan pontu asesu ba rede seluk, hanesan ligasaun rede lokál ba internet.
- **Firewall**: Sistema seguransa rede ne'ebé monitoriza no kontrola tráfiku rede nian, hodi tama no sai.
- **SSH (Secure Shell)**: Protokolu rede kriptográfiku ba operasaun servisu rede ho seguransa iha rede inseguru.
- **iptables**: Programa utilidade espasu uza nian ne'ebé permite administrador sistema atu konfigura regras filtru pakote IP husi firewall kernel Linux nian.
- **firewalld**: Manejador firewall dinámiku ne'ebé uza zona atu maneja grupu regras ba nível konfiansa diferente.
- **Xave Públika**: Komponente ne'ebé bele fahe públikamente husi par xave kriptográfiku ne'ebé uza ba enkripsaun asimétrika.
- **Xave Privada**: Komponente segredu husi par xave kriptográfiku ne'ebé uza ba enkripsaun asimétrika.
- **Autentikasaun**: Prosesu verifika identidade uza nian ka sistema nian.

## 2. Ajuda Vizual ka Diagrama

1. Diagrama Konfigurasaun Rede:
   - Diagrama rede simples ne'ebé hatudu router, switch, no komputador balu.
   - Etiketa ba endereçu IP, máskara subnet, no gateway.
   - Seta hatudu fluxu tráfiku.

2. Diagrama Konseitu Firewall:
   - Reprezentasaun vizual husi firewall entre rede interna no internet.
   - Seta hatudu tráfiku ne'ebé permite no blokeia.
   - Íkon hatudu tipu diferensa tráfiku (web, email, etc.).

3. Gráfiku Fluxu Autentikasaun Xave SSH:
   - Gráfiku fluxu hatudu prosesu autentikasaun ba xave SSH.
   - Pasu sira inklui: jerasaun xave, distribuisaun xave públika, tentativa ligasaun, verifikasaun xave, no login susesu.

## 3. Folha Distribui ka Folla Traballu

1. Folha Trapaça Komandu Konfigurasaun Rede:
   - Lista komandu ip no nmcli komun ho esplikasaun badak.
   - Ezemplu kona-ba oinsá haree no define endereçu IP, máskara subnet, no gateway.

2. Folla Traballu Regras Firewall:
   - Tabela ba estudante atu kompleta ho koluna ba: Númeru Regra, Asaun (Permite/Nega), IP Fonte, IP destinasaun, Portu, no Protokolu.
   - Espasu ba estudante atu hakerek komandu iptables ka firewalld korespondente.

3. Guia Jerasaun no Konfigurasaun Xave SSH:
   - Instrusaun pasu-ba-pasu ba jerasaun par xave SSH.
   - Komandu ba kopia xave públika ba servidor remotu.
   - Pasu konfigurasaun atu desativa autentikasaun pasword iha SSH.

## 4. Rekursu Adisional ba Leitura ka Prátika Nafatin

1. Tutorial Online:
   - Série "Introdusaun ba Firewall Linux" husi DigitalOcean
   - Guia "Hahu ho firewalld" husi Red Hat

2. Livru:
   - "Guia Administrador Rede Linux" husi Tony Bautts, Terry Dawson, no Gregor N.