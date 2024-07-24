'# Konseitu Networking Camada 3

Camada 3, mós konhesidu hanesan Camada Rede, mak camada terseiru husi modelu OSI. Nia responsável ba enderesamentu lójiku no enkaminhamentu pakote dadus entre rede sira ne'ebé diferente. Camada Rede garante katak dadus enderesadu ho loloos no haruka ba destinu ne'ebé planeadu, maske dispositivu hosi fonte no destinu iha rede sira ne'ebé diferente. Iha papel ida ne'e, ami sei esplora konseitu sira ne'ebé importante kona-ba networking Camada 3, inklui enderesamentu IP (IPv4 no IPv6), fundamentu subnetting, konseitu routing, no Tradusaun Endereçus Rede (NAT) no Tradusaun Endereçus Portu (PAT).

## Endereçamentu IP (IPv4 no IPv6)

Endereçus Internet Protocol (IP) mak endereçus lójiku ne'ebé atribuí ba dispositivu sira iha rede ida atu identifika sira ho maneira úniku no habilita komunikasaun entre sira. Iha versão rua prinsipál hosi endereçus IP: IPv4 no IPv6.

### Endereçamentu IPv4

Endereçus IPv4 mak endereçus 32-bit ne'ebé reprezenta iha nota desimal pontuadu, ne'ebé konsiste iha oktet haat ne'ebé separa husi períodu (por ezemplu, 192.168.1.1). Kada oktet varia husi 0 too 255, permitindu total aproximadamente 4.3 biliaun endereçus úniku.

Endereçus IPv4 divide iha parte rua: parte rede no parte hospe. Parte rede identifika rede ne'ebé dispositivu pertense, bainhira parte hospe identifika dispositivu espesífiku ida iha rede ne'e. Divisaun entre parte rede no hospe determina husi máskara subnet, ne'ebé mak valor 32-bit ne'ebé tapa parte hospe hosi endereçus.

Endereçus IPv4 divide iha klase lima (A, B, C, D, no E) bazeia ba valor hosi oktet primeiru. Klase A, B, no C uza ba enderesamentu unicast, bainhira Klase D uza ba multicast no Klase E rezerva ba fins experimentais.

### Endereçamentu IPv6

Endereçus IPv6 mak endereçus 128-bit ne'ebé reprezenta iha nota hexadecimal, ne'ebé konsiste iha grupu ualu husi díjitu hexadecimal haat ne'ebé separa husi kólun (por ezemplu, 2001:0db8:85a3:0000:0000:8a2e:0370:7334). IPv6 introdus ba endereçamentu esgotamentu hosi IPv4 no fornese espasu endereçus boot liu.

Endereçus IPv6 divide iha parte rua: prefixu rede no identifikadór interface. Prefixu rede identifika rede ne'ebé dispositivu pertense, bainhira identifikadór interface identifika dispositivu espesífiku ida iha rede ne'e. IPv6 uza nota durasaun prefixu (por ezemplu, /64) atu hatudu númeru díjitu iha prefixu rede.

Endereçus IPv6 bele abrevia liuhusi omiti zero sira ne'ebé lidera iha kada grupu no substitui grupu zero sira ne'ebé seguidu ho kólun duplu (::). Por ezemplu, endereçus 2001:0db8:0000:0000:0000:8a2e:0370:7334 bele hakerek hanesan 2001:db8::8a2e:370:7334.

## Fundamentu Subnetting

Subnetting mak prosesu husi divide rede boot liu iha subrede sira ne'ebé ki'ik liu (subnets) atu hadi'a desempeñu rede, seguransa, no jestaun. Subnetting permite administradór rede sira

'Encaminhamento

O encaminhamento dinâmico utiliza protocolos de encaminhamento para trocar automaticamente informações de encaminhamento entre roteadores. Roteadores aprendem sobre redes de seus vizinhos e atualizam suas tabelas de roteamento de acordo. O encaminhamento dinâmico é mais expansível e adaptável que o encaminhamento estático, tornando-o adequado para redes maiores e mais complexas.

Os protocolos de encaminhamento dinâmico comuns incluem:

- RIP (Protocolo de Informações de Roteamento): Um protocolo de vetor de distância que usa a contagem de hops como sua métrica.
- OSPF (Open Shortest Path First): Um protocolo de estado de link que usa o custo como sua métrica e suporta design de rede hierárquica.
- EIGRP (Enhanced Interior Gateway Routing Protocol): Um protocolo híbrido que combina características de protocolos de vetores de distância e estados de link, oferecendo rápida convergência e uso eficiente de largura de banda.

## NAT e PAT

Network Address Translation (NAT) e Port Address Translation (PAT) são técnicas usadas para conservar endereços IP públicos e permitir a comunicação entre redes privadas e públicas.

### NAT

NAT permite que vários dispositivos em uma rede privada compartilhem um único endereço IP público. Quando um dispositivo na rede privada envia um pacote para a rede pública, o roteador NAT substitui o endereço IP de origem privado pelo seu próprio endereço IP público. Quando o pacote de resposta chega, o roteador NAT traduz o endereço IP público de volta para o endereço IP privado original e encaminha o pacote para o dispositivo apropriado.

NAT ajuda a conservar endereços IP públicos e fornece um nível de segurança ao ocultar a estrutura da rede interna da rede pública.

### PAT

Port Address Translation (PAT), também conhecido como NAT overloading, é uma extensão do NAT que permite que vários dispositivos compartilhem um único endereço IP público e porta. PAT usa números de porta de origem únicos para distinguir entre diferentes conexões do mesmo endereço IP privado.

Quando um dispositivo na rede privada envia um pacote para a rede pública, o roteador PAT substitui o endereço IP de origem privado e a porta pelo seu próprio endereço IP público e uma porta de origem única. O roteador PAT mantém uma tabela de tradução para rastrear os mapeamentos entre endereços IP privados e públicos e portas.

PAT é comumente usado em redes domésticas e de pequenos escritórios, onde um único endereço IP público é atribuído pelo Provedor de Serviços de Internet (ISP).

## Demonstração: Usando os Comandos 'ip addr' e 'ip route'

No Linux, os comandos 'ip addr' e 'ip route' são usados para visualizar e configurar endereços IP e tabelas de roteamento.

### Visualizando Endereços IP

Para visualizar os endereços IP atribuídos às interfaces de rede, use o comando 'ip addr show':

```bash
ip addr show
```

Este comando exibe uma lista de todas as interfaces de rede e seus endereços IP associados, juntamente com informações adicionais como o endereço link-local, endereço de transmissão e máscara de rede.

### Configurando Endereços IP

Para atribuir um endereço IP a uma interface de rede, use o comando 'ip addr add':

```bash
ip addr add 192.168.1.10/24 dev eth0
```

Este comando atribui o endereço IP 192.168.1.10 com uma máscara de sub-rede de 255.255.255.0 (comprimento de prefixo /24) à interface eth0.

### Visualizando a Tabela de Roteamento

Para visualizar a tabela de roteamento, use o comando 'ip route show':

```bash
ip route show
```

Este comando exibe a tabela de roteamento atual, incluindo as redes de destino, gateways e métricas.

### Configurando Rotas Estáticas

Para adicionar uma rota estática, use o comando 'ip route add':

```bash
ip route add 192.168.2.0/24 via 10.0.0.2
```

Este comando adiciona uma rota estática para a rede 192.168