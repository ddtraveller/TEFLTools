'## Unidade Aprendizajen 6

## Unidade Aprendizajen 6: Fundamentus Scripting Shell
- Objetivus:
  * Komprende fundamentus scripting shell
  * Kria scripts automasaun básiku
- Tópikus:
  * Estrutura no sintaxe script shell
  * Variáveis, loops, no kondisionais
  * Substituisaun komandu no piping
- Atividades:
  * Hakerek script hodi automatiza verifica sistema loron-loron
  * Kria script backup ba fail sistema importante

## Rekursus Unidade

# Rekursus Básiku Scripting Shell 

## Notas Palestra

### Estrutura no Sintaxe Script Shell

- Scripts shell sira mak fail textu sira ne'ebé kontén série komandus
- Liña primeiru normalmente hahu ho shebang (#!) no tuir dalan ba interpreter
- Ezemplu: #!/bin/bash
- Komentáriu sira hahu ho #
- Komandus sira executa tuir sequénsia, ida kada liña
- Bele uza \ ba kontinuasaun liña
- Scripts presiza iha permisaun executável (chmod +x script.sh)
- Korré scripts ho ./script.sh ka bash script.sh

### Variáveis

- Deklara variáveis: NARAN_VARIAVEL=valor (la iha espasu volta =)
- Aksesu variáveis ho $NARAN_VARIAVEL
- Uza aspas ba valores ho espasu: NARAN="John Doe"
- Variáveis espesiál:
  - $0: Naran script
  - $1, $2, sira seluk: Argumentus linha komandu
  - $#: Númeru argumentus
  - $@: Argumentus hotu-hotu hanesan lia-fuan separadu
  - $?: Status saida husi komandu ikus

### Loops no Kondisionais

#### Loops For
```bash
for item iha lista
do
    # komandus
done
```

#### Loops While
```bash
while [ kondisaun ]
do
    # komandus
done
```

#### Kondisionais If
```bash
if [ kondisaun ]
then
    # komandus
elif [ kondisaun ]
then
    # komandus
else
    # komandus
fi
```

### Substituisaun Komandu no Piping

- Substituisaun komandu: $(komandu) ka `komandu`
- Kaptura saida husi komandu hodi uza iha script
- Piping: komandu1 | komandu2
- Haruka saida husi komandu1 hanesan input ba komandu2

## Perguntas Diskusaun

1. Oinsá script shell bele hadi'a tarefas administrasaun sistema?
2. Saida maka preokupasaun seguransa potensial bainhira hakerek scripts shell?
3. Oinsá variáveis iha scripts shell difere husi variáveis iha línguas programasaun seluk?
4. Iha situasaun saida mak ita sei hili loop for liu loop while, ka versa versa?
5. Oinsá nune'e kombina substituisaun komandu no piping atu kria scripts ne'ebé boot?

## Exercísius Hakerek

1. Hakerek script shell ne'ebé husu uza nia naran no kór favoritu, no depois imprime kumprimentu personalizadu ho input sira-ne'ebé.
2. Kria script ida ne'ebé verifica se diretóriu ida eziste. Karik eziste, lista sira-nia konteúdu; se lae, kria diretóriu.
3. Dezenvolve script ida ne'ebé lee lista numerus husi fail ida no kalkula sira-nia suma no media.

## Detalhes Trabalhu

### Script Verifikasaun Sistema

Kria script shell naran `system_check.sh` ne'ebé halo tarefa sira tuir mai:
1. Apresenta uptime sistema atual
2. Hatudu uzasaun disk ba filesystems hotu-hotu ne'ebé monta tiha
3. Lista uza sira ne'ebé loga on iha momentu
4. Imprime data no oras atual

Rekis