# Лабораторная №3
# Часть 1 VPN

Работу выполнили: 
- Полеся Виталий
- Скопецкий Анатолий

## WireGuard

Установка WireGuard

![](images/wireguard/Screenshot_1.png)

Разрешаем пробрасывать пакеты

![](images/wireguard/Screenshot_2.png)

Генерируем ключи на сервере

![](images/wireguard/Screenshot_3.png)

Создаем конфиг wg0.conf

![](images/wireguard/Screenshot_4.png)

Запускаем сервис 

![](images/wireguard/Screenshot_5.png)

Генерируем ключи для клиента

![](images/wireguard/Screenshot_6.png)

Обновляем конфиг сервера wg0.conf, добавив в него раздел с клиентом

![](images/wireguard/Screenshot_7.png)

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

![](images/wireguard/Screenshot_8.png)

Вывод ipconfig

![](images/wireguard/Screenshot_9.png)

## IPSec
### Настройка сервера
* Готовая ВМ
![](images/img0.png)

* Пользуемся автоматической установкой из QuickStart
![](images/img5.png)

* Скачиваем автоматический установщик, производим установку
![](images/img1.png)

* Успешная установка. Пользователь по умолчанию IKEv2
![](images/img3.png)

* В конец файла добавлена поддержка RSA1 для подключения клиентов Linux.
![](images/img8.png)

![](images/img9.png)

![](images/img10.png)

## Настройка клиента

* Пошаговая настройка клиента.
![](images/img7.png)

* Перейдём к пункту Linux.
![](images/img8.png)

* Установка strrongswan - поддержку IKEv1 и IKEv2 протоколов.
![](images/img11.png)

* Проверяем наличие .p12 набора сертификатов и ключей клиента vpnclient.
![](images/img12.png)

* Подмонтировал эту же папку к файловой системе и открыл через проводник.
![](images/img13.png)

* Произвёл перемещение, извлёк из данного "ахрива" сертификаты и ключ шифрования.
![](images/img14.png)

* Произвёл настройку vpn в настройках системы.
![](images/img15.png)

![](images/img16.png)


## Проверка работоспособности
* Проверил работоспособность VPN. Фото без VPN...
![](images/img17.png)

* ... и через VPN.
![](images/img18.png)

* Проверка наличия перенаправления пакетов на 20.212.209.136. Перенаравление происходит. Выделенный "адаптер" под VPN не создаётся.
![](images/img22.png)

## Технические проблемы
* Не работало подключение через VPN. Никак. Для проверки, что проблема не на клиенте спустя получаса различных проверок установил на андроид strongSwan VPN Client. Получил отказ работы. Попробовал создать авторазвёртывание. На этапе установки софта оно работать отказалось. Немного подумав, заглянул в открытые порты, перенёс открытые UDP порты в основную ВМ и всё заработало. Скрин работы на ведре ниже. Два открытых UDP порта тоже ниже.

* Android
![](images/img19.jpg)
![](images/img20.jpg)

* UDP
![](images/img21.png)




