'## Unidade Aprendizajen 3: Jestaun Prosesu
- Objetivu:
  * Komprende konseitu prosesu iha Linux
  * Aprende atu monitoriza no kontrola prosesu
- Topikus:
  * Estadu prosesu no siklu vida
  * Folin monitorizasaun prosesu (ps, top, htop)
  * Kontrolu servisu no prosesu iha latar
- Atividades:
  * Hakerek skript shell ida atu monitoriza prosesu sistema
  * Eskperimenta ho servisu laran no kontrollu iha latar

## Rekursu Unidade

# Nota Palestra

## Introdusaun ba Prosesu

### Saidas mak Prosesu?
- Prosesu mak instansia ida husi programa ne'ebe tama ona iha prosesu halao
- Kada prosesu iha ninia espasu memoria rasik no rekursu sistema
- Prosesu sira jestaun husi kernel Linux

### Estadu Prosesu
1. Tama ona: Atualmente halao iha CPU
2. Durmi: Hein ba rekursu ka eventu
3. Para: Suspende, normalmente husi signal ida
4. Zombie: Remata ona maibe sei iha entrada ida iha tabela prosesu

### Atributu Prosesu
- Prosesu ID (PID): Identifikadór únika ba kada prosesu
- Parent Prosesu ID (PPID): ID husi prosesu ne'ebe kria nia
- User ID (UID): Nain ba prosesu
- Prioridade: Determina ordem ba eskedulamentu

## Folin Monitorizasaun Prosesu

### Komandu ps
- Sintaxe básiku: `ps [opsoens]`
- Opsoens komuns:
  - `ps aux`: Hatudu prosesu hotu-hotu husi uza-na'in hotu
  - `ps -ef`: Lista iha formatu tomak
  - `ps -u username`: Hatudu prosesu husi uza-na'in ida espesífiku

### Komandu top
- Haree prosesu sistema iha tempu real, dinamiku
- Atualiza periodikamente (default: kada 3 segundos)
- Komandu interativa:
  - 'q': Sai
  - 'k': Oho prosesu ida
  - 'r': Renice prosesu ida

### Komandu htop
- Versaun avansadu husi top
- Kódigu kolor, interface amigu uza-na'in
- Karaterístika adisionál:
  - Haree prosesu iha forma ai-han
  - Skrol horizontál no vertikál
  - Suporta rato

## Kontrolu Servisu

### Prosesu iha oin kontra prosesu iha latar
- Prosesu iha oin: Prosesu ne'ebe kontrola terminal
- Prosesu iha latar: Prosesu halao laho kontrolu terminal diretu

### Komandu Kontrolu Servisu
- `jobs`: Lista servisu atual
- `bg [servisu_spec]`: Hadiak servisu ba latar
- `fg [servisu_spec]`: Hadiak servisu ba oin
- `&`: Hala'o komandu iha latar

### Prioridade Prosesu
- Valór Nice halao husi -20 (prioridade as) to'o 19 (prioridade ki'ik liu)
- Valór Nice default mak 0
- Komandu `nice`: Hahu prosesu ho valór Nice espesífiku
- Komandu `renice`: Muda valór Nice husi prosesu ne'ebe tama ona

# Kestaun Diskusaun

1. Oinsa konseitu prosesu relasiona ho aplikasaun ne'ebe ita uza loron-loron iha ita-nia komputador?
2. Tanba importante atu monitoriza prosesu sistema? Saidas mak problema potensial ne'ebe bele identifika liuhusi monitorizasaun prosesu?
3. Oinsa ita bele uza kontrolu servisu iha situasaun mundu real? Fó ezemplu ida.
4. Saidas mak konsiderasaun ét