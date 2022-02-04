# Backdoor

![](imgs/msf1.png)

Проблема в lhost. Изменил ip на свой

![](imgs/ip_addr.png)

![](imgs/msf2.png)

запустил shell оболочку, вывел папки

![](imgs/msf3.png)

увидел какой-то user.txt

![](imgs/cat.png)

флаг введен

![](imgs/flag.png)


# Devzat (Medium)

![](imgs/Devzat/htb.png)

Сначала найдем открытытые порты. Просканируем данный ip с помощью nmap.

![](imgs/Devzat/nmap.png)

Просмотрим порт 80 - HTTP. Главная страница сайта - чата для разработчиков.

![](imgs/Devzat/main_page1.png)

Видим, что 2 ветки гита, 10 клиентов, ... Также предложение подключиться по ssh.

![](imgs/Devzat/main_page2.png)

email patrick@devzat.htb. Ссылки на социалки не работают.

![](imgs/Devzat/main_page3.png)

Здесь мы больше ничего не может найти. Попытаемся найти поддомены с помощью gobuster.
Словарь взят из: 
https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-110000.txt

![](imgs/Devzat/gobuster.png)

Спустя некоторое нашелся первый поддомен - pets.devzat.htb

![](imgs/Devzat/pets_page.png)

Видим таблицу записей о питомцах. Внизу страницы есть поле ввода.

![](imgs/Devzat/pets_page2.png)

exit status 1 вместо species.

![](imgs/Devzat/pets_page3.png)

Удаление записей не работает.

![](imgs/Devzat/pets_page4.png)



