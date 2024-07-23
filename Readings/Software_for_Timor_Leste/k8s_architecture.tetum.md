Títulu: Arquitetura Kubernetes: Explorasaun Detalladu Modelu Mestre-Node

Introdusaun

Kubernetes, plataforma orkestrasaun kontainer líder, uza arquitetura mestre-node sofistikadu atu maneja aplikasaun kontainer nian iha eskala boot. Arquitetura ida ne'e habilita Kubernetes atu fornese orkestrasaun kontainer ne'ebé forte, bele aumenta, no resistente ba falha. Papel ida ne'e sei hetan esplorasaun ba komplikasaun sira husi arquitetura ida ne'e, detalha komponente sira husi mestre no node traballador sira nian no interasaun sira.

Vista Jerál Arquitetura Kubernetes

Kubernetes uza arquitetura distribuída ne'ebé mak hatene hanesan modelu mestre-node. Modelu ida ne'e konsiste iha mestre node ida (mós hatene hanesan planu kontrolu) no traballador node barak. Mestre node mak responsável ba jestaun kluster, no traballador node sira mak halao aplikasaun kontainer nian.

Mestre Node (Planu Kontrolu)

Mestre node, refere dala barak hanesan planu kontrolu, mak serebro husi kluster Kubernetes. Nia halo desizaun globál kona-ba kluster no deteta no responde ba eventu kluster nian. Mestre node iha komponente importante hirak ne'e:
3.1 Servidor API

Hanesan front-end ba planu kontrolu Kubernetes
Eksplika API Kubernetes
Prosesa operasaun REST no halo update ba objetu sira ne'ebé koresponde iha etcd
Hanesan pontu jestaun prinsipál ba kluster tomak
Valida no konfigura dadus ba objetu API sira hanesan pods, servisu sira, no kontrolador replikasaun

3.2 Scheduler

Hare ba pod foun sira ne'ebé laiha node atribuído no hili node ida ba sira atu halo servisu
Konsidera rekizitu rekursu individuál no kolektivu, limitasaun hardware/software/polítika, spesifikasaun afinidade no anti-afinidade, lokalidade dadus, no liu tan
Halo desizaun agenda bazeia ba algoritmu komplexu ne'ebé konsidera fator sira ne'e

3.3 Jestaun Kontrolador

Halao prosesu kontrolador nian ne'ebé regula estadu sistema
Inklui Kontrolador Node, Kontrolador Replikasaun, Kontrolador Ponta Final, no Kontrolador Kuenta Servisu & Token
Hare estadu kompartilhada kluster nian liu husi servidor API no halo mudansa atu muda estadu atual ba estadu desejadu

3.4 etcd

Armazenamentu xave-valór konsistente no iha disponibilidade aas uza hanesan armazenamentu suporte ba dadus kluster hotu-hotu Kubernetes
Armazena dadus konfigurasaun no informasaun kona-ba estadu kluster
Implementa forma ida husi algoritmu konsensus Raft atu asegura konsistensia dadus liu husi node barak

Traballador Node sira

Traballador node sira, mós hatene hanesan minions, mak mákina sira ne'ebé halao aplikasaun kontainer nian. Sira bele komputador físiku ka mákina virtual, depende ba kluster. Kada node jestionadu husi mestre no iha servisu sira ne'ebé presiza atu halao kontainer aplikasaun nian. Komponente importante husi traballador node mak:
4.1 Kubelet

Ajente node prinsipál ne'ebé halao iha kada node
Asegura katak kontainer sira halao iha pod ida
Halo uzu conjunto PodSpecs ne'ebé fornese liu husi mekanismu oioin no asegura katak kontainer sira ne'ebé deskreve iha PodSpecs sira ne'e halao no iha kondisaun di'ak
Komunika ho servidor API mestre node nian atu simu komandu