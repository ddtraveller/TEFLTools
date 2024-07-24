'# ## Unidade Aprendizajen 3

## Unidade Aprendizajen 3: Uzuáriu Input no Kontrolu Jogu
- Objetivu:
  * Maneja input husi tekladu no rato
  * Implementa movimentu jogadór
- Tópiku sira:
  * Manejamentu eventu Pygame
  * Input husi tekladu no rato
  * Muda objetu jogu
- Atividade sira:
  * Kria programa ida atu muda karakter ida uza tekladu seta
  * Implementa kontrolu rato ba movimentu karakter

## Rekursu Unidade

Iha ne'e rekurso sira detallu ba Unidade Aprendizajen 3: Uzuáriu Input no Kontrolu Jogu, formatadu iha Markdown:

# Unidade Aprendizajen 3: Uzuáriu Input no Kontrolu Jogu - Rekursu Detallu

## 1. Nota Aula

### Introdusaun ba Manejamentu Eventu Pygame

- Eventu iha Pygame reprezenta aksaun uzuáriu ka okorensia sistema
- Loop eventu sempre verifica no prosesa eventu
- Estrutura báziku husi loop eventu:

```python
import pygame

pygame.init()
ekraun = pygame.display.set_mode((800, 600))
halai = True

while halai:
    for event iha pygame.event.get():
        if event.tipu == pygame.QUIT:
            halai = False
    
    # Kódigu lójika jogu no dezeñu iha ne'e

    pygame.display.flip()

pygame.quit()
```

### Input Tekladu

- Pygame fornese konstante ba tekladu (e.g., `pygame.K_UP`, `pygame.K_SPACE`)
- Maneira rua prinsipál atu maneja input tekladu:
  1. Bazeia ba eventu: Verifika `pygame.KEYDOWN` no `pygame.KEYUP` eventu
  2. Bazeia ba estadu: Uza `pygame.key.get_pressed()` ba input kontínuu

Ezemplu input bazeia ba eventu:

```python
for eventu iha pygame.event.get():
    if eventu.tipu == pygame.KEYDOWN:
        if eventu.tekla == pygame.K_LEFT:
            print("Tekla seta karuk pressionadu")
        elif eventu.tekla == pygame.K_RIGHT:
            print("Tekla seta loos pressionadu")
```

Ezemplu input bazeia ba estadu:

```python
tekla = pygame.key.get_pressed()
if tekla[pygame.K_LEFT]:
    jogadór_x -= 5
if tekla[pygame.K_RIGHT]:
    jogadór_x += 5
```

### Input Rato

- Eventu rato inklui movimentu, klik butaun, no roda scroll
- Eventu rato komun:
  - `pygame.MOUSEMOTION`: Movimentu rato
  - `pygame.MOUSEBUTTONDOWN`: Butaun rato pressionadu
  - `pygame.MOUSEBUTTONUP`: Butaun rato la pressionadu

Ezemplu input rato:

```python
for eventu iha pygame.event.get():
    if eventu.tipu == pygame.MOUSEBUTTONDOWN:
        if eventu.butaun == 1:  # Butaun rato karuk
            print("Klik karuk iha", eventu.pos)
    elif eventu.tipu == pygame.MOUSEMOTION:
        print("Rato muda ba", eventu.pos)
```

### Muda Objetu Jogu

- Atualiza pozisaun objetu bazeia ba input iha loop jogu
- Konsidera taxa frame no tempu delta ba movimentu suave
- Ezemplu muda sprite jogadór:

```python
jogadór_x, jogadór_y = 400, 300
velosidade_jogadór = 5

# Iha loop jogu
tekla = pygame.key.get_pressed()
if tekla[pygame.K_LEFT]:
    jogadór_x -= velosidade_jogadór
if tekla[pygame.K_RIGHT]:
    jogadór_x += velosidade_jogadór
if tekla[pygame.K_UP]:
    jogadór_y -= velosidade_jogadór
if tekla[pygame.K_DOWN]:
    jogadór_y += velosidade_jogadór

# Dezena jogad