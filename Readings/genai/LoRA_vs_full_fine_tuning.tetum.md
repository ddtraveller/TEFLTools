'# LoRA kontra Afinasaun Kompletu: Komprende Diferensa sira

## Afinasaun Kompletu

Afinasaun kompletu involve atu atualiza hotu ka barak liu husi parametru sira iha modelu ne'ebé treinu tiha ona atu adapta ba tarefa ka dominio foun.

### Karakteristika:
1. **Atualizasaun total**: Kapa hotu husi modelu atualiza durante treinamentu.
2. **Rekursu nesesariu aas**: Presiza kapasidade komputasaun no memoria boot.
3. **Risku Overfitting nian**: Risku boot atu sai overfitting, liuliu ho dataset ki'ik.
4. **Flexibilidade**: Bele halo adaptasaun total ba modelu.
5. **Armazenamentu**: Presiza armazena kopia kompletu husi modelu adaptadu.

### Kondisaun Uzu:
- Bainhira iha dataset boot no diversu
- Bainhira presiza alterasaun boot ba modelu nia hahalok
- Bainhira rekursu komputasaun la restringe

## LoRA (Adaptasaun Ranku Kraik)

LoRA maka teknika ne'ebé adapta modelu lian ne'ebé treinu tiha ona liuhusi tau matris ranku dekompozisaun ne'ebé ki'ik no bele treinu ba iha pesos ezistente.

### Karakteristika:
1. **Atualizasaun Parametru efisiente**: Atualiza de'it numeru ki'ik parametru nian.
2. **Rekursu Nesesariu Kraik**: Presiza memoria no kapasidade komputasaun ne'ebé menus.
3. **Risku Overfitting menus**: Risku kraik atu sai overfitting, liuliu ho dataset ki'ik.
4. **Modular no Muda-Troka**: Adaptador LoRA bele muda-troka ka kombina ho fasilidade.
5. **Efisiensia Armazenamentu**: Presiza de'it armazena pesos LoRA ki'ik, la'os modelu tomak.

### Kondisaun Uzu:
- Bainhira hahu servisu ho rekursu komputasaun limitadu
- Ba adaptasaun lais ba tarefa ka dominio espesifiku
- Bainhira hakarak mantein adaptasaun barak husi modelu ba objetivu sira ne'ebé diferente

## Diferensa Xave

1. **Efisiensia Parametru**:
   - Afinasaun Kompletu: Atualiza parametru hotu husi modelu
   - LoRA: Atualiza de'it subset parametru

2. **Uzu Memoria**:
   - Afinasaun Kompletu: Presiza memoria ba modelu tomak
   - LoRA: Presiza memoria de'it ba pesos adaptador nian

3. **Velosidade Treinamentu**:
   - Afinasaun Kompletu: Jeralmente lalais liu
   - LoRA: Jeralmente lais liu tanba atualiza parametru menus

4. **Adaptabilidade**:
   - Afinasaun Kompletu: Bele halo alterasaun total ba hahalok modelu nian
   - LoRA: Efetivu ba adaptasaun tarefa espesifiku, maibé bele iha limitasaun ba mudansa drastiku

5. **Risku Husi Eskece Katastrofiku**:
   - Afinasaun Kompletu: Risku aas ba modelu "eskece" nia koñesimentu ne'ebé treinu tiha ona
   - LoRA: Risku kraik, tanba modelu orijinal barak mak sei hanesan

6. **Modularidade**:
   - Afinasaun Kompletu: Rezulta iha modelu foun no kompletu
   - LoRA: Produs pesos adaptador ne'ebé bele mistura no kombina ho modelu baze

## Hili entre LoRA no Afinasaun Kompletu

- Hili LoRA bainhira:
  1. Iha rekursu komputasaun limitadu
  2. Presiza adaptasaun lais ba tarefa espesifiku
  3. Hakarak mantein adapt