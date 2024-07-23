'Iha ne'e rekursu kompleto ida kona ba dokumentasaun Pygame no ezemplu ba Unidade 6:

# Dokumentasaun Pygame no Ezemplu

## 1. Introdusaun ba Pygame

Pygame maka konjuntu ida husi módulu Python ne'ebé dezenvolve ba hakerek vídeu jogu. Nia inklui gráfiku komputadór no biblioteka sonus ne'ebé dezenvolve ba uza ho lian programasaun Python.

### Karaterístika Prinsipál:
- Plataforma transversál
- Dezenvolve iha leten SDL (Simple DirectMedia Layer)
- Suporta gráfiku 2D no 3D
- Forsese módulu ba maneja eventu, desenhu, karga imajen no sonus, no barak liu tan

## 2. Instalasaun

Atu instala Pygame, uza pip:

```
pip install pygame
```

## 3. Estrutura Bázika husi Programa Pygame

```python
import pygame

pygame.init()

# Prepara hatudu
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ha'u nia Jogu")

# Loop jogu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Lójika jogu iha ne'e
    
    # Kódigu desenhu iha ne'e
    
    pygame.display.flip()

pygame.quit()
```

## 4. Módulu Prinsipál Pygame

### 4.1 pygame.display
- Jere janela hatudu no ekrãn
- Funsaun prinsipál:
  - `set_mode()`: Inisia janela ba hatudu
  - `flip()`: Atualiza hatudu tomak

### 4.2 pygame.event
- Jere eventu no fila eventu
- Funsaun prinsipál:
  - `get()`: Hetan eventu husi fila

### 4.3 pygame.draw
- Iha funsaun desenhu
- Ezemplu:
  - `rect()`: Desenhu retângulu
  - `circle()`: Desenhu sirkulu

### 4.4 pygame.image
- Jere karga no salva imajen
- Funsaun prinsipál:
  - `load()`: Karga imajen husi ficheiru

### 4.5 pygame.mixer
- Jere reproduksaun sonus
- Funsaun prinsipál:
  - `Sound()`: Kria Objetu Sonus husi ficheiru

## 5. Ezemplu

### 5.1 Desenhu Forma

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

# Desenhu retângulu mean
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 100))

# Desenhu sirkulu azúl
pygame.draw.circle(screen, (0, 0, 255), (200, 150), 50)

pygame.display.flip()
```

### 5.2 Karga no Hatudu Imajen

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

# Karga imajen
image = pygame.image.load("player.png")

# Hatudu imajen
screen.blit(image, (100, 100))

pygame.display.flip()
```

### 5.3 Maneja Input Uzuáriu

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Botão espaço primi!")

    pygame.display.flip()

pygame.quit()
```

### 5.4 Toca Sonus

```python
import pygame

pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound("beep.wav")
sound.play()

pygame.time.wait(1000)  # Hespera ba segundu ida
```

## 6. Rekursu Útil

- Dokumentasaun Ofisiál Pygame: https://www.pygame.org/docs/
- Tutorial Pygame: https://www.pygame.org/wiki/tutorials
- Ezemplu Pygame: https://www.pygame.org/docs/ref/examples.html

## 7. K