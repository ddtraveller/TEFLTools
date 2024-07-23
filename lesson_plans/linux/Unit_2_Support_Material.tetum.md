'Iha ne'e apoiu material ba planu aula kona-ba Navegasaun no Jestaun Sistema Arkivu, formatu iha Markdown:

# Material Apoiu ba Aula Navegasaun no Jestaun Sistema Arkivu

## 1. Lista Vocabulariu Importante ho Definisaun

- **Sistema Arkivu**: Dalan ne'ebé arkivu naran no sira-nia fatin loloos ba armazenamentu no buka fila-fila
- **Direktoriu**: Estrutura katalogu sistema arkivu ne'ebé iha referensia ba arkivu sira no diretoriu sira seluk
- **Dalan**: Fatin uniku ida husi arkivu ka direktoriu iha sistema arkivu
- **Dalan absolutu**: Dalan ida ne'ebé hahu husi direktoriu root (/)
- **Dalan relativa**: Dalan ida ne'ebé hahu husi direktoriu servisu atual
- **Permissoens**: Regra sira ne'ebé asosia ho arkivu ka direktoriu ne'ebé kontrola asesu uzuariu (lee, hakerek, ezekuta)
- **Propriedade**: Uzuariu no grupu ne'ebé atribui hanesan dono ba arkivu ka direktoriu
- **Direktoriu root**: Direktoriu nivel leten ida husi sistema arkivu, indikadu ho /
- **Direktoriu uma**: Direktoriu ida ba uzuariu partikular ida husi sistema
- **Direktoriu servisu**: Direktoriu ne'ebé uzuariu hela servisu iha ne'ebá

## 2. Ajuda Vizuál ka Diagrama

1. Diagrama Hierarkia Sistema Arkivu Linux:
   - Estrutura hanesan ai-hun ne'ebé hatudu direktoriu sira prinsipál:
     - / (root)
       - /home (direktoriu uma uzuariu)
       - /etc (arkivu konfigurasaun sistema)
       - /var (dadus variavel)
       - /usr (programa no dadus uzuariu)
       - /tmp (arkivu temporariu)
       - /boot (arkivu boot loader)
       - /dev (arkivu dispositivo)
       - /mnt (pontu monta ba sistema arkivu)
       - /opt (paketus softuare opcionál)

2. Diagrama Permissoens Arkivu:
   - Representasaun vizuál husi permissoens rwx (lee, hakerek, ezekuta) ba uzuariu, grupu, no sira seluk:
     ```
     rwx rwx rwx
     ||| ||| |||
     ||| ||| ||+-- Seluk: Ezekuta
     ||| ||| |+--- Seluk: Hakerek
     ||| ||| +---- Seluk: Lee
     ||| ||+------ Grupu: Ezekuta
     ||| |+------- Grupu: Hakerek
     ||| +-------- Grupu: Lee
     ||+---------- Uzuariu: Ezekuta
     |+----------- Uzuariu: Hakerek
     +------------ Uzuariu: Lee
     ```

## 3. Folha Informativa ka Exercisiu

1. Folha Kódigu Navegasaun Sistema Arkivu:
   - Lista komandu navegasaun komun (cd, pwd, ls) ho ezemplu sira
   - Esplikasaun kona-ba dalan absolutu kontra dalan relativa ho exercisiu prátika

2. Exercisiu Prátika Manipulasaun Arkivu:
   - Série tarefa sira ba estudante atu prátika komandu manipulasaun arkivu (cp, mv, rm, mkdir, touch)
   - Inklui kria estrutura direktoriu espesífika no muda arkivu entre direktoriu sira

3. Exercisiu Puzzle Permissoens:
   - Senariu variedade ne'ebé estudante presiza determina permissoens korretu
   - Exercisiu prátika ba uza komandu chmod no chown

## 4. Rekursu Adisionál ba Leitura Ka Prátika Tan

1. Tutorial Online:
   - LinuxCommand