'# Konseitu Networking Camada 2

Camada 2, mós konhesidu nudar Data Link layer, mak camada segundu husi modelu OSI. Nia responsabilidade mak transfere dadus ho fiar entre dispositivo rua ne'ebé konekta diretamente iha rede. Data Link layer garante dadus formatu ho diak, endereçu adekuadu, no entrega laho error. Iha papel ida ne'e, ita sei esplora konseitu balun importante kona-ba Camada 2 Networking, inklui MAC addresses, Ethernet frames, switches no bridging, no VLANs.

## MAC Addresses

Media Access Control (MAC) addresses mak identifikador uniku ne'ebé atribui ba network interface cards (NICs) husi sira-nia produsente. MAC address mak address ida ho 48-bit ne'ebé reprezenta iha notasaun hexadecimal, normalmente iha formatu "XX:XX:XX:XX:XX:XX" ne'ebé kada "X" mak digitu hexadecimal.

MAC addresses funsiona iha Data Link layer no uja hodi identifika dispositivo sira iha segmentu rede ida. Diferente husi IP addresses, ne'ebé mak address lójiku ne'ebé atribui husi administrador rede, MAC addresses mak baseia ba hardware no kleur ba NIC.

Bainhira dispositivo ida haruka dadus iha rede, nia inklui MAC address destinatariu iha header frame. Dispositivo ne'ebé simu ne'e sei fo verifikasaun ba MAC address destinatariu hodi determina se frame ne'e destina ba nia. Se address tuir, dispositivo ne'e sei simu frame; se lae, nia sei hasai.

## Ethernet Frames

Ethernet frames mak unidade báziku husi transmisaun iha Data Link layer iha rede Ethernet. Ethernet frame kápsula dadus husi camada superior no adiciona informasaun header Camada 2 ba entrega ba dispositivo destinatariu.

Estrutura husi Ethernet frame inklui:

- Preamble: Sekuénsia husi 1s no 0s ne'ebé alterna hodi ajuda sinkroniza relójiu husi receiver.
- Start Frame Delimiter (SFD): Marka hahú husi frame.
- Destination MAC Address: MAC address husi destinatariu ne'ebé planea.
- Source MAC Address: MAC address husi dispositivo ne'ebé haruka.
- EtherType/Komprimentu: Indika protokolu ne'ebé uza iha camada superior (exemplu, IPv4, IPv6, ARP) ka komprimentu frame.
- Payload: Dadus real ne'ebé transmite, normalmente husi Camada Rede no iha leten.
- Frame Check Sequence (FCS): Checksum ida ne'ebé uza ba deteksaun error.

Bainhira dispositivo ida haruka Ethernet frame, nia konstrui frame ho informasaun header ne'ebé apropriadu no transmite iha média rede. Dispositivo ne'ebé simu sei analiza frame, verifika error uza FCS, no prosesa frame bazeia ba MAC address destinatariu.

## Switches no Bridging

Switches mak dispositivo Camada 2 ne'ebé uza MAC addresses hodi haruka frames entre dispositivo sira iha rede ida. Sira funsiona liu husi manutensaun tabela MAC address, ne'ebé mapeia MAC addresses ba portu switch ne'ebé sira iha.

Bainhira switch simu Ethernet frame, nia analiza MAC address fonte no atualiza tabela MAC address ho informasaun portu ne'ebé tuir. Nia depois buka MAC address destinatariu iha tabela hodi determina portu output ne'ebé apropriadu. Se MAC address destinatariu la iha tabela, switch sei haruka frame liu husi hotu-hotu portu, esepke portu ne'ebé simu.

Prosesu ida ne'e, ne'ebé aprende MAC addresses no haruka frames bazeia ba tabela MAC address, mak konhesidu nudar bridging. Switches iha esénsia ponte frames entre segmentu diferente iha rede, muda performansa rede no redus dominio kolizaun.

Diferente husi hub, ne'ebé funsiona iha Camada 1 no simu frames ba hotu-hotu