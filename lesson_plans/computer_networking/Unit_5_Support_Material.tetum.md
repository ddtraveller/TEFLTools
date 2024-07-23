Iha ne'e mak materiais suporte ba lição de IP Addressing no Subnetting, formatu iha Markdown:

# Materiais Suporte ba Lição de IP Addressing no Subnetting

## 1. Lista Vokabulariu Prinsipal ho Definisaun

- **Endereçu IP**: Numeru uniku ida ne'ebé atribui ba kada dispositivu iha rede komputador
- **IPv4**: Versaun dahuluk husi Protocolo Internet, uza endereçus 32-bit
- **IPv6**: Versaun neen husi Protocolo Internet, uza endereçus 128-bit
- **Subnet**: Divizão lógika ida husi rede IP
- **Máskara Subnet**: Numeru 32-bit ida ne'ebé máskara endereçu IP, divide ba parte rede no parte host
- **CIDR (Classless Inter-Domain Routing)**: Métodu ida ba alokasaun endereçus IP no routing pakotes IP
- **ID Rede**: Parte husi endereçu IP ne'ebé identifika rede
- **ID Host**: Parte husi endereçu IP ne'ebé identifika dispositivu espesifiku iha rede
- **Octet**: Grupu husi bit walu, uza iha endereçamentu IPv4
- **Endereçu Broadcast**: Endereçu espesial ida uza hodi haruka dadus ba dispositivus hotu iha rede

## 2. Ajudas Visuais ka Diagramas

1. Diagrama Estrutura Endereçu IPv4:
   ```
   [Octet 1] . [Octet 2] . [Octet 3] . [Octet 4]
   [8 bits]    [8 bits]    [8 bits]    [8 bits]
   ```

2. Tabela Klases Endereçu IP:
   ```
   Klase | Intervalu Primeiru Octet | Máskara Subnet Default
   ------|-------------------|---------------------
   A     | 1-126             | 255.0.0.0
   B     | 128-191           | 255.255.0.0
   C     | 192-223           | 255.255.255.0
   D     | 224-239           | (Multicast)
   E     | 240-255           | (Reservadu)
   ```

3. Diagrama Subnetting:
   ```
   Rede Orijinal: 192.168.1.0/24
   Subnets:
   [192.168.1.0/26] [192.168.1.64/26] [192.168.1.128/26] [192.168.1.192/26]
   ```

## 3. Handouts ka Worksheets

1. Exercicio Klasifikasaun Endereçu IP:
   - Lista husi 10 endereçus IP ba estudantes hodi klasifika (Klase A, B, C, D, ka E)
   - Espaço ba estudantes hodi hakerek klase no esplika sira nia pensamentu

2. Emparelhamentu Máskara Subnet:
   - Tabela ho tamanhos rede no máskaras subnet korespondente hodi emparelha

3. Konversaun Notasaun CIDR:
   - Lista husi endereçus IP ho máskaras subnet tradisional hodi konverte ba notasaun CIDR
   - Lista husi endereçus IP iha notasaun CIDR hodi konverte ba máskaras subnet tradisional

4. Worksheet Subnetting:
   - Fornese endereçu rede no numeru subnets presiza, estudantes kalkula:
     * Máskara subnet
     * Numeru endereçus host kada subnet
     * Endereçus subnet
     * Primeiru no ikus endereçus host ne'ebé uza iha kada subnet
     * Endereçus broadcast ba kada subnet

## 4. Recursos Adisionais ba Leitura ka Prátika Adisional

1. Kalkuladora Subnet IP Online: https://www.calculator.net/ip-subnet-calculator.html
2. Guia Cisco "Endereçamentu IP no Subnetting ba Utilizadores Foun": https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html
3. "