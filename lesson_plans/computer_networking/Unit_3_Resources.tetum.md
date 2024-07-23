'## Unidade Aprendizajen 3

## Unidade Aprendizajen 3: Dispositivus Rede no Sira-nia Fungsaun
- Objetivus:
  * Identifika dispositivus rede komuns
  * Esplika fungsaun hosi hubs, switches, no routers
- Topikus:
  * Hubs no repeaters
  * Switches no bridges
  * Routers no gateways
- Atividades:
  * Ezersisiu práktiku: Konfigura rede LAN ki'ik ho dispositivus ne'ebé disponivel
  * Peskiza kona-ba dispositivus rede ne'ebé uza iha instituisaun Timor-Leste

## Rekursu Unidade

# Nótus Aula

## Hubs no Repeaters

### Definisaun no Fungsaun Báziku
- Hub mak dispositivu báziku networking ne'ebé funsiona iha kama fíziku (Kamada 1) husi modelu OSI
- Nia hanesan pontu ligasaun sentrál ba dispositivus iha rede
- Hubs simple hodi broadcast dadus ne'ebé mai ba dispositivus hotu-hotu ne'ebé konekta

### Transmisaun Dadus Liuhusi Hub
- Bainhira dispositivu haruka dadus liuhusi hub:
  1. Hub simu dadus iha portu ida
  2. Nia regenera sinál atu mantein forsa sinál
  3. Dadus depois haruka ba portus hotu-hotu seluk
- Prosesu ida ne'e hanaran "flooding"

### Limitasaun Hosi Hubs
- Kolizaun: Dispositivus barak bele transmite iha momentu hanesan, halo kolizaun dadus
- Domíniu kolizaun ida: Portus hotu iha hub fahe domíniu kolizaun ida deit
- Fahe bandwidth: Dispositivus hotu-hotu ne'ebé konekta fahe bandwidth total
- Preokupasaun seguransa: Dadus haruka ba dispositivus hotu-hotu, maske la destina ba sira

### Repeaters
- Hanesan ho hubs, maibé normalmente uza hodi aumenta kampu rede
- Amplifika no regenera sinál hodi halo kontra degradasaun sinál iha distánsia longu

## Switches no Bridges

### Definisaun no Fungsaun Báziku
- Switches funsiona iha kama ligasaun dadus (Kamada 2) husi modelu OSI
- Sira kria domíniu kolizaun separadu ba kada portu
- Switches uza enderesu MAC hodi haruka dadus de'it ba destinatáriu indikadu

### Komparasaun ho Hubs
- Switches liu inteligente duke hubs
- Sira bele aprende kona-ba dispositivus ne'ebé konekta ba portus sira
- Switches hamenus congestion rede liuhusi kria domíniu kolizaun separadu

### Tabela Enderezu MAC
- Switches mantein tabela enderezu MAC (mós hanaran hanesan tabela forwarding)
- Tabela map enderezu MAC ba portus espesífiku
- Switches aprende enderezu MAC liuhusi analiza enderezu fonte husi frames ne'ebé mai

### Oinsá Switches Aprende
1. Bainhira frame to'o, switch grava enderezu MAC fonte no portu ne'ebé nia mai husi
2. Se enderezu MAC destinasaun hatene ona, frame haruka de'it ba portu ne'ebé
3. Se la hatene, frame haruka ba portus hotu-hotu tuir mai husi nia mai
4. Iha tempu, switch harii mapa kompletu husi rede

### Benefísiu Switches Liuhusi Hubs
- Melhoria dezempeñu: Hamenus kolizaun no uza efisiente bandwidth
- Seguransa aas: Dadus haruka de'it ba destinatáriu indikadu
- Eskalabilidade: Switches bele maneja rede boot liu efetivamente

## Routers no Gateways

### Definisaun no Fungsaun Báziku