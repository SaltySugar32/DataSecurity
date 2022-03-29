Установка WireGuard

![](imgs/wireguard/Screenshot_1.png)

Разрешаем пробрасывать пакеты

![](imgs/wireguard/Screenshot_2.png)

Генерируем ключи на сервере

![](imgs/wireguard/Screenshot_3.png)

Создаем конфиг wg0.conf

![](imgs/wireguard/Screenshot_4.png)

Запускаем сервис 

![](imgs/wireguard/Screenshot_5.png)

Генерируем ключи для клиента

![](imgs/wireguard/Screenshot_6.png)

Обновляем конфиг сервера wg0.conf, добавив в него раздел с клиентом

![](imgs/wireguard/Screenshot_7.png)

Создаем конфиг клиента

    [Interface]
    PrivateKey = OM3ynUSD0Q5xmGIner0Mbd7tt6bbwzrC8KnUPAdvm0U=
    Address = 10.0.0.4/32
    DNS = 8.8.8.8

    [Peer]
    PublicKey = wGYjhqzapB2sBdGUf9RVdJi3zarCQMr5rkc4fcXEfiY=
    AllowedIPs = 0.0.0.0/0
    Endpoint = 137.116.150.160:51820
    PersistentKeepalive = 20


Добавляем туннель в WireGuard

![](imgs/wireguard/Screenshot_8.png)

Вывод ipconfig

![](imgs/wireguard/Screenshot_9.png)





