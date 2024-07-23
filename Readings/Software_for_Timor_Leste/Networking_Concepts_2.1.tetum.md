'# Konseitu Networking Layer 2

Layer 2, mós konhesidu hanesan Data Link layer, mak layer segundu husi modelu OSI. Nia responsavel ba transferénsia fiar husi dadus entre dispositivus rua ne'ebé konekta direita ba malu iha rede. Data Link layer garante katak dadus formatu di'ak, endereçadu no entrega laho erru. Iha papel ida ne'e, ita sei explora konseitu sira importante relasiona ho networking Layer 2, inklui MAC addresses, Ethernet frames, switches no bridging, no VLANs.

## MAC Addresses

Media Access Control (MAC) addresses mak identifikadores únika ne'ebé atribui ba network interface cards (NICs) husi sira-nia fabrikante. MAC address mak address bit 48 ne'ebé reprezenta iha notasaun hexadecimal, normalmente iha formatu "XX:XX:XX:XX:XX:XX" ne'ebé kada "X" mak digitu hexadecimal.

MAC addresses funsiona iha Data Link layer no uza atu identifika dispositivus dentro de segmentu rede ida. Diferente husi IP addresses, ne'ebé mak addresses lójika ne'ebé atribui husi administradores rede, MAC addresses mak baseia iha hardware no permanese fixu ba NIC.

Bainhira dispositivu ida haruka dadus iha rede, nia inklui MAC address destinatáriu iha header frame. Dispositivu ne'ebé simu verifica MAC address destinatáriu atu determina se frame mak destina ba nia. Se address koresponde, dispositivu simu frame; se lae, nia rejeita.

## Ethernet Frames

Ethernet frames mak unidade báziku transmisaun iha Data Link layer iha rede Ethernet. Ethernet frame enkapsula dadus husi layers iha leten no adiciona informasaun header Layer 2 ba entrega ba dispositivu destinatáriu.

Estrutura husi Ethernet frame inklui:

- Preamble: Sekuénsia alternada husi 1s no 0s ne'ebé ajuda atu sinkroniza relójiu husi simu.
- Start Frame Delimiter (SFD): Marca hahú frame.
- Destination MAC Address: MAC address husi destinatáriu.
- Source MAC Address: MAC address husi dispositivu ne'ebé haruka.
- EtherType/Length: Indika protokolu ne'ebé uza iha layer iha leten (ex: IPv4, IPv6, ARP) ka komprimentu frame.
- Payload: Dadus atuál ne'ebé transmite, normalmente husi Network layer no iha leten.
- Frame Check Sequence (FCS): Checksum ne'ebé uza atu detekta erru.

Bainhira dispositivu ida haruka Ethernet frame, nia kria frame ho informasaun header apropriadu no transmite iha média rede. Dispositivu ne'ebé simu examina frame, verifica erru ho FCS, no prosesa frame baseia iha MAC address destinatáriu.

## Switches no Bridging

Switches mak dispositivus Layer 2 ne'ebé uza MAC addresses atu enkaminha frames entre dispositivus iha rede ida. Sira funsiona liuhosi manutensaun tabela MAC address, ne'ebé mapeia MAC addresses ba portus switch nian ne'ebé sira lokaliza.

Bainhira switch simu Ethernet frame, nia examina MAC address fonte no atualiza tabela MAC address ho informasaun portu korespondente. Nia buka MAC address destinatáriu iha tabela atu determina portu output apropriadu. Se MAC address destinatáriu la hetan iha tabela, switch distribui frame liu husi hotu portus no la inklui ne'ebé nia simu.

Prosesu ida ne'e aprende MAC addresses no enkaminha frames baseia iha tabela MAC address mak hanesan bridging. Switches ponte frames entre segmentu rede sira ne'ebé diferente, hadi'a desempeñu rede no redus dominu kolizaun.

Diferente husi hubs, ne'ebé funsiona iha Layer 1 no simplismente emite frames ba dispositivus hotu ne'ebé konekta, switches enkaminha