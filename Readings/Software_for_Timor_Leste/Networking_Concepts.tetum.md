'# Konseitu Networking Camada 2

Camada 2, mós konhesidu hanesan Camada Ligasaun Dadus, mak camada daruak husi modelu OSI. Nia responsável ba transferénsia fiar husi dadus entre aparénsia rua ne'ebé konekta diretamente iha rede. Camada Ligasaun Dadus asegura katak dadus ne'ebé formata, endereza, no entrega ho loke laho erros. Iha artigu ida ne'e, ita sei esplora konseitu importante balu relasiona ho networking Camada 2, inklui enderesu MAC, quadru Ethernet, switches no bridging, no VLANs.

## Endereços MAC

Endereçus Media Access Control (MAC) mak identifikadores úniku ne'ebé atribui ba karta interface rede (NICs) husi sira-nia fabrikante. Endereçu MAC ida mak endereçu bit 48 ne'ebé reprezenta iha notasaun hexadecimal, normalmente iha formatu "XX:XX:XX:XX:XX:XX" iha ne'ebé kada "X" mak digitu hexadecimal.

Endereçus MAC operasaun iha Camada Ligasaun Dadus no uza hodi identifika aparénsia iha segmentu rede ida. Diferente husi endereçus IP, ne'ebé mak endereçus lójika ne'ebé atribui husi administrador rede, endereçus MAC mak bazeia iha hardware no fixa ba NIC.

Bainhira aparénsia ida haruka dadus iha rede, nia inklui endereçu MAC destinatáriu iha header quadru. Aparénsia ne'ebé simu tau matan ba endereçu MAC destinatáriu hodi determina se quadru ne'e intendi ba nia. Se endereçu koiniside, aparénsia simu quadru; se lae, nia halo de'it hamlaha.

## Quadru Ethernet

Quadru Ethernet sira mak unidade báziku ba transmisaun iha Camada Ligasaun Dadus iha rede Ethernet. Quadru Ethernet ida kapsula dadus husi camada aas liu no kria informasaun header Camada 2 ba entrega ba aparénsia destinatáriu.

Estrutura quadru Ethernet inklui:

- Preamble: Sekuénsia ida husi 1s no 0s ne'ebé ajuda hodi sinkroniza relójiu simu nian.
- Delimitador Hahú Quadru (SFD): Marca hahú quadru nian.
- Endereçu MAC Destinatáriu: Endereçu MAC husi destinatáriu.
- Endereçu MAC Fonte: Endereçu MAC husi aparénsia ne'ebé haruka.
- EtherType/Naruk: Indika protokolu ne'ebé uza iha camada aas (exemplu: IPv4, IPv6, ARP) ka naruk quadru nian.
- Payload: Dadus atual ne'ebé transmite, normalmente husi Camada Rede no aas.
- Sekuénsia Verifikasaun Quadru (FCS): Checksum ida ba deteksaun erros.

Bainhira aparénsia ida haruka quadru Ethernet, nia kria quadru ho informasaun header apropriadu no transmite iha média rede. Aparénsia simu tau matan ba quadru, tau matan ba erros uza FCS, no prosesa quadru bazeia ba endereçu MAC destinatáriu.

## Switches no Bridging

Switches sira mak aparénsia Camada 2 ne'ebé uza endereçus MAC hodi enkaminha quadru entre aparénsia sira iha rede ida. Sira operasaun liu husi manutensaun tabela endereçu MAC, ne'ebé mapeia endereçus MAC ba portus switch nian iha ne'ebé sira lokaliza.

Bainhira switch ida simu quadru Ethernet, nia tau matan ba endereçu MAC fonte no atualiza tabela endereçu MAC nian ho informasaun portu korespondente. Nia depois buka endereçu MAC destinatáriu iha tabela hodi determina portu saída ne'ebé a