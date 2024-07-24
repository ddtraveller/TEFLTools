'# ## Unidade Aprendizajen 4

## Unidade Aprendizajen 4: Deteção Kolisão no Lójika Jogu
- Objetivu:
  * Komprende no implementa deteção kolisão
  * Dezenvolve regras jogu no sistema pontuasaun
- Tópiku:
  * Deteção Kolisão Retangular
  * Implementasaun regras jogu
  * Pontuasaun no jestaun estadu jogu
- Atividade:
  * Kria jogu simples koleksaun ho ai-fuan lokál (hanesan, ai-manas, ai-papaia)
  * Implementa pontuasaun bazeia ba itens ne'ebé kolekta

## Rekursu Unidade

Iha ne'e detallu rekursu ba Unidade Aprendizajen 4: Deteção Kolisão no Lójika Jogu, formatu iha Markdown:

# Unidade Aprendizajen 4: Deteção Kolisão no Lójika Jogu Rekursu

## 1. Nota Leksiun

### Deteção Kolisão

#### Introdusaun ba Deteção Kolisão
- Deteção kolisão mak konseitu fundamentál iha dezenvolvimentu jogu
- Nia determina bainhira objektu jogu interajen ka sobrepos
- Esensiál ba mekanika jogu hanesan kolekta itens, evita obstákulu, etc.

#### Deteção Kolisão Retangular
- Forma simples liu husi deteção kolisão
- Uza kaixa limitadora (retángulu) atu aproksima forma objektu
- Pygame fornese klase `Rect` atu fasil manipulasaun retángulu

#### Implementasaun Deteção Kolisão ho Pygame
```python
# Kódigu ezemplu ba deteção kolisão retangular
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(120, 120, 60, 60)

if rect1.colliderect(rect2):
    print("Kolisão detetada!")
```

- Métedu `colliderect()` verifica se retángulu rua sobrepos
- Bele uza ba kolisão entre jogadór-item, jogadór-inimigu, etc.

### Regras Jogu no Pontuasaun

#### Importánsia Regras Jogu
- Regras define oinsá jogu joga
- Kria estrutura no dezafiu ba jogadór
- Ezemplu: kolekta itens, evita obstákulu, limiti tempu

#### Implementasaun Sistema Pontuasaun Báziku
```python
score = 0

# Aumenta pontuasaun bainhira jogadór kolekta item
if player_rect.colliderect(item_rect):
    score += 10
    # Hasai item ne'ebé kolekta tiha ona
    items.remove(item)

# Hatudu pontuasaun
font = pygame.font.Font(None, 36)
score_text = font.render(f"Pontuasaun: {score}", True, (255, 255, 255))
screen.blit(score_text, (10, 10))
```

#### Jestaun Estadu Jogu
- Estadu jogu komun: hola jogu, pausa, jogu remata
- Uza variável atu monitoriza estadu atuál
```python
PLAYING = 0
PAUSED = 1
GAME_OVER = 2

current_state = PLAYING

# Iha loop jogu
if current_state == PLAYING:
    # Atualiza lójika jogu
elif current_state == PAUSED:
    # Hatudu menu pausa
elif current_state == GAME_OVER:
    # Hatudu ekrã jogu remata
```

## 2. Pergunta Diskusaun

1. Oinsá deteção kolisão kontribui ba gameplay iha vários genre jogu?
2. Saida mak avantajen no dezvantajen husi uza deteção kolisão retangular?
3. Oinsá bele ami halo deteção kolisão liu tan presiza ba objektu forma irregular?
4. Tansaa sistema pontuasaun importante iha jogu? Oinsá nia afeta motivasaun jogadór?
5. Saida mak maneira kreativu balun atu implement