## 1. VPN NOT found
---
## 2. All Info
                        src_ip               dst_ip bidirectional_packets bidirectional_bytes   application_name application_category_name
                 192.168.218.2      192.168.218.128                     9                1242               ICMP                   Network
               192.168.218.130       20.199.120.182                    28                8523      TLS.Microsoft                     Cloud
               192.168.218.128        192.168.218.2                     9                 990            NetBIOS                    System
                219.100.37.211      192.168.218.130                  4253             1678358                TLS                       Web
               192.168.218.130          224.0.0.251                     2                 164               MDNS                   Network
     fe80::cd3a:d3bf:19f9:cd9e             ff02::fb                     2                 204               MDNS                   Network
                   20.54.37.73      192.168.218.130                     1                 205          TLS.Azure                     Cloud
                 192.168.218.1        192.168.218.2                     3                 330            NetBIOS                    System
## Unique src_ip, dst_ip, application_name
                        src_ip               dst_ip   application_name
                 192.168.218.2      192.168.218.128               ICMP
               192.168.218.130       20.199.120.182      TLS.Microsoft
               192.168.218.128        192.168.218.2            NetBIOS
                219.100.37.211      192.168.218.130                TLS
               192.168.218.130          224.0.0.251               MDNS
     fe80::cd3a:d3bf:19f9:cd9e             ff02::fb               MDNS
                   20.54.37.73      192.168.218.130          TLS.Azure
                 192.168.218.1        192.168.218.2            NetBIOS
---
## 3. Capture start/stop time

 Start time: 2022-04-17 14:36:06.693000

 Stop time: 2022-04-17 14:37:07.861000

---
## 4. Useful info

  application_name application_category_name bidirectional_bytes
              ICMP                   Network                1242
              MDNS                   Network                 368
           NetBIOS                    System                1320
               TLS                       Web             1678358
         TLS.Azure                     Cloud                 205
     TLS.Microsoft                     Cloud                8523