'# Bash Kontrolu Estrutura, Fungsaun, no Tratamentu Erro

## I. Kontrolu Estrutura

### Deklarasaun If-else
Deklarasaun If-else permite ita atu ezekuta komandu diferent sira bazeia ba kondisaun ida. Sintaksa bázika mak hanesan tuir mai:

```bash
if [ kondisaun ]; then
    # Komandu sira atu ezekuta bainhira kondisaun loos
else
    # Komandu sira atu ezekuta bainhira kondisaun sala
fi
```

Ita bele mós uza `elif` atu aumenta kondisaun adisional:

```bash
if [ kondisaun1 ]; then
    # Komandu sira atu ezekuta bainhira kondisaun1 loos
elif [ kondisaun2 ]; then
    # Komandu sira atu ezekuta bainhira kondisaun2 loos
else
    # Komandu sira atu ezekuta bainhira kondisaun hotu-hotu sala
fi
```

Exemplu:
```bash
idade=25
if [ $idade -lt 18 ]; then
    echo "Ita ki'ik."
elif [ $idade -ge 18 ] && [ $idade -lt 65 ]; then
    echo "Ita adultu."
else
    echo "Ita sidadaun senior."
fi
```

### Deklarasaun Kaza
Deklarasaun Kaza proporciona dalan ida atu konferensia valor ida hasoru padraun sira no ezekuta komandu korespondente. Sintaksa mak hanesan tuir mai:

```bash
case $variavel in
    padraun1)
        # Komandu sira atu ezekuta bainhira variavel tuir padraun1
        ;;
    padraun2)
        # Komandu sira atu ezekuta bainhira variavel tuir padraun2
        ;;
    *)
        # Komandu default sira atu ezekuta bainhira laiha tuir
        ;;
esac
```

Exemplu:
```bash
loron="Segunda"
case $loron in
    "Segunda"|"Tersa"|"Kuarta"|"Kinta"|"Sesta")
        echo "Ne'e loron semana."
        ;;
    "Sabadu"|"Domingu")
        echo "Ne'e fim-de-semana."
        ;;
    *)
        echo "Loron la validu."
        ;;
esac
```

### Loop For
Loop For permite ita atu itera lista item sira no ezekuta komandu ba kada item. Sintaksa mak hanesan tuir mai:

```bash
for item in lista; do
    # Komandu sira atu ezekuta ba kada item
done
```

Exemplu:
```bash
futa=("maça" "banana" "laranja")
for ai-fuan in "${futa[@]}"; do
    echo "Hau gosta $ai-fuan."
done
```

### Loop Enkuantu
Loop Enkuantu ezekuta komandu sira hanesan ona too kondisaun loos. Sintaksa mak hanesan tuir mai:

```bash
while [ kondisaun ]; do
    # Komandu sira atu ezekuta bainhira kondisaun loos
done
```

Exemplu:
```bash
kuenta=1
while [ $kuenta -le 5 ]; do
    echo "Kuenta: $kuenta"
    ((kuenta++))
done
```

### Demonstrasaun no Ezersisiu Prátika

1. Hakerek skript ida ne'ebé verifica se numeru pozitivu, negativu, ka zero.
2. Hakerek skript ida ne'ebé hatudu naran loron bazeia ba numeru (1-7).
3. Hakerek skript ida ne'ebé kalkula factorial husi numeru uza loop For.
4. Hakerek skript ida ne'ebé husu uza-na'in atu hatama password too password korreto haruka.

## II. Fungsaun no Tratamentu Erro

### Definisaun no Xamada Fungsaun
Fungsaun sira mak bloku kódigu ne'ebé bele uza fila-fali no bele