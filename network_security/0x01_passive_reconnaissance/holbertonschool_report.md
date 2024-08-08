Para esta tarea, necesitamos que recopile la mayor cantidad de información posible sobre el dominio holbertonschool.com usando Shodan*

* Recopile todos los rangos de IP dentro del dominio holbertonschool.com
* Recopile las tecnologías y los marcos utilizados dentro de todos los subdominios de holbertonschool.com
* Redacte sus notas como un informe en formato Markdown.

usage: ping holbertonschool.com -c 4

PING holbertonschool.com (75.2.70.75) 56(84) bytes of data.
64 bytes from aacb0a264e514dd48.awsglobalaccelerator.com (75.2.70.75): icmp_seq=1 ttl=244 time=17.4 ms
64 bytes from aacb0a264e514dd48.awsglobalaccelerator.com (75.2.70.75): icmp_seq=2 ttl=244 time=17.1 ms
64 bytes from aacb0a264e514dd48.awsglobalaccelerator.com (75.2.70.75): icmp_seq=3 ttl=244 time=18.7 ms
64 bytes from aacb0a264e514dd48.awsglobalaccelerator.com (75.2.70.75): icmp_seq=4 ttl=244 time=17.0 ms

--- holbertonschool.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3006ms
rtt min/avg/max/mdev = 17.009/17.559/18.714/0.685 ms

usage: shodan host 75.2.70.75

Hostnames:               aacb0a264e514dd48.awsglobalaccelerator.com;sumthing.org
City:                    Seattle
Country:                 United States
Organization:            Amazon.com, Inc.
Updated:                 2024-08-08T19:02:13.409986
Number of open ports:    2

Ports:
     80/tcp
        |-- HTTP title: 301 Moved Permanently
    443/tcp
        |-- HTTP title: 301 Moved Permanently
        |-- Cert Issuer: C=US, CN=R11, O=Let's Encrypt
        |-- Cert Subject: CN=sumthing.org
        |-- SSL Versions: -SSLv2, -SSLv3, -TLSv1, -TLSv1.1, TLSv1.2, TLSv1.3

