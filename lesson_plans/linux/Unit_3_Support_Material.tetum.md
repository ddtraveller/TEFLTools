Iha ne'e material apoiu ba lição kona-ba Jestaun Prosesu iha Linux, ne'ebe formatu iha Markdown:

# Material Apoiu ba Jestaun Prosesu iha Linux

## 1. Lista Vocabuláriu Prinsipál ho Definisaun

- **Prosesu**: Instánsia ida husi programa ne'ebé halai iha Linux.
- **PID (Prosesu ID)**: Numeru ida identifikadór únika ne'ebé atribui ba kada prosesu.
- **Servisu iha Oin**: Prosesu ida ne'ebé iha kontrolu direitu husi terminal no simu input husi uza-na'in.
- **Servisu iha Kotuk**: Prosesu ida ne'ebé halai la ho kontrolu direitu husi terminal, ne'ebé permite prosesu seluk atu halai iha tempu hanesan.
- **Valor Nice**: Númeru ida ne'ebé influénsia prioridade ba prosesu nia agenda, varia husi -20 (prioridade aas) ba 19 (prioridade ki'ik).
- **Prosesu Zombie**: Prosesu ida ne'ebé remata ona maibé nafatin iha entrada iha tabela prosesu.
- **Daemon**: Prosesu iha kotuk ne'ebé halai kontinuamente, hirak ne'ebé ofrese servisu ba prosesu sira seluk.
- **Thread**: Prosesu ki'ik ne'ebé fahe rekursu ho prosesu ina-aman nia.
- **Muda Kontestu**: Akto ida husi salva estadu prosesu ida no karga estadu salva husi prosesu seluk.
- **Estadu Prosesu**: Kondisaun atual husi prosesu (exemplu, halai, durmi, para, zombie).

## 2. Ajuda Visual ka Diagrama

1. Diagrama Siklu Prosesu:
   - Gráfiku fluxu ne'ebé hatudu estadu prosesu (Foun, Prontu, Halai, Hela, Remata)
   - Seta entre estadu sira ne'ebé hatudu tranzisaun posível

2. Ai-hun Hierarkia Prosesu:
   - Estrutura ai-hun ne'ebé hatudu relasaun entre prosesu ina ho oan
   - Rai husi ai-hun mak prosesu inicial (PID 1)
   - Dalan hatudu oinsá prosesu kria prosesu oan

3. Esplikasaun Output Husi Komandu Top:
   - Screenshot ida ne'ebé hatudu output husi komandu top
   - Anotasaun sira ne'ebé esplica kampu importante hanesan PID, UZA-NA'IN, %CPU, %MEM, KOMANDU

## 3. Material Distribui ka Ficha Trabalhu

1. Folha Fraude Husi Komandu Jestaun Prosesu:
   - Tabela ida ne'ebé lista komandu importante (ps, top, htop, kill, nice, renice) ho opsaun komun no deskrisaun badak

2. Ficha Ezplorasaun Prosesu:
   - Instrusaun husi pasu ba pasu ba estudante sira atu identifika no rejista informasaun kona-ba prosesu sistema importante
   - Tabela sira-ne'ebé estudante sira bele preenxe ho informasaun prosesu (PID, naran, uzu CPU, uzu memória, estadu)

3. Gia Ezersisiu Kontrolu Servisu:
   - Instrusaun atu hahu prosesu, halai iha kotuk, no hodi fila fali iha oin
   - Senario prátika ba estudante sira atu halo

## 4. Rekursu Adisionál ba Leitura ka Prátika

1. Kapítulu "Jestaun Prosesu Linux" husi "The Linux Command Line" husi William Shotts
2. Tutorial online: "H comprende Estadu Prosesu Linux" iha Linux.com
3. Pájina manual ba komandu ps, top, htop, no nice
4. Artigu "Prosesu no Sinal Linux" iha DigitalOcean
5. Simulador