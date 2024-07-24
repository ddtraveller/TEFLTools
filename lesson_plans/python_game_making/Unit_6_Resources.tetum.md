'Unidade Aprendizajen 6

Unidade Aprendizajen 6: Projetu Finál - Jogu Kompletu Dodger
- Objetivus:
  * Aplika konseitus hotu-hotu ne'ebé ita aprende ba kria jogu kompletu
  * Personaliza jogu ho elementus kulturális lokál
- Tópikus:
  * Dezenu no planeamentu jogu
  * Integra elementus hotu-hotu jogu
  * Debugging no testajen
- Atividades:
  * Dezenvolve jogu Dodger ho gráfikus no sonus temátika Timor-Leste
  * Apresenta no testa jogu ho ema seluk iha klase

Rekursus Rekeridus
- Komputadór ho Python 3.x no Pygame instaladu
- Editor texte (ex., IDLE, Visual Studio Code)
- Software edisaun imajen báziku (ex., GIMP)

Sujestaun Itens ba Kobre
- Prinsípius báziku dezenu jogu
- Kontrolu versaun ho Git
- Publika jogus online ka ba plataformas móveis

Esperiénsia Prátika no Envolvimentu Komunidade
- Organiza eventu demonstrasaun jogu ba komunidade lokál
- Kolabora ho artistas lokáis ba gráfikus no múzika jogu
- Dezenvolve jogus edukasionál ba eskola lokál ou organizasaun

Rekursus Adisionál
- Tutorials Python online no dokumentasaun
- Dokumentasaun Pygame no exemplos
- Ativos jogu grátis no bibliotekas sonus
- Komunidades no fóruns dezenvolvimentu jogu lokál

Syllabus ne'e adapta ba kontestu Timor-Leste liu husi integrasaun elementus kulturális lokál, uza ezemplu familiares, no sujere atividades envolvimentu komunidade relevante ba rejiaun. Estrutura ne'e fornese progresu klaru unidade aprendizajen nian, kada ida ho objetivus, tópikus, no atividades ne'ebé ajusta ba kontestu lokál.

Rekursus Unidade

Iha ne'e mak rekursus detalhadu ba Unidade Aprendizajen 6: Projetu Finál - Jogu Kompletu Dodger, formatadu iha Markdown:

Rekursus ba Unidade Aprendizajen 6: Projetu Finál - Jogu Kompletu Dodger

1. Nota Aula

Dezenu Jogu no Planeamentu

Introdusaun ba Dokumentus Dezenu Jogu (GDD)
- Propósitu: Blueprint ba dezenvolvimentu jogu
- Komponentus xave:
  * Konseitu jogu no istória
  * Mekánika jogu
  * Estilu vizuál no direksaun arte
  * Dezenu sonu
  * Rekisitus tékniku

Kria GDD ba Jogu Dodger
1. Konseitu Jogu:
   - Jogador kontrola karakter ne'ebé evita objetos monu
   - Tema Timor (ex., festival tradisionál, eventu istóriku)
2. Mekánika Jogu:
   - Kontrolus movimentu (tekladu/ratu)
   - Sistema pontuasaun
   - Progresu difikuldade
3. Estilu Vizuál:
   - Gráfikus inspiradu Timor (karakteres, fundus)
   - Dezenu UI (display pontuasaun, ekrã menus)
4. Dezenu Sonu:
   - Múzika fundu (múzika tradisionál Timor)
   - Efeitus sonu (kolisaun, pontuasaun)
5. Rekisitus Tékniku:
   - Python no Pygame
   - Rekisitus sistema mínimu

Integrasaun Elementus Jogu

Estrutura Loop Jogu Prinsipál
```python
import pygame

# Inisializa Pygame
pygame.init()

# Setup jogu
ekrã = pygame.display.set_mode((800, 600))
relójiu = pygame.time.Clock()

# Loop jogu
korrendu = True
while korrendu:
    # Trata eventus
    for eventu in pygame