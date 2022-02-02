# Лабораторная №5 Challenges
Работу выполнили: 
- Полеся Виталий
- Скопецкий Анатолий
## OSINT
- ### Infiltration
https://app.hackthebox.com/challenges/infiltration

Описание челленджа.

    Can you find something to help you break into the company 'Evil Corp LLC'. Recon social media sites to see if you can find any useful information.

Необходимо найти информацию про Evil Corp LLC

Результаты, полученные в поисковике Yandex

![](imgs/inf/inf_yandex.png)

Yandex не дал полезной информации касательно той компании, что указана в челендже.

Результаты, полученные в поисковике Google

![](imgs/inf/inf_google.png)

Были найдены страницы потенциальной искомой компании Evil Corp LLC на linkedin, а также linkedin потенциального CEO компании и instagram работника компании. 

На linkedin компании в описании есть нечто похожее на искомый нам флаг для челленджа.

![](imgs/inf/inf_linkedin.png)

Найденный флаг не тот, что нам нужен.

![](imgs/inf/inf_flag_error.png)

Данный "флаг" похож на зашифрованное сообщение. Попытка расшифровать с помощью [CyberChef](https://gchq.github.io/CyberChef). 
 "WW91IGNhbiBkbyB0aGlzLCBrZWVwIGdvaW5nISEh" декодируется из base64.

![](imgs/inf/inf_decode.png)

На странице linkedin CEO также встречается это зашифрованное сообщение. Новой информации не найдено. Также мы нашли twitter страницу этого CEO. Среди всех постов выделяется следуюший:

![](imgs/inf/inf_twitter.png)

Результат расшифровки этого сообщения не дал нужного результата

![](imgs/inf/inf_decode2.png)

Рассмотрим instagram потенциального работника. Среди всех фото было найдено следующее, потенциально содержащее искомый флаг, спрятанный где-то на экране ноутбука/комментариях/окружающих вещах.

![](imgs/inf/inf_instagram.png)

Увеличив картинку, можно заметить флаг на бейджике.

![](imgs/inf/inf_flag_closeup.png)

Искомый флаг

    HTB{Y0ur_Enum3rat10n_1s_Str0ng_Y0ung_0ne}

![](imgs/inf/inf_flag.png)

- ### Money Flowz
https://app.hackthebox.com/challenges/money-flowz

Описание челленджа.

    Frank Vitalik is a hustler, can you figure out where the money flows?

Необходимо найти информацию про некоего Frank Vitalik и его деньги. Результат поиска в yandex.

![](imgs/mon/mon_yandex.png)

Среди всех ссылок интересна только одна - пост на реддите про криптовалюты. 

![](imgs/mon/mon_yandex_reddit.png)

Здесь есть некоторая ссылка на сайт с транзакциями по некоторому адресу. Ничего интересного не найдено.

![](imgs/mon/mon_eth_scan.png)

Результат поиска в google.

![](imgs/mon/mon_google.png)

На странице reddit можно заметить ссылку на twitter Фрэнка, а также его интерес в криптовалютах и мошенничестве. С хорошей вероятностью это искомая нами страница.

![](imgs/mon/mon_reddit.png)

Рассмотрим реддит посты Фрэнка. Кросспост рассмотренного ранее поста. 

![](imgs/mon/mon_crosspost.png)

Второй пост Фрэнка также содержит некоторую ссылку.

![](imgs/mon/mon_post.png)

![](imgs/mon/mon_giveaway.png)

На данной странице есть интересный адрес

     0x1b3247Cd0A59ac8B37A922804D150556dB837699. 
     
Вернемся к сайту из предыдущего поста и просмотрим этот адрес. Список транзакций пуст, ничего интересного.

![](imgs/mon/mon_eth_scan2.png)

В комментариях поста с раздачей упоминается ropsten net. Загуглим.

![](imgs/mon/mon_giveaway.png)

![](imgs/mon/mon_google2.png)

Сайт весьма похожий на etherscan, но с другим доменом.

![](imgs/mon/mon_new_eth_scan.png)

Попробует ввести сбда найденные ранее адреса. C первым адресом ничего необычного.

![](imgs/mon/mon_new_eth_scan2.png)

Однако для второго адреса таблица транзакций на этом сайте уже не пуста. Также в поле баланса теперь есть некоторое число (ранее везде были нули).

![](imgs/mon/mon_new_eth_scan3.png)

После отчаяных попыток что либо найти, было замечено, что в списке транзакций есть одна выделяющаяся тразакция.

![](imgs/mon/mon_list.png)

В окне описания транзакции несколько новых адресов. Также замечена кнопка `View Input As`.

![](imgs/mon/mon_transaction.png)

Если просмотреть с помощью utf-8 получим флаг HTB. Проверим его.

![](imgs/mon/mon_flag.png)

Искомый флаг

    HTB{CryPt0Curr3ncy_1s_FuNz!!}

![](imgs/mon/mon_pwned.png)

---

## Forensics
- ### USB Ripper
https://app.hackthebox.com/challenges/usb-ripper

Описание челленджа.

    There is a sysadmin, who has been dumping all the USB events on his Linux host all the year... Recently, some bad guys managed to steal some data from his machine when they broke into the office. Can you help him to put a tail on the intruders? Note: once you find it, "crack" it.

Необходимо найти воров. Скачиваем файлы челленджа.

![](imgs/usb/usb_files.png)

В файле auth.json представлен список некоторых номеров.

![](imgs/usb/usb_auth.png)

В файле syslog представлены логи событий.

![](imgs/usb/usb_syslog.png)

Раз злоумышленники украли данные, то можно предположить, что в логах есть событие USB с номером, которого нет в auth.json. Так как там хранятся данные за весь год, то руками это сложно проверить. Необходимо найти инструмент. Был найден https://github.com/snovvcrash/usbrip .

![](imgs/usb/usb_google.png)

Установим и запустим usbrip, чтобы найти несоответствия.

![](imgs/usb/usb_ripper.png)

Получили следующий результат.

![](imgs/usb/usb_ripper2.png)

Загуглим полученный номер 

    71DF5A33EFFDEA5B1882C9FBDC1240C6

![](imgs/usb/usb_google2.png)

![](imgs/usb/usb_decode.png)

Искомый флаг 

    HTB{mychemicalromance}

![](imgs/usb/usb_flag.png)

- ### Emo
https://app.hackthebox.com/challenges/emo

Описание челленджа.

    WearRansom ransomware just got loose in our company. The SOC has traced the initial access to a phishing attack, a Word document with macros. Take a look at the document and see if you can find anything else about the malware and perhaps a flag.

Была произведена фишинговая атака. Вредносный файл - emo.doc.

![](imgs/emo/emo_file.png)

Проверим данный файл на вирусы с помощью [hybrid-analysis.com](https://www.hybrid-analysis.com/)

![](imgs/emo/emo_analys.png)

Просмотрим инциденты.

![](imgs/emo/emo_incidents_report.png)

В сетевом поведении не замечено ничего странного.

![](imgs/emo/emo_risk.png)

Однако в Mitre Att&ck techniques detection можно заметить множество подозрительных индикаторов. Рассмотрим все эти индикаторы.

![](imgs/emo/emo_mitre.png)

На странице первого же индикатора видим следующее.

![](imgs/emo/emo_encoded.png)

Можно предположить, что это какой-то закодированный скрипт для powershell.
Чтобы раскодровать это, воспользуемся [PSDecode](https://github.com/R3MRUM/PSDecode). Для этого зашифрованное сообщение запишем в файл test2.ps1 и запустим для него PSDecode.

![](imgs/emo/emo_psdecode.png)

![](imgs/emo/emo_psdecode2.png)

Здесь интересен 3й уровень.

![](imgs/emo/emo_psdecode3.png)

Получили следующий код.

![](imgs/emo/emo_decode.png)

В нем выделяются массивы чисел для переменной 
    
    $5FN5ggmsH.

![](imgs/emo/emo_decode2.png)

Запустим полученный код в powershell. Замечаем оператор 
    
    bxor 0xdf

Может потребоваться для расшифровки.

![](imgs/emo/emo_decode3.png)

Попытка раскодировать с помощью CyberChef.

![](imgs/emo/emo_decode4.png)

Искомый флаг
    
    HTB{4n0th3R_d4Y_AnoThEr_pH1Sh}

![](imgs/emo/emo_pwned.png)

- ### Market Dump
https://app.hackthebox.com/challenges/marketdump

Описание челленджа.

    We have got informed that a hacker managed to get into our internal network after pivoiting through the web platform that runs in public internet. He managed to bypass our small product stocks logging platform and then he got our costumer database file. We believe that only one of our costumers was targeted. Can you find out who the customer was?

Файл данных перехваченных пакетов, предоставленный в челлендже.

![](imgs/mar/mar_file.png)

Откроем MarketDump.pcapng предустановленным в kali Wireshark (программа-анализатор сетевых протоколов).

![](imgs/mar/mar_wireshark.png)

Злоумышленник получил доступ к сети с помощью некоторого веб приложения. предположим, что был использован протокол http.

![](imgs/mar/mar_http.png)

Видим, что среди пакетов встречается запись с статус кодом 200 и 'sql'. Так как в описании челленджа сказано, что злоумышленник украл файл базы данных с пользователями, предположим, что это искомый http пакет.

![](imgs/mar/mar_sql.png)

В описании пакета не было найдено ничего интересного.

![](imgs/mar/mar_packet.png)

Просмотрим поток TCP этого пакета.

![](imgs/mar/mar_tcp.png)

Здесь среди всех записей выделяется следующая. Похоже на зашифрованное сообщение.

![](imgs/mar/mar_encoded.png)

Попытка расшифровать с помощью CyberChef.

![](imgs/mar/mar_decoded.png)

Искомый флаг
    
    HTB{DonTRuNAsRoOt!MESsEdUpMarket}.

![](imgs/mar/mar_pwned.png)

---

## PWN
- ### Racecar
https://app.hackthebox.com/challenges/racecar

Описание челленджа. 
    
    Did you know that racecar spelled backwards is racecar? Well, now that you know everything about racing, win this race and get the flag!

Файл, предоставленный в челлендже.

![](imgs/race/file.png)

![](imgs/race/file_details.png)

Запустим файл. предлагается ввести имя и никнейм игрока, выбрать машину и трек.

![](imgs/race/game.png)

![](imgs/race/game2.png)

Видим сообщение об отсутствии файла flag.txt. Создадим его, вставим туда текст для теста. 

    AAAA

Запустим по новой игру. Теперь после победы появилось новое сообщение.

![](imgs/race/after_victory.png)

Просмотрим файл в IDA. Просмотрим структуру для этого участка кода.

![](imgs/race/ida.png)

Видим, что здесь используется printf.

![](imgs/race/ida2.png)

Можно попытаться воспользоваться [уязвимостью в printf](https://owasp.org/www-community/attacks/Format_string_attack)

![](imgs/race/prinf_attack.png)

Попытаемся проверить уязвимость. Закинем сюда %p, чтобы узнать какой-то указатель. Сработало, 0x58534200.

![](imgs/race/after_victory2.png)

Попытаемся закинуть сразу несколько %p.

![](imgs/race/flag_content.png)

Видим, что среди указателей есть `0x41414141`, соотвествтующий содержимому созданного flag.txt. Похоже он хранится в стеке в программе, на 12й позиции.

![](/imgs/race/flag_content2.png)

Попытаемся прочитать файл с удаленного сервера c помощью NetCat.

![](imgs/race/ip.png)

Для этого вводим известные данные для победы в игре. Далее в интересующий нам printf закидываем 
    
    %12$x
Получили следующий результат

    7b425448

![](imgs/race/remote.png)

Мы уже знаем, что это ASCII. Расшифруем. Очевидно, что это часть искомого флага.

![](imgs/race/decode.png)

Слегка изменим строку для printf, чтобы забрать весь флаг.

    %p%p%p%p%p%p%p%p%p%p%p___%p%p%p%p%p%p%p%p%p%p%p 
    (11 первых адресов нас не интересует, далее идут нужные, отделили их "_").

Получили 
    
    0x7b4254480x5f7968770x5f6431640x34735f310x745f33760x665f33680x5f67346c0x745f6e300x355f33680x6b6334740x7d213f

![](imgs/race/remote2.png)

Расшифруем. Получили 

    {BTH_yhw_d1d4s_1t_3vf_3h_g4lt_n05_3hkc4t}!?. 
    
В описании челленджа есть намек на то, что нужно "написать наоборот".

![](imgs/race/decode2.png)

Искомый флаг:
    
    HTB{why_d1d_1_s4v3_th3_fl4g_0n_th3_5t4ck?!}

![](imgs/race/pwned.png)

- ### You know 0xDiablos
https://app.hackthebox.com/challenges/you-know-0xdiablos

Описание челленджа.

    I missed my flag

Файл, предоставляеммый в челлендже.

![](imgs/diablos/file.png)

Файл vuln - исполняемый, запустим его. Предлагается ввести что-то, затем печтается введенная строка.

![](imgs/diablos/execute.png)

Просмотрим файл в IDA. Ничего интересного.

![](imgs/diablos/ida_main.png)

Видим, что в главной функции вызывается какая-то функция vuln. Просмотрим ее.

![](imgs/diablos/ida_vuln.png)

Здесь фигурируют 2 числа - 184 и 4. Также видим, что вызывается функция gets. Она уязвима, ибо не проверяет размер вводимого массива. Можно атаковать переполнением буфера.

Также среди функций есть интересная flag. Возможно получится с помощью атаки переполнением и регистра eip получить доступ к искомому флагу.

![](imgs/diablos/ida_flag.png)

Вернемся к переполнению буфером. Воспользуеися gdb, предустановленным в kali. Создадим файл ввода с 300 символами, чтобы переполнить буфер.

![](imgs/diablos/gdb.png)

Видим в указателе регистра EIP 

    0x41417741 ('AwAA')

Найдем оффсет этого регистра.

![](imgs/diablos/gdb_offset.png)

Теперь, чтобы попасть в функцию flag, необходимо узнать ее адрес. Заходим в IDA и видим нужный адрес.

    0x080491e2

![](imgs/diablos/ida_flag_address.png)

![](imgs/diablos/address.png)

Создадим входной файл - input.txt. Так как оффсет eip = 188, то после 188 символов надо вставить адрес функции flag ('\xe2\x91\x04\x08').

![](imgs/diablos/attack.png)

Пытаемся провернуть это на сервере. Не сработало.

![](imgs/diablos/server.png)

Просмотрим функцию flag. Видим, что тут используются какие-то 2 аргумента, похоже они сравниваются с некоторыми значениями

        0x0DEADBEEF и 0x0C0DED00D

![](imgs/diablos/ida_flag2.png)

![](imgs/diablos/args.png)

(`\r` эквивалентно `\x0d`)

Исходя из данного рисунка из [статьи](https://web.archive.org/web/20161106210059/https://www.exploit-db.com/docs/28553.pdf) Можно закинуть в наш входной файл параметры, найденные выше.

![](imgs/diablos/article.png)

Для этого к уже имеющимся символам в файле добавим 'smth' - заглушку для saved return address, и за ним - параметры (`\xef\xbe\xad\xde` и `\x0d\xd0\xde\xc0`). Теперь получили флаг с сервера.

![](imgs/diablos/flag.png)

Искомый флаг:

    HTB{0ur_Buff3r_1s_not_healthy}

![](imgs/diablos/pwned.png)

---

## Web
- ### Slippy
https://app.hackthebox.com/challenges/slippy

    You've found a portal for a firmware upgrade service, responsible for the deployment and maintenance of rogue androids hunting humans outside the tractor city. The question is... what are you going to do about it?

Файлы, предоставленные в челлендже.

![](imgs/slippy/files.png)

Видим файл flag, в котором лежит наш искомый флаг.

![](imgs/slippy/files2.png)

Просмотрим докерфайл. Видим, что это фласк приложение.

![](imgs/slippy/dockerfile.png)

Соберем и запустим приложение. Открывается страница, на которой можно загрузить файл.

![](imgs/slippy/app.png)

Просмотрим код, отвечающий за загрузку.

![](imgs/slippy/upload_code.png)

Вызывается функция `extract_from_archive`. Сначала проверяется, что тип файла - tar. Затем tar файл извлекается в некоторую директорию. 

![](imgs/slippy/extract_func.png)

Также в tarfile имеется [уязвимость](https://m.vk.com/away.php?to=https%3A%2F%2Fcodeql.github.com%2Fcodeql-query-help%2Fpython%2Fpy-tarslip%2F):

    For example, if a tar archive contains a file entry ..\sneaky-file, and the tar archive is extracted to the directory c:\output, then naively combining the paths would result in an output file path of c:\output\..\sneaky-file, which would cause the file to be written to c:\sneaky-file.

Чтобы воспользоваться этим эксплойтом необходимо определить, куда записывается содержимое. Данная информация есть в config.py.

![](imgs/slippy/upload_folder.png)

Теперь ясно, что наш tar.gz по дефолту сохраняется в `/app/application/static/archives/<some_number>/<наш tar>`. Чтобы получить искомый флаг из flag.txt можно попытаться добавить в файл routes.py новый путь GET /flag, который даст нам содержимое flag.txt. Затем можно добавить в tar.gz обновленный routes.py с использованием уязвимости.

Создадим новый раут:

![](imgs/slippy/route.png)

Теперь создадим тар файл:

![](imgs/slippy/expoit_tar.png)

![](imgs/slippy/expoit_tar2.png)

Теперь можно залить этот файл на сервер.

![](imgs/slippy/uploaded.png)

Проходим по /pwned, видим флаг.

![](imgs/slippy/flag.png)

Искомый флаг:

    HTB{i_slipped_my_way_to_rce} 

![](imgs/slippy/pwned.png)

- ### Toxic

https://app.hackthebox.com/challenges/toxic

Описание челленджа.

    Humanity has exploited our allies, the dart frogs, for far too long, take back the freedom of our lovely poisonous friends. Malicious input is out of the question when dart frogs meet industrialisation. 🐸

Файлы, предоставленные в челлендже.

![](imgs/toxic/files.png)

![](imgs/toxic/files.png)

В файле index.php видим, как создаются куки. В значение $file кладется путь до index.html и затем кодируется в base64. Так же оказывается, в ответ сервер кидает содержимое файла в куках.

![](imgs/toxic/cookies.png)

Получим куки через Postman и расшифруем.

![](imgs/toxic/postman_get.png)

![](imgs/toxic/decoded.png)

Попробуем посмотреть flag на сервере, для этого подделаем куки.

![](imgs/toxic/new_cookie.png)

![](imgs/toxic/response.png)

Похоже файла flag нет на сервере. проверим исходники ещё раз. В скрипте entrypoint.sh видим, что флагу присваивается рандомное имя. Осталось понять, как узнать его.

![](imgs/toxic/entrypoint.png)

Для этого воспользуемся [log poisoning](https://henkel-security.com/tag/log-poisoning/). Нужно в куки засунуть путь `/var/log/nginx/access.log`

![](imgs/toxic/new_cookie2.png)

![](imgs/toxic/response2.png)

Теперь надо узнать название флага. Запустим скрипт в запросе.

    <?php system('ls /');?>

![](imgs/toxic/response3.png)

Имя файла на сервере - `flag_yxj56`. Подделаем куки.

![](imgs/toxic/new_cookie3.png)

![](imgs/toxic/flag.png)

Искомый флаг:

    HTB{P0i5on_1n_Cyb3r_W4rF4R3?!}

![](imgs/toxic/pwned.png)

- ### Owasp top10

---

- #### 1 looking glass

Описание челленджа:

    We've built the most secure networking tool in the market, come and check it out!

Просмотрим сайт.

![](imgs/owasp/1/1_site.png)

![](imgs/owasp/1/1_page_source.png)

Видим, что можно ввести какой-то айпишник и пингануть его. Можно предположить, как устроена эта функция. К команде ping конкатенируется введенная строка (айпи) и затем выполняется команда ping. Так как используется командная строка, то можно попытаться к айпи приписать следующее:

    <ip>; ls

![](imgs/owasp/1/1_ls.png)

Команда выполнена, теперь можно просмотреть директории с целью найти нужный флаг. Начнем с родительской директории.

    cd ..; ls

![](imgs/owasp/1/1_cd_ls.png)

Видим файл, похожий на наш флаг. просмотрим его с помощью:

    cd..; cat flag_fUKsC

![](imgs/owasp/1/1_cd_cat.png)

Искомый флаг:

    HTB{I_f1n4lly_l00k3d_thr0ugh_th3_rc3}


- #### 2 sanitize

Описание челленджа.

    Can you escape the query context and log in as admin at my super secure login page?

Сайт. 

![](imgs/owasp/2/2_site.png)

Попробуем войти в учетку админа. Попробуем стандартные admin:admin

![](imgs/owasp/2/2_login.png)

Не получилось однако видим интересное сообщение на языке SQL.
Посмотрим на код страницы.

![](imgs/owasp/2/2_page_source.png)

Видим закомментированный `/debug`. Попробуем перейти по этому пути.

![](imgs/owasp/2/2_debug_source.png)

Видим код сайта. Самое интересное - функция логина.

    q = "select * from users where username = '%s' AND password = '%s';" % (request.form.get('username', ''), request.form.get('password', ''))

![](imgs/owasp/2/2_vuln.png)

Сразу понятно, что она уязвима к SQL инъекции.
Для этого снова попытаемся войти, на этот раз с логином admin и паролем:

    smth' or '1'='1'

Теперь в функцию в качестве пароля попадет 'smth', а также в SQL команду добавится строка `or '1'='1'`. Понятно, что логин произойдет успешно. Получили наш флаг.

![](imgs/owasp/2/2_login2.png)

Искомый флаг:

    HTB{SQL_1nj3ct1ng_my_w4y_0utta_h3r3}

- #### 3 baby auth

Описание челленджа.

    Who needs session integrity these days?

Перейдем на сайт.

![](imgs/owasp/3/3_site.png)

Просмотрим код страниц. Ничего интересного.

![](imgs/owasp/3/3_login_source.png)

![](imgs/owasp/3/3_register_source.png)

admin:admin не работает. Также на сайте есть возможность зарегестрирлваться. Попробуем зарегистрироваь новый акк.

![](imgs/owasp/3/3_register.png)

При входе в только что созданный акк видим следующее.

![](imgs/owasp/3/3_salty_login.png)

Посмотрим на куки.

![](imgs/owasp/3/3_cookie.png)

Раскодируем в cyberchef.

![](imgs/owasp/3/3_decoded.png)

Видим кое-что интересное. Попробуем заменить ник на admin. Кстати, тут почему-то `7/` в конце, я это убрал, ибо не работало по-другому.

![](imgs/owasp/3/3_encoded.png)

Теперь перейдем на сайт с этим куки. Получаем флаг.

![](imgs/owasp/3/3_flag.png)

Искомый флаг:

    HTB{s3ss10n_1nt3grity_1s_0v3r4tt3d_4nyw4ys}

- #### 4 baby nginxatsu

Описание челленджа.

    Can you find a way to login as the administrator of the website and free nginxatsu?

Перейдем на сайт.

![](imgs/owasp/4/site.png)

В коде страниц ничего интересного. Попробуем войти с admin:admin. Не получилось.

![](imgs/owasp/4/admin_login.png)

Создадим новый аккаунт.

![](imgs/owasp/4/salty_register.png)

Видим следующее окно генерации конфиг файла nginx.

![](imgs/owasp/4/create.png)

В сгенерированном файле видим в комментариях подсказку.

![](imgs/owasp/4/config.png)

Переходим на /storage. Видим список файлов, среди которых есть интересный tar файл.

![](imgs/owasp/4/tar.png)

Скачаем его и откроем. Получили папку database c sqlite файлом.

![](imgs/owasp/4/extract.png)

В БД есть таблица users, в которой видим админку. надо расхешировать пароль.

![](imgs/owasp/4/database.png)

Воспользуемся crackstation. Видим, что пароль - `adminadmin1`

![](imgs/owasp/4/crack.png)

Теперь войдем в админку на сайте.

![](imgs/owasp/4/admin_login2.png)

Видим флаг.

![](imgs/owasp/4/flag.png)

Искомый флаг:

    HTB{ng1ngx_r34lly_b3_sp1ll1ng_my_w3ll_h1dd3n_s3cr3ts??}

- #### 5 baby WAFfles order

Описание челленджа.

    Our WAFfles and ice scream are out of this world, come to our online WAFfles house and check out our super secure ordering system API!

Заходим на сайт.

![](imgs/owasp/5/site.png)

Здесь можно выбрать waffles или ice cream и ввести номер таблицы. Опция Both недоступна.

![](imgs/owasp/5/parameters.png)

При отправке заказа видим такое сообщение.

![](imgs/owasp/5/order.png)

Просмотрим код страницы. Ничего интересного.

![](imgs/owasp/5/source.png)

Вкладка сайта называется xxe. Весьма странное название, не соотвестствует сайту, загуглим:

![](imgs/owasp/5/google.png)

Видим статью про XML инъекцию. Возможно это поможет достать флаг.

![](imgs/owasp/5/xxe.png)

Просмотрим файлы приложения, предоставленные в челлендже. Сразу видим файл flag.

![](imgs/owasp/5/files.png)

В index.php видим, что при методе POST вызывается контроллер OrderController.

![](imgs/owasp/5/index_php.png)

Посмотрим этот контроллер. Он работает с json и xml. Похоже нам действительно надо воспользоваться XXE.

![](imgs/owasp/5/order_controller.png)

Видим, что пользователю выводится order->food.

Воспользуемся XML инъекцией. Добавим к запросу POST ... /api/order (из index.php) пейлоуд:

    <!--?xml version="1.0" ?-->
    <!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///flag"> ]>
    <order>
    <food>
    &ent;
    </food>
    </order>

![](imgs/owasp/5/post3.png)

Искомый флаг:

    HTB{wh0_l3t_th3_XX3_0ut??w00f..w00f..w00f..WAFfles!}

- #### 6 baby todo or not todo
  
Описание.

    I'm so done with these bloody HR solutions coming from those bloody HR specialists, I don't need anyone monitoring my thoughts, or do I... ?

- #### 7 baby BoneChewerCon

Описание.

    Due to heavy workload for the upcoming baby BoneChewerCon event, the website is under maintenance and it errors out, but the debugger is still enabled in production!! I think the devil is enticing us to go and check out the secret key.

- #### 8 Full Stack Conf

Описание.

    Welcome to Full Stack Conf, explore the future of JavaScript with a lineup of industry professionals and discover new techniques to advance your career as a web developer. But be very careful with the stay up to date form, we don't sanitize anything and the admin logs in and checks the emails regularly, don't try anything funny!! 😅

- #### 9 baby website rick

Описание.

    Look Morty, look! I turned myself into a website Morty, I'm Website Rick babyyy!! But don't play around with some of them anti pickle serum I have stored somewhere safe, if I turn back to a human I'll have to go to family therapy and we don't want that Morty.


- #### 10 baby breaking grad

Описание.

    We corrected the math in our physics teacher's paper and now he is failing us out of spite for making a fool out of him in the university's research symposium, now we can't graduate, unless we can do something about it...

---

- ### Steamcoin

https://app.hackthebox.com/challenges/steamcoin

Описание челленджа.

    Meet SteamCoin, the first decentralized cryptocurrency of the SteamPunk realm that provides you the liberty to exchange value without intermediaries and translates to greater control of funds and lower fees. Sign up today in our SteamCoin wallet to get equipped with the tools and information you need to buy, sell, trade, invest, and spend SteamCoins.

Файлы, предоставленные в челлендже.

![](imgs/steamcoin/files.png)

![](imgs/steamcoin/files2.png)

![](imgs/steamcoin/files3.png)

В докерфайле видим, что используется haproxy v.2.4.0, а также, что nodejs работает на 8081 порту.

![](imgs/steamcoin/dockerfile.png)

![](imgs/steamcoin/dockerfile2.png)

В HAProxy существует [уязвимость](https://jfrog.com/blog/critical-vulnerability-in-haproxy-cve-2021-40346-integer-overflow-enables-http-smuggling/) - HTTP smuggling.
Просмотрим конфиг файл haproxy.

![](imgs/steamcoin/haproxy_cfg.png)

Видим restricted_page /api/test-ui. Эта страница может быть достигнута из 127.0.0.1 (локалхост). Так как мы знаем, что есть возможность обойти ACL(Access control list) с помощью http smuggling, то, возможно, эта страница поможет получить искомый флаг.

В local.ini видим админку.

![](imgs/steamcoin/local_ini.png)

В database.js видим инициализацию бд, а также поле verification_doc с тестовым флагом. Похоже, чтобы забрать флаг, надо попасть в аккаунт админа и прочитать этот файл.

![](imgs/steamcoin/database_js.png)

Посмотрим, как выполняется процесс аутентификации. Вначале проверяется наличие cookies. В getHeaders берется JWT токен. Также видим, что на сайте используется JWKS 

![](imgs/steamcoin/auth_middleware.png)

Зайдем на сайт.

![](imgs/steamcoin/site.png)

Попробуем войти в админку. Стандартные данные не подходят.

![](imgs/steamcoin/admin_login.png)

Создадим аккаунт и войдем. Кнопки receive/send не работают.

![](imgs/steamcoin/account.png)

Однако на странице Settings видим, что можно загрузить файл.

![](imgs/steamcoin/settings.png)

Возможные форматы:

![](imgs/steamcoin/valid_files.png)

Просмотрим куки. Видим JWT токен. Расшифруем.

![](imgs/steamcoin/salty_cookie.png)

![](imgs/steamcoin/salty_decoded.png)

Посмотрим на jku url. Видим ключи.

![](imgs/steamcoin/jwks.png)

В функции аутентификации видим, что для jku проверяется локалхост. Необходимо обойти эту проверку.

![](imgs/steamcoin/localhost_check.png)

В файле раутов видим кое-что интересное `/api/test-ui`. Здесь проверяется, что имя пользователя - admin. Также вызывается некоторый метод testUI.

![](imgs/steamcoin/test_ui.png)

Просмотрим метод testUI, получающая path и keyword. Далее идет переход на локалхост/path и проверяет наличие keyword.

![](imgs/steamcoin/testui.png)

Можно попытаться загрузить вредоносный файл на сайт, а затем с помощью testUI обойти проверку локалхоста. Посмотрим на код загрузки файла.

![](imgs/steamcoin/upload.png)

Сразу бросается в глаза, что админ не может просматривать страницу. Далее проверяется расширение файла, название хешируется в md5.

Можно попытаться кинуть в файл ключи из 'well-known/jwks.json'. Затем подделать JWT токен, чтобы он ссылался на этот файл, изменить имя на admin и получить доступ в админку.

Для этого создадим ключи, файл test.png с публичным ключом.

![](imgs/steamcoin/generate_keypair.png)

![](imgs/steamcoin/test_png.png)

Загрузим файл с ключами.

![](imgs/steamcoin/uploaded.png)

    uploads/eea86c409157902fb526030d5c876a60.png

Теперь подделаем JWT токен.

![](imgs/steamcoin/token.png)

Мы можем войти в админку. Однако тут ничего нет особого.

![](imgs/steamcoin/admin_login2.png)
