'Iha ne'e apoiu material ba lição kona-ba Uzuáriu Input no Jogu Controls, ne'ebé formatu iha Markdown:

# Material Apoiu: Uzuáriu Input no Jogu Controls

## 1. Lista Vocabuláriu Prinsipál ho Definisaun

- **Event Handling**: Prosesu deteksaun no responde ba aksaun uzuáriu ka eventu sistema iha programa
- **Keyboard Events**: Aksaun sira ne'ebé relasiona ho tekan ka la tekan tekladu
- **Mouse Events**: Aksaun sira ne'ebé relasiona ho movimentu mouse ka klik iha nia botun
- **Game Loop**: Siklu kontínuu iha jogu ne'ebé aktualiza estadu jogu no rende gráfiku
- **Sprite**: Imajen 2D ka animasaun ne'ebé reprezenta karakter ka objetu iha jogu
- **Input**: Informasaun ne'ebé programa simu husi fonte esternu (exemplu, tekladu, mouse)
- **Key Constant**: Variável predefinidu iha Pygame ne'ebé reprezenta tekladu ida espesífiku (exemplu, K_UP, K_DOWN)
- **Frame Rate**: Númeru veses kada segundu ne'ebé jogu aktualiza no desenha fali nia gráfiku
- **Delta Time**: Tempu ne'ebé hahu husi frame ida ba frame tuir mai iha jogu

## 2. Ajuda Visual ka Diagrama

1. **Event Handling Flowchart**: Diagrama ne'ebé hatudu fluxu eventu iha programa Pygame, husi input uzuáriu to'o respostas jogu.
   - Uzuáriu Input → Event Queue → Event Handling → Update Estadu Jogu → Rende Gráfiku

2. **Keyboard Layout Diagram**: Imajen tekladu ho tekladu seta no tekladu kontrolu jogu komun sira-ne'ebé destaka, ho label sira ho nia konstante tekladu Pygame ne'ebé koresponde.

3. **Sprite Movement Diagram**: Seri imajen sira-ne'ebé hatudu mudansa pozisaun sprite bazeia ba tekan tekladu diferente, ho seta sira hatudu direksaun movimentu.

## 3. Handouts ka Worksheets

1. **Event Handling Code Template**: Worksheet ida ho estrutura bázika handling eventu Pygame, ho espasu mamuk ba estudante sira atu preenxe respostas eventu espesífiku.

2. **Input-Output Table**: Tabela ida ba estudante sira atu preenxe, mapeia input uzuáriu diferente (exemplu, tekan tekladu, klik mouse) ba output jogu ka aksaun esperadu.

3. **Sprite Movement Exercise**: Worksheet ida ho grid ne'ebé reprezenta ekrã jogu, iha-ne'ebé estudante sira desenha dalan sprite bazeia ba sekénsia tekan tekladu ne'ebé fó tiha ona.

## 4. Rekursus Adisionál

1. Dokumentasaun Pygame kona-ba Event Handling: https://www.pygame.org/docs/ref/event.html
2. Tutorial kona-ba Pygame Input Handling: https://realpython.com/pygame-a-primer/#handling-events
3. Vídeu Tutorial: "Pygame iha 90 Minutus - Ba Prinsipiantes" (foka iha seksaun input): https://www.youtube.com/watch?v=jO6qQDNa2UY
4. Tutorial Interativu Pygame Input: https://pythonprogramming.net/pygame-tutorial-moving-images-key-input/

## 5. Tips ba Profesór

1. **Dezafiu**: Estudante sira bele hetan difikuldade ho konseitu handling input kontínuu iha game loop.
   **Solusaun**: Uza analogia sira husi mundu real, hanesan seguransa ne'ebé semo sempre halo verifikasaun ba eventu, atu esplika konseitu.

2. **Dezafiu**: Difisuldade iha komprensaun diferensa entre tekan tekladu no teklad