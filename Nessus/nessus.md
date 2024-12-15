# Nessus Scan Report
## Scan Configuration
### Scan Template Selection
The "Web Application Testing" template was selected for this exercise due to its specialized focus on identifying web application-related vulnerabilities such as misconfigurations, SQL injections, XSS, and TLS/SSL issues. This template allows for a comprehensive scan covering both technical vulnerabilities and specific web service configuration issues.

## Scan Settings Considerations:

**IP ​​Range and Specific URLs** : Scanning was limited to target domains and IP addresses to avoid affecting unauthorized services.
Credentials: Login credentials were configured to perform an authenticated scan and scan pages protected by login.
Scan Policies: Scan options were adjusted to minimize impact on the target system (e.g., limit the number of requests per second).
**Advanced Scanning Profile**: Plugins have been enabled to detect web server misconfigurations, certificate errors, and unsafe practices such as insecure cookies.

# Running the Scan
![Scan Screenshot](https://github.com/toleman84/holbertonschool-cyber_security/blob/c83e7501ba0d95f3f62973e762b311eba57a59e2/Nessus/2.png)

## Scan Launch Process
From the Nessus dashboard, I selected the "Web Application Testing" template.
I entered the relevant IP addresses, domains, and subdomains.
I configured the settings described above and validated the connection to the targets.
### I started the scan manually by clicking the "Start Scan" button.
### Monitoring Progress
During the scan, I monitored the progress from the Nessus dashboard, checking the completion percentage and possible errors in real time.
I verified that there were no crashes or interruptions on the target systems through parallel monitoring (e.g., server logs).
I reviewed the enabled plugins and detection activity to ensure that critical tests were running smoothly.

## Analysis of results
### Identified Vulnerabilities
Total Number of Vulnerabilities:    [13].
Critical:                           [0].
High Severity:                      [0].
Medium/Low Severity:                [1].

# Summary of Vulnerabilities
![Vuln Screenshot](https://github.com/toleman84/holbertonschool-cyber_security/blob/a16af34a77e35fb7a960b4db1c6f34a04bf5d4f0/Nessus/1.png)
**Low** ICMP Timestamp Request Remote Date Disclosure
### Description
The remote host answers to an ICMP timestamp request. This allows an attacker to know the date that is set on the targeted machine, which may assist an unauthenticated, remote attacker in defeating time-based authentication protocols.

Timestamps returned from machines running Windows Vista / 7 / 2008 / 2008 R2 are deliberately incorrect, but usually within 1000 seconds of the actual system time.

### Plugin Details
Severity:Low
ID:10114
Version:1.56
Type:remote
Family:General
Published:August 1, 1999
Modified:October 7, 2024

### VPR Key Drivers
Threat Recency: No recorded events
Threat Intensity: Very Low
Exploit Code Maturity: Unproven
Age of Vuln: 730 days +
Product Coverage: Very High
CVSSV3 Impact Score: 3.4
Threat Sources: No recorded events

### Risk Information
Vulnerability Priority Rating (VPR): 4.2
Exploit Prediction Scoring System (EPSS): 0.8808
Risk Factor: Low
CVSS v2.0 Base Score: 2.1
CVSS v2.0 Vector: CVSS2#AV:L/AC:L/Au:N/C:P/I:N/A:N

### Vulnerability Information
Vulnerability Pub Date: August 1, 1997
Reference Information
CWE:  200
CVE:  CVE-1999-0524

### Solution
Filter out the ICMP timestamp requests (13), and the outgoing ICMP timestamp replies (14).

