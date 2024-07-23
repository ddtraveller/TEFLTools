'Estrutura Dadus iha Python: Haree Kompletu

Introdusaun

Python, lian programasaun ne'ebé versátil no potente, oferese konjuntu estrutura dadus ne'ebé riku, ne'ebé habilita organizasaun no manipulasaun dadus ho efisiente. Estrutura sira ne'e fundamentál ba hakerek kódigu ne'ebé efetivu no otimizadu. Iha dokumentu ne'e, ita sei esplora estrutura dadus tolu prinsipál iha Python nian: listas, tuplas, no dicionários. Ita sei analiza karakterístika, kazu uza, no vantajen sira ne'ebé sira oferese iha situasaun programasaun oioin.

Listas: Koleksaun Dinámiku no Mutável

Listas mak estrutura dadus ne'ebé uza liu hotu iha Python. Sira ordenadu, koleksaun mutável ne'ebé bele inklui elementus husi tipu dadus diferente. Listas define ho kuda hakerek kuadrátiku no bele modifika depois kriasaun, ne'ebé torna sira flexível tebes ba aplikasaun barak.

Ezemplu, lista kidades Timor nian bele reprezenta hanesan:

```python
kidades_timor = ["Dili", "Baucau", "Maliana", "Suai"]
```

Listas suporta operasaun no métodu oioin. Elementus bele aumenta ho métodu append() ka insere iha pozisaun espesífiku ho usa insert(). Métodu extend() permite konkatenasau listas. Remosaun elementus bele halo liu husi métodu sira hanesan remove() ka pop(). Listas mós suporta índise no fatia, ne'ebé fásiliza asesu no manipulasaun elementus.

Karakterístika ida ne'ebé potente husi listas mak kompreensaun lista, ne'ebé fornese dalan badak ba kria listas foun bazeia ba listas ezistente. Ezemplu:

```python
kuadrádu = [x**2 for x in range(10)]
```

Ne'e kria lista kuadrádu husi númeru sira husi 0 ba 9 iha liña ida de'it husi kódigu.

Tuplas: Sekuénsia Imutável

Tuplas hanesan listas maibé ho diferensa ida ne'ebé importante: sira imutável. Depois kria, tuplas la bele modifika. Sira define ho parenteses:

```python
koordenada = (125.5741, -8.5568)  # Koordenada husi Dili
```

Imutabilidade husi tuplas torna sira ideál ba reprezenta koleksaun fixa husi item sira, hanesan koordenada ka valór kór RGB. Tuplas uza liu bainhira ita hakarak garantia katak dadus permanese konstante durante ezekusaun programa.

Tuplas suporta índise no bele desempakotadu, ne'ebé permite atribuisaun variável múltiplu iha liña ida:

```python
longitude, latitude = koordenada
```

Maske menus flexível duke listas, tuplas oferese benefísiu desempeñu iha situasaun balun no bele uza hanesan xave dicionáriu, ne'ebé la posível ho listas mutável.

Dicionários: Par Xave-Valór

Dicionários mak koleksaun desordenadu husi par xave-valór. Sira fornese dalan efisiente ba armazena no rekupera dadus bazeia ba xave únika. Dicionários define ho kuda hakerek kurla:

```python
tetum_ingles = {
    "bondia": "good morning",
    "obrigadu": "thank you",
    "hau": "I"
}
```

Dicionários oferese peskiza ne'ebé lais no ideál ba situasaun ne'ebé ita presiza asosia valór sira ho identifikadór únika. Sira suporta métodu oioin ba aumenta, hasai, no asesu element