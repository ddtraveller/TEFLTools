'# Atividades Aquecimento

## Quiz Seguransa Rede
1. Kria quiz lalais 5 pergunta kona-ba konseitu networking báziku:
   - Saida mak IP address?
   - Saida mak objetivu husi subnet mask?
   - Naran tolu port rede komún no sira-nia funsaun.
   - Saida mak diferença entre firewall no antivirus software?
   - Tanba sa SSH liu seguru duke Telnet?

## Diskusaun kona-ba Senáriu Seguransa
2. Apresenta senáriu: "Empreza ki'ik ida iha Dili hasoru problema rede ne'ebé akontese barak no suspeita katak iha ameasa seguransa. Saida mak pasu sira tenke halo atu investiga no seguru sira-nia rede?"
   - Halo estudante sira diskute iha grupu ki'ik durante minutu 5.
   - Fahe idea ho klase no kria lista aksaun potensial iha quadro branku.

# Atividades Lição Prinsipál

## Demonstrasaun Konfigurasaun IP
1. Demonstrasaun uza komandu `ip` atu haree no konfigura interface rede:
   - Hatudu konfigurasaun IP atuál: `ip addr show`
   - Aumenta foun IP address: `ip addr add 192.168.1.10/24 dev eth0`
   - Hasai IP address: `ip addr del 192.168.1.10/24 dev eth0`

## Kriasaun Regra Firewall
2. Hakat liu prosesu kria regra firewall báziku:
   - Ba iptables: `iptables -A INPUT -p tcp --dport 22 -j ACCEPT`
   - Ba firewalld: `firewall-cmd --zone=public --add-port=22/tcp --permanent`

## Jerasaun no Konfigurasaun SSH Key
3. Orienta estudante sira atu:
   - Jera par SSH key: `ssh-keygen -t rsa -b 4096`
   - Kopia chave públiku ba server: `ssh-copy-id user@server`
   - Konfigura SSH atu disativa autentikasaun password

# Tarefa Trabalha iha Grupu ka Par

## Dezafiu Dezain Rede
1. Iha par, dezain estrutura rede ba ofisina ki'ik iha Timor Leste:
   - Desenha diagrama rede
   - Atribui IP addresses no subnets
   - Lista regra firewall ne'ebé presiza
   - Apresenta ita-nia dezain ba par seluk no diskute diferensa

## Implementasaun Regra Firewall
2. Iha grupu tolu, implementa regra firewall hodi:
   - Permite tráfiku entrada SSH (portu 22)
   - Permite tráfiku saida HTTP no HTTPS (portu 80 no 443)
   - Blokeia tráfiku entrada hotu-hotu seluk
   - Testa regra no verifica katak sira funsiona hanesan esperado

# Exercisiu Prátika Individuál

## Konfigurasaun Rede
1. Konfigura ita-nia setting rede mákina:
   - Define IP address estátiku uza `ip` ka `nmcli`
   - Konfigura gateway default
   - Instala DNS servers

## Setup SSH Key
2. Jera par SSH key no setup autentikasaun bazeia ba chave:
   - Kria par chave
   - Konfigura cliente SSH atu uza chave
   - Disativa autentikasaun password iha konfigurasaun server SSH

## Konfigurasaun Firewall
3. Implementa konfigurasaun firewall báziku:
   - Permite tráfiku entrada iha portu 22, 80, no 443
   - Blokeia tráfiku entrada hotu-hotu seluk
   - Permite tráfiku saida hotu-hotu
   - Salva konfigurasaun atu kontinua depois reboot

# Atividades Arrefesimentu ka Konklusaun

## Diskusaun Prátika Di'ak Seguransa
1. Iha grupu ki'ik, kria lista prátika di'ak seguransa rede ba empreza iha Timor Leste:
   - Konsidera desafiu lokal no limitasaun