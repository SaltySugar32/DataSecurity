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



