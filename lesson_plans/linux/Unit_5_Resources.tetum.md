'## Unidade Aprendizajen 5

## Unidade Aprendizajen 5: Sistema Logging no Monitorizasaun
- Objetivu:
  * Komprende sistema logging Linux nian
  * Aprende atu monitoriza saúde no desempeño sistema nian
- Tópiku:
  * Syslog no journald
  * Folinha análise log nian
  * Utilidade monitorizasaun sistema nian
- Atividade:
  * Analiza fail log atu halo troubleshoot problema sistema nian
  * Konfigura logging personalizadu ba aplikasaun ida-idak

## Rekursu Unidade

# Nota Palestra

## Introdusaun ba Sistema Logging

### Finalidade husi Sistema Logging
- Fornese rejistu kona-ba eventu no atividade sistema nian
- Importante tebes ba troubleshoot, auditoria seguransa, no análise desempeño
- Ajuda kumpri regulamentu no polítika

### Protocolo Syslog
- Protocolo padrãun ba logging mensajen 
- Permite separasaun entre software ne'ebé produz mensajen husi sistema ne'ebé armazena sira
- Normalmente uza portu 514 ba UDP (historikamente) ka 6514 ba TCP ho TLS

### Journald
- Parte ida husi systemd, jestor servisu no sistema ba Linux
- Koleita no armazena dadus log iha formatu estruturadu, indexadu
- Fornese kapasidade konsulta ne'ebé maka'as

### Atu haree Logs
- Fail log tradisionál: normalmente armazenadu iha /var/log/
- Komandu Journalctl: uza atu konsulta no hatudu logs husi journald

## Folinha Análise Log

### Grep
- Buca testu uza padrãun
- Sintaxe básiku: `grep [opsaun] padrãun [fail...]`
- Opsaun útil:
  - `-i`: buka insensivel ba kazu
  - `-v`: inverte kombinasaun (hatudu linhas ne'ebé la kombina)
  - `-r`: buka rekursivu iha diretóriu

### Awk
- Folinha prosesamentu testu ne'ebé maka'as
- Kapas buka no transforma testu
- Sintaxe básiku: `awk 'padrãun {asaun}' [fail...]`
- Útil ba extrai kampu espesífiku husi entrada log nian

### Sed
- Editor fila ba filtru no transforma testu
- Sintaxe básiku: `sed [opsaun] 'komandu' [fail...]`
- Normalmente uza ba operasaun buka no troka

## Monitorizasaun Sistema

### Top/Htop
- Espektadór prosesu interativu
- Hatudu sumáriu sistema no lista prosesu
- Informasaun Xave:
  - Uzu CPU nian
  - Uzu Memória nian
  - Media karga

### Iotop
- Folinha monitorizasaun I/O nian
- Hatudu informasaun uzu I/O ba prosesu
- Útil ba identifika prosesu ne'ebé kauza atividade disk a'as

### Vmstat
- Hatudu informasaun kona-ba prosesu, memória, paging, block I/O, traps, no atividade CPU
- Fornese visãun konzisa kona-ba desempeño sistema nian

# Kestaun Diskusaun

1. Tanba sistema logging importante ba administrador sistema no uzuáriu regulár?
2. Oinsá protocolo syslog difere husi journald? Saida mak vantajen no dezvantajen ida-idak nian?
3. Iha situasaun sira ne'ebé mak ita uza grep liu awk ka sed, no ho versa?
4. Oinsá folinha monitorizasaun sistema bele ajuda identifika no resolve problema desempeño?
5. Saida konsiderasaun étiku sira ne'ebé administrador sistema tenke konsidera bainhira halo logging no monitorizasaun atividade uzuáriu nian?

# Instrusaun Ezersísiu Hakerek

## Ezersísiu