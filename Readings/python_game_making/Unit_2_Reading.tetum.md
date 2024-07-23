'Dezeñu no Animasaun ho Pygame: Hanoin Lolon

Introdusaun

Pygame, hanesan konjuntu modulu Python ne'ebé dezenvolve ba hodi kria vídeu jogu, oferese instrumentu ba dezeñu no animasaun ne'ebé makaas. Artigu ne'e peskiza kona-ba konseitu no téknika fundamentál ne'ebé uza iha Pygame hodi kria elementu vizuál no fó vida ba sira liu husi animasaun. Ho kompreensaun ba prinsípiu sira-ne'e, dezenvolvedor sira bele kria jogu no aplikasaun interativa ne'ebé atrativu.

Dezeñu iha Pygame

Pygame-nia kapasidade atu dezéña iha laran mak superfísiu. Superfísiu iha Pygame mak pratika, área retangular ne'ebé bele dezéña gráfiku. Superfísiu prinsipál hatudu janela vídeu jogu, maibé bele kria superfísiu seluk ba renderização ne'ebé kompleksu liu.

Pygame oferese funsaun dezéña ne'ebé bele ajuda dezenvolvedor sira atu kria forma bázika diretamente iha superfísiu. Modulu pygame.draw inklui funsaun hanesan rect() ba retángulu, circle() ba sirkulu, no line() ba linha. Funsaun sira-ne'e foti parámetru ne'ebé hateten superfísiu sasán, kór, no koordenada. Kór iha Pygame normálmente reprezenta ho valór RGB (Matak, Metan, Azúl), ne'ebé bele hetan opsaun kór barak.

Imajen Manipulasaun

Maske útil atu dezéña forma, jogu barak presiza gráfiku ne'ebé kompleksu liu. Pygame suporta karga no hatudu imajen liu husi modulu imajen. Funsaun pygame.image.load() bele karga formatu imajen barak, hodi kria superfísiu husi arquivu imajen. Superfísiu ne'e bele "blitted" (dezéña) ba superfísiu seluk, normalmente superfísiu hatudu prinsipál.

Animasaun Bázika

Animasaun iha Pygame hetan liu husi atualiza hatudu ho imajen ne'ebé la hanesan ou movimenta objetu liu-liu iha ekrán. Konseitu taxa kadru importante iha ne'e, determina hira dala hatudu atualiza iha segundu ida.

Kódigu hanesan tuir mai bele kria animasaun bázika iha Pygame:

x = 0
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Klean ekrán
    pygame.draw.rect(screen, (0, 0, 255), (x, 100, 50, 50))
    x += 1  # Muda retángulu

    pygame.display.flip()  # Atualiza hatudu
    clock.tick(60)  # Mantein 60 fps

Kódigu ne'e kria retángulu azúl ne'ebé seidauk liu husi ekrán husi karuk ba loos, atualiza dala 60 iha segundu ida.

Sprites no Grupu Sprite

Ba jogu ne'ebé kompleksu liu, Pygame introdús konseitu sprite. Sprite mak objetu ne'ebé reprezenta elementu vídeu jogu, inklui reprezentasaun vizuál no komportamentu. Modulu sprite Pygame fornese klasifikasaun Sprite, ne'ebé bele kria objetu vídeu jogu.

Grupu sprite mak koleksaun sprite sira ne'ebé bele atualiza no dezéña hamutuk, hodi simplifika jestaun ba objetu vídeu jogu barak. Ne'e útil tebes ba jestaun ba objetu hanesan barak, hanesan inimigu ka projeção iha vídeu jogu.

Konklusaun

Dezeñu no animasaun mak as