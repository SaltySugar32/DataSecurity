## 1. VPN found
---
## 2. All Info
              src_ip               dst_ip bidirectional_packets bidirectional_bytes   application_name application_category_name
       192.168.218.1      239.255.255.250                     4                 844               SSDP                    System
     192.168.218.128       64.233.161.188                     3                 163             Google                       Web
       192.168.218.1      239.255.255.250                     4                 840               SSDP                    System
     192.168.218.128        192.168.218.2                     7                 770            NetBIOS                    System
        20.212.17.54      192.168.218.128                  8506             5650897      OpenVPN.Azure                     Cloud
       192.168.218.1      192.168.218.255                     2                 172            Spotify                     Music
       192.168.218.2      192.168.218.128                     2                 276               ICMP                   Network
## Unique src_ip, dst_ip, application_name
              src_ip               dst_ip   application_name
       192.168.218.1      239.255.255.250               SSDP
     192.168.218.128       64.233.161.188             Google
     192.168.218.128        192.168.218.2            NetBIOS
        20.212.17.54      192.168.218.128      OpenVPN.Azure
       192.168.218.1      192.168.218.255            Spotify
       192.168.218.2      192.168.218.128               ICMP
---
## 3. Capture start/stop time

 Start time: 2022-04-17 20:33:05.031000

 Stop time: 2022-04-17 20:34:07.217000

---
## 4. Useful info

  application_name application_category_name bidirectional_bytes
            Google                       Web                 163
              ICMP                   Network                 276
           NetBIOS                    System                 770
     OpenVPN.Azure                     Cloud             5650897
              SSDP                    System                1684
           Spotify                     Music                 172