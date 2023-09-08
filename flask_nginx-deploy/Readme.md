#Description
Um servidor web Nginx com balanceamento de carga distribuindo o tráfego 60% para o Container app:1 e 40% para o Container app:2. Retornando uma aplicação Flask que disponibiliza um cartão postal de duas cidades do nordeste brasileiro.

#Requeriments
Flask=2.3.3
Docker-compose=2.5.0
Docker=24.0.6
Python=3

#Nginx Load-Balancer arquitecture 
app1 = 60% of traffic
app2 = 40% of traffic
