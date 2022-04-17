## 1. VPN NOT found
---
## 2. All Info
              src_ip               dst_ip bidirectional_packets bidirectional_bytes application_name application_category_name
         20.54.37.73      192.168.218.130                     1                  58        TLS.Azure                     Cloud
      178.79.212.129      192.168.218.130                     3                 162             HTTP                       Web
       93.184.220.29      192.168.218.130                     9                 486             HTTP                       Web
      104.212.67.154      192.168.218.130                     1                  54        TLS.Azure                     Cloud
       192.168.218.1          224.0.0.251                     1                  83             MDNS                   Network
     192.168.218.128        192.168.218.2                     2                 220          NetBIOS                    System
       20.212.18.139      192.168.218.130                 10587             8283394        WireGuard                       VPN
## Unique src_ip, dst_ip, application_name
              src_ip               dst_ip application_name
         20.54.37.73      192.168.218.130        TLS.Azure
      178.79.212.129      192.168.218.130             HTTP
       93.184.220.29      192.168.218.130             HTTP
      104.212.67.154      192.168.218.130        TLS.Azure
       192.168.218.1          224.0.0.251             MDNS
     192.168.218.128        192.168.218.2          NetBIOS
       20.212.18.139      192.168.218.130        WireGuard
---
## 3. Capture start/stop time

 Start time: 2022-04-17 14:33:29.843000

 Stop time: 2022-04-17 14:34:32.160000

---
## 4. Useful info

application_name application_category_name bidirectional_bytes
            HTTP                       Web                 648
            MDNS                   Network                  83
         NetBIOS                    System                 220
       TLS.Azure                     Cloud                 112
       WireGuard                       VPN             8283394