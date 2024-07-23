'Plano Aula: Sistema Logging no Monitorização

## 1. Recursos Precisa

- Máquinas Linux ka máquinas virtuais ba kada estudante
- Acesso ba ficheiros de sistema (ex: /var/log/)
- Editores de texto (ex: nano, vim)
- Ferramentas de monitorização (ex: htop, iotop)
- Projetor ba demonstrações

## 2. Objetivos Aula

Iha remata aula nee, estudantes sei bele:
- Esplika objetivu no importância husi sistema logging
- Navega no interpreta ficheiros de log comum
- Uza ferramentas básicas análise de log
- Configura logging personalizado ba aplicações
- Monitoriza saúde no performansia sistema uza ferramentas linha de comando

## 3. Atividade Aquecimento (10 minutos)

- Diskusaun grupu: "Tanba sistema logging importante? Eventos sira neebé ita hakarak log?"
- Haree resposta sira iha quadro no diskute hanesan klase

## 4. Ensina Vocabulário Importante (10 minutos)

- Introduz no esplika termos chave:
  - Syslog
  - Journald
  - Rotação de log
  - Carga sistema
  - Operações I/O

## 5. Conteúdo Principal Aula (40 minutos)

### A. Introdução ba Sistema Logging (15 minutos)
- Esplika protocolo syslog no nia importância
- Diskute função de journald iha sistema Linux moderno
- Demonstração oinsá atu haree logs uza journalctl no ficheiros de log tradisional

### B. Ferramentas Análise de Log (15 minutos)
- Introduz ferramentas análise de log comum:
  - grep
  - awk
  - sed
- Demonstração técnicas básicas ba buka no filtra log

### C. Monitorização Sistema (10 minutos)
- Introduz ferramentas chave ba monitorização sistema:
  - top/htop
  - iotop
  - vmstat
- Esplika oinsá atu interpreta resultadu husi ferramentas sira nee

## 6. Atividades Prática (30 minutos)

### A. Exercício Análise de Log (15 minutos)
- Fornese estudantes ho ficheiro de log amostra ho eventos variados
- Husu sira atu uza grep, awk, no sed atu extrai informação específica

### B. Exercício Monitorização Sistema (15 minutos)
- Husu estudantes atu uza top/htop atu identifika prosesu ne'ebé uza recursos barak
- Husu sira atu interpreta resultadu no sugere otimizações possíveis

## 7. Tarefa Produção (30 minutos)

- Senário: "O ita-boot administrador sistema ba kompanhia alojamento web ki'ik. Configura logging personalizado ba servidor web no kria script shell simples atu monitoriza nia performansia."
- Estudantes tenke:
  1. Configura logging personalizado ba servidor web Apache ka Nginx
  2. Hakerek script shell ne'ebé verifica carga servidor no regista avisos se ultrapassa limite

## 8. Konklusão no Revisão (10 minutos)

- Recapitula pontos importante husi aula
- Responde duvida ka preokupasaun sira
- Preve aula tuir mai kona-ba básico script shell

## 9. Tarefa Uma

1. Analiza auth.log ka secure log iha sistema ita-boot. Hakerek relatório badak kona-ba:
   - Tentativa autenticação falha
   - Uso suksesu sudo
   - Evento segurança seluk ne'ebé interesa

2. Kria script shell simples ne'ebé verifica carga sistema kada 5 minutos no adisiona resultadu ba ficheiro de log personalizado.

## 10. Definições Vocabulário Chave

- Syslog: Padrão ba mensajen logging, separa software ne'ebé gera mensajen husi sistema ne'ebé armazena sira no software ne'ebé relata no analiza sira.
- Journald: Serviço sistema ne'ebé kokoleta no armazena data logging, fornese solusaun gestão centralizada ba logging sistema tomak.