'Unidade Aprendizajen 5

Unidade Aprendizajen 5: Endereçamento IP no Subnetting
- Objetivos:
  * Hakomprende endereçamento IP (IPv4 no IPv6)
  * Aprende técnicas báziku subnetting
- Tópikus:
  * Klase endereçamento IP
  * Máscaras Subnet
  * Notação CIDR
- Atividades:
  * Exercícios de endereçamento IP no subnetting
  * Analiza alokasaun IP iha rede governu Timor-Leste

Rekursus Unidade

Nota Aula

Introdução ao Endereçamento IP

Objetivo de Endereços IP
- Endereços IP são identificadores únikus ba dispositivus numa rede
- Permite dispositivus atu haruka no simu dadus liuhusi rede
- Esensiál ba encaminhamentu paketes ba sira nia destinu korretu

IPv4 vs IPv6
- IPv4: Endereços de 32 bits, eskritu hanesan oktetu haat (ex., 192.168.1.1)
- IPv6: Endereços de 128 bits, eskritu iha hexadecimal (ex., 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
- IPv6 dezenvolve atu halo adresu IPv4 la maran

Estrutura Endereçamento IPv4

Endereços de 32 bits
- Kompostu husi 32 dízitu bináriu (0s no 1s)
- Divide ba oktetu haat de 8 bits

Notação Decimal Pontuada
- Kada oktetu reprezenta hanesan númeru decimal (0-255)
- Númeru haat separa husi pontus (ex., 192.168.1.1)

Klase Endereçamento IP

Klase A
- Bit primeiru sempre 0
- Ranggu: 0.0.0.0 too 127.255.255.255
- Máskara subnet default: 255.0.0.0

Klase B
- Dois bits primeiru sempre 10
- Ranggu: 128.0.0.0 too 191.255.255.255
- Máskara subnet default: 255.255.0.0

Klase C
- Tolu bits primeiru sempre 110
- Ranggu: 192.0.0.0 too 223.255.255.255
- Máskara subnet default: 255.255.255.0

Klase D no E
- Klase D: Endereços Multicast (224.0.0.0 too 239.255.255.255)
- Klase E: Rezervadu ba uzu experimental (240.0.0.0 too 255.255.255.255)

Máscaras Subnet

Objetivu
- Determina parte ida husi endereçamento IP refere ba rede no parte ida refere ba hospedeiru
- Uza ho endereçamento IP atu define rede

Máscaras Subnet default
- Klase A: 255.0.0.0
- Klase B: 255.255.0.0
- Klase C: 255.255.255.0

Notação CIDR

Definisaun
- Classless Inter-Domain Routing
- Métodu ne'ebé liu flexível atu aloka endereçamento IP

Representasaun
- Endereçamento IP tuir husi barra too karuk no númeru (ex., 192.168.1.0/24)
- Númeru reprezenta númeru bits iha parte rede husi endereçamento

Exemplu
- 192.168.1.0/24 (ekuivalente ba máskara subnet 255.255.255.0)
- 10.0.0.0/8 (ekuivalente ba máskara subnet 255.0.0.0)

Konseitus Báziku Subnetting

Objetivu Subnetting
- Divide rede boot ba subrede kiik liu, ne'ebé bele maneja liu
- Hadia performansa no seguransa rede
- Optimize alokasaun endereçamento IP

Kria Subnets