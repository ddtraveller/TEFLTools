"Iha ne'e mak material suporte ba lição kona-ba Sistema Logging no Monitoring, formatu iha Markdown:

# Material Suporte: Sistema Logging no Monitoring

## 1. Lista Vocabulário Prinsipál ho Definisaun

- **Syslog**: Protokolu padraun nebebé uza ba registu mensajen, ne'e permisi separasaun husi software nebebé prodús mensajen husi sistema nebebé armazena sira no software nebebé relata no analiza sira.
- **Journald**: Servisu sistema ida nebebé koleita no armazena dadus registu, fornese solusaun jestaun sentralizadu ba hotu sistema logging iha sistema Linux modernu.
- **Rotasaun Log**: Prosesu husi arkuivu no renova file log atu evita sira konsume espasu disk demais.
- **Karga Sistema**: Medida husi volume servisu komputasaun nebebé komputador halo.
- **Operasaun I/O**: Operasaun Input/Output, refere ba komunikasaun entre komputador ho nia uza-na'in, ka entre komputador ho nia periferiku sira.
- **grep**: Utilidade linha komandu ba buka iha data set testu simples ba linhas nebebé kombina ho espresaun regular.
- **awk**: Lingua programasaun nebebé dezenvolve ba prosesamentu testu no normalmente uza hanesan ferramenta extrasaun dadus no relatoriu.
- **sed**: Editor fluxu ba filtra no transforma testu.
- **top/htop**: Visualizador prosesu interaktivu nebebé hatudu informasaun sistema no prosesu sira nebebé halo hela.
- **iotop**: Ferramenta ba monitorizasaun uzu I/O husi prosesu sira.
- **vmstat**: Ferramenta ida nebebé hatudu estatistika memoria virtual.

## 2. Ajuda Visual ka Diagrama

1. **Diagrama Estrutura File Log**
   Deskrisaun: Diagrama fluxu nebebé hatudu estrutura tipika husi file log, inklui timestamp, nivel gravidade, ID prosesu, no komponente mensajen.

2. **Dashboard Monitorizasaun Sistema**
   Deskrisaun: Mock-up ida husi dashboard monitorizasaun sistema, nebebé hatudu metrica prinsipal sira hanesan uzu CPU, uzu memoria, disk I/O, no atividade rede.

3. **Fluxu Trabalho Analiza Log**
   Deskrisaun: Diagrama nebebé ilustra prosesu analiza log, husi gerasaun log to'o koleksaun, prosesamentu, no analiza/relatoriu final.

## 3. Folha Distribuisaun ka Worksheet

1. **Folha Referensia Kona-ba Analiza Log**
   Konteudu: Gia referensia rapidu ba komandu analiza log komun sira uza grep, awk, no sed, ho ezemplu ba kada ida.

2. **Worksheet Ezersisiu Monitorizasaun Sistema**
   Konteudu: Worksheet ho senario sira nebebé rekeri estudante sira atu interpreta output husi top/htop no sujere otimizasaun bazeia ba dadus.

3. **Gia Konfigurasaun Logging Personalizadu**
   Konteudu: Instrusaun pasu-ba-pasu ba konfigurasaun logging personalizadu ba servidor web, inklui pedasu konfigurasaun amostra.

## 4. Rekursu Adisional ba Leitura ka Pratika Adisional

1. Projetu Dokumentasaun Linux: Logging
   https://tldp.org/HOWTO/Logging-HOWTO/

2. Dokumentasaun Linux Red Hat Enterprise 8: Konfigurasaun no jestaun logging
   https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_logging/index

3. Jornal Linux: Monitorizasaun Sistema ho Sysstat
   https://www.linuxjournal.com/content/system-monitoring-sysstat

4. Tutorial DigitalOcean: Oinsa Uza Journalctl atu Haree no Manipula Logs Systemd
   https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs

5. Repos