'## Unidade Aprendizajen 2

## Unidade Aprendizajen 2: Dezenhu no Animasaun
- Objetivus:
  * Aprende atu dezenha formas no imajens iha ekran
  * Implementa teknikas animasaun báziku
- Tópikus:
  * Funsaun dezenhu Pygame
  * Karik no hatudu imajens
  * Animasaun simples ho Pygame
- Atividades:
  * Dezenha bandeira Timor-Leste uza formas Pygame
  * Anima símbolu kulturál lokál (hanesan, padraun tais)

## Rekursus Unidade

Iha ne'e rekursus detalladu ba Unidade Aprendizajen 2: Dezenhu no Animasaun, formatu iha Markdown:

# Unidade Aprendizajen 2: Dezenhu no Animasaun - Rekursus Detalladu

## 1. Nota Leitura

### Dezenha Formas ho Pygame

#### Introdusaun ba Dezenhu Pygame
- Pygame uza sistema coordenada ne'ebé (0, 0) mak kanto karuk leten
- Eixu X aumenta hodi ba loos, eixu Y aumenta hodi ba okos
- Hotu-hotu dezenhu akontese iha superfísie objetu

#### Funsaun Dezenhu Báziku
1. `pygame.draw.rect(surface, color, rect, width=0)`
   - Dezenha retângulo
   - `surface`: fatin atu dezenha
   - `color`: tuple RGB, hanesan, (255, 0, 0) ba mean
   - `rect`: (x, y, width, height) ka objetu pygame.Rect
   - `width`: espesura husi kontornu (0 ba forma prenxe)

2. `pygame.draw.circle(surface, color, center, radius, width=0)`
   - Dezenha sirkulu
   - `center`: tuple (x, y) ba sentru sirkulu
   - `radius`: radius husi sirkulu

3. `pygame.draw.line(surface, color, start_pos, end_pos, width=1)`
   - Dezenha linha
   - `start_pos` no `end_pos`: tuple (x, y)

#### Kór iha Pygame
- Kór reprezenta hanesan tuple RGB
- Valór varia husi 0 ba 255
- Kór komun:
  * Metan: (0, 0, 0)
  * Mutin: (255, 255, 255)
  * Mean: (255, 0, 0)
  * Matak: (0, 255, 0)
  * Azul: (0, 0, 255)

### Karik no Hatudu Imajens

#### Karik Imajens
- Uza `pygame.image.load(filename)` atu karik imajen
- Formatu suporta: JPG, PNG, GIF (la anima), BMP, PCX, TGA, TIF, LBM, PBM, XPM
- Ezemplu: `image = pygame.image.load("tais_pattern.png")`

#### Hatudu Imajens
- Uza `surface.blit(source, dest, area=None, special_flags=0)` atu dezenha superfísie ida iha superfísie seluk
- `source`: Superfísie atu dezenha
- `dest`: pozisaun atu dezenha (bele tuple ka Rect)
- Ezemplu: `screen.blit(image, (100, 100))`

### Teknikas Animasaun Báziku

#### Prinsípiu Animasaun
- Animasaun kria husi hatudu imajens la hanesan ho ritmu aas
- Iha Pygame, ne'e hetan husi redesenha ekran iha kada kuadru

#### Taxa Kuadru
- Kontrola ho `pygame.time.Clock()`
- Establese kuadru desejadu kada segundu (FPS) ho `clock.tick(FPS)`

#### Move Objetus
1. Hamlaha ekran (normalmente ho prenxe ho kór fundu)
2. Atualiza pozisaun objetus
3. Redesenha hotu-hotu objetus
4. Atualiza hatudu ho `pygame.display.flip()` ka `pygame.display.update()`

#### Ezemplu Siklu Animasa