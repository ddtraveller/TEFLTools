'Unidade Aprendizajen 7

Unidade Aprendizajen 7: Konfigurasaun Rede no Seguransa
- Objetivu:
  * Konfigura settings rede báziku
  * Implementa práktika seguransa fundamentál
- Tópiku:
  * Ferramenta konfigurasaun rede (ip, nmcli)
  * Báziku firewall (iptables, firewalld)
  * Konfigurasaun SSH no autentikasaun bazeia ba xave
- Atividade:
  * Konfigura settings rede ba rede ofisina ki'ik
  * Hestabelese autentikasaun bazeia ba xave SSH no desativa login password

Rekursu Presiza

- Komputadór ne'ebé bele halao Linux (nativamente ka iha mákina virtual)
- Asesu ba distribuisaun Linux (Ubuntu ka CentOS rekomenda)
- "The Linux Command Line" husi William Shotts
- "Linux Administration: A Beginner's Guide" husi Wale Soyinka

Sujestaun Itens ba Kobre

- Diferensa distribuisaun Linux no hili di'ak ida ba nesesidade Timor Leste
- Lisensa software fonte aberta no nia implikasaun
- Rekursu komunidade Linux no kanal suporta

Ezperiénsia Prátika no Envolvimentu Komunidade

- Organiza "Linux Install Fest" ba komunidade lokál
- Kolabora ho kompañia lokál hodi identifika solusaun bazeia ba Linux ba sira nia nesesidade
- Partisipa iha ka organiza Grupu Uza Linux Lokál (LUG)
- Kontribui ba tradusaun dokumentasaun Linux ba Tetum

Rekursu Adisionál

- Projetu Dokumentasaun Linux (TLDP)
- Kursu online Linux Academy
- Forum komunidade Linux lokál no lista postál iha Timor Leste
- Alternativa livre no fonte aberta ba software proprietáriu komun iha Timor Leste

Rekursu Unidade

Nota Palestra

Konfigurasaun Rede

Uza Komandu 'ip'

Komandu 'ip' mak hanesan ferramenta ne'ebé makaas ba konfigurasaun interface rede iha Linux. Iha ne'e ita bele hatene uza di'ak liu:

- Haree interface rede: `ip link show`
- Haree enderesu IP: `ip addr show`
- Hatama enderesu IP: `ip addr add 192.168.1.10/24 dev eth0`
- Hasai enderesu IP: `ip addr del 192.168.1.10/24 dev eth0`
- Hahú ka para interface: `ip link set eth0 up` ka `ip link set eth0 down`

Uza `nmcli`

Interface linha komandu NetworkManager, `nmcli`, fornese maneira ne'ebé fásil ba uza atu jere koneksaun rede:

- Lista hotu-hotu koneksaun: `nmcli connection show`
- Ativa koneksaun: `nmcli connection up <naran-koneksaun>`
- Desativa koneksaun: `nmcli connection down <naran-koneksaun>`
- Kria koneksaun foun: `nmcli connection add type ethernet con-name "My Connection" ifname eth0`
- Modifika koneksaun: `nmcli connection modify "My Connection" ipv4.addresses 192.168.1.10/24`

Báziku Firewall

iptables

iptables mak hanesan utilidade firewall linha komandu ba Linux. Konseitu prinsipál:

- Tabela: filter, nat, mangle, raw
- Kadeia: INPUT, OUTPUT, FORWARD
- Regra: Konsiste husi koinidénsia no alvu

Komandu báziku iptables:

- Lista regra: `sudo iptables -L`
- Hatama regra: `sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT`
- Hasai regra: `sudo iptables -D INPUT 1`
- Hestabelese polítika default: `sudo iptables -P INPUT DROP`

firewalld

firewalld mak hanesan jestor firewall dinámiku ba Linux. Konseitu prinsipál:

- Zona: públiku, uma, servisu