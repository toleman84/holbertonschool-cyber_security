# Informe de Análisis del Dominio holbertonschool.com

## 1. Rango de Direcciones IP
Obtener la dirección IP del dominio (si aún no la tenemos):
```
dig +short holbertonschool.com

75.2.70.75
99.83.190.102
```

``` con el comando host:
host holbertonschool.com

holbertonschool.com has address 75.2.70.75
holbertonschool.com has address 99.83.190.102
holbertonschool.com mail is handled by 10 alt4.aspmx.l.google.com.
holbertonschool.com mail is handled by 5 alt1.aspmx.l.google.com.
holbertonschool.com mail is handled by 10 alt3.aspmx.l.google.com.
holbertonschool.com mail is handled by 5 alt2.aspmx.l.google.com.
holbertonschool.com mail is handled by 1 aspmx.l.google.com.
alt3.aspmx.l.google.com has address 142.250.153.27
```

Una vez teniendo la dirección IP, utilizamos whois para obtener detalles sobre el rango de IPs asignado

A continuación se detallan las direcciones IP y rangos asociados con el dominio `holbertonschool.com`:

- **IP Ranges**:
  ```
  - comando: whois 75.2.70.75
    - NetRange:       75.2.0.0 - 75.2.191.255
    - CIDR:           75.2.0.0/17, 75.2.128.0/18
  ```
- **IP Ranges**:
  ```
  - comando: whois 99.83.190.102
    - NetRange:       99.83.64.0 - 99.84.255.255
    - CIDR:           99.84.0.0/16, 99.83.64.0/18, 99.83.128.0/17
  ```

## 2. Tecnologías y Frameworks Utilizados

### Subdominio: `www.holbertonschool.com` (utilizando la herramienta Shodan)
- **Servidor Web**: Nginx
- **Autenticación**: OpenSSH
- **Sistema Operativo**: Ubuntu
- **Message boards**: Discourse
- **Programming languages**: Ruby
- **Framework**: Ruby on Rails

## 3. Observaciones Adicionales

- **Seguridad**: Algunos subdominios pueden mostrar vulnerabilidades en Shodan, como versiones desactualizadas de software.

## 4. Conclusiones

Este análisis revela que `holbertonschool.com` utiliza una variedad de tecnologías y frameworks en diferentes subdominios.
