# Domain Analysis Report for `holbertonschool.com`

## 1. IP Address Range
Get the domain's IP address (if we don't have it yet):
 - whit the dig command:
```
dig +short holbertonschool.com

75.2.70.75
99.83.190.102
```

 - whit the host command:
```
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

Once we have the IP address, we use whois to obtain details about the assigned IP range

Below are the IP addresses and ranges associated with the domain `holbertonschool.com`:

- **IP Ranges**:
  - whit the whois command:
  ```
  whois 75.2.70.75
  NetRange:       75.2.0.0 - 75.2.191.255
  CIDR:           75.2.0.0/17, 75.2.128.0/18
  ```
- **IP Ranges**:
  - whit the whois command:
  ```
  whois 99.83.190.102
  NetRange:       99.83.64.0 - 99.84.255.255
  CIDR:           99.84.0.0/16, 99.83.64.0/18, 99.83.128.0/17
  ```

## 2. Technologies and Frameworks Used

### Subdominio: `www.holbertonschool.com` (using the Shodan tool)
- **Servidor Web**: Nginx
- **Autenticación**: OpenSSH
- **Sistema Operativo**: Ubuntu
- **Message boards**: Discourse
- **Programming languages**: Ruby
- **Framework**: Ruby on Rails

## 3. Aditional remarks

- **Security**: Some subdomains may display vulnerabilities in Shodan, such as outdated software versions.

## 4. Conclusions

This analysis reveals that `holbertonschool.com` uses a variety of technologies and frameworks on different subdomains.
