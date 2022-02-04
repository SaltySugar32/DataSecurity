# Лабораторная №6 Исследование дампа машины Tesla

Работу выполнили: 
- Полеся Виталий
- Скопецкий Анатолий
## Постановка задачи:
Скачать образ виртуальной машины можно тут: https://disk.yandex.ru/d/4J_tc2sAFwtiDg.

## Техническое задание:
Необходимо провести анализ дампа операционной системы машины Tesla (да, той самой, 19го
года). Необходимо построить схему работы приложений внутри, большая часть из которых
являются веб приложениями. Внутри существует множество папок и файлов, содержащие
различные веб приложения, документацию, бортовые системы и т.д.. Образ 19го года, поэтому
данные приложения являются уязвимыми. Необходимо найти как минимум 2 уязвимости, либо
руководствуясь исходниками, которые есть в образе, либо можно запустить сервисы и найти их
вручную и эксплуатировать. Результатом работы будет карта образа, в любом удобном для вас
виде, mindmap, дерево папок с описанием и т.д., где должны быть описаны ключевые сервисы,
присутствующие в дампе. Второй частью задания найти уязвимости в данном дампе. С образом
разрешено производить все виды манипуляций.

---

## 7-zip

## Обзор директорий

![](imgs/main_directory.png)

### etc

В etc\openvpn видим скрипты настройки openvpn.

![](imgs/openvpn_1.png)

### local

В local\bin\ видим файл, в котором присутствуют какие-то ip. Ape-A и Ape-B - первичный и вторичный компьютеры автопилота.

![](imgs/ape_ip.png)

### share

В share\sounds\alsa видим файлы аудио системы Alsa.

![](imgs/share_sounds.png)

В share\base-files\ можно заметить какой-то ip адрес.

![](imgs/share_networks.png)

В share\ca-certificates\ находятся различны сертификаты

![](imgs/share_certificatess.png)

### ssl

В ssl\misc\ видим CA скрипт для openSSL, в нем есть 2 почты.

![](imgs/ssl_ca.png)

### tesla\UI

В tesla\UI\apps\ находятся папки различных приложений

![](imgs/tesla_apps.png)

![](imgs/app_audiotest.png)
![](imgs/app_browser.png)

В tesla\UI\assets\ есть файл со списком возможных голосовых команд.

![](imgs/tesla_voice_commands.png)

В tesla\UI\assets\sounds\WAV\ находятся различные звуковые файлы.

![](imgs/tesla_sounds.png)

В tesla\UI\assets\videos\ есть видео файл "starfield".

![](imgs/starfield.png)

В tesla\UI\assets\web_content\base\ присутствуют файлы для смены темы интерфейса - день/ночь.

![](imgs/tesla_day_nignt.png)

В tesla\UI\assets\web_content\manual\ присутствует мануал пользователя.

![](imgs/tesla_manuals.png)

![](imgs/tesla_manual_index.png)

![](imgs/tesla_manual_img.png)

В tesla\UI\assets\tesla_maps\ находятся файлы Valhalla, "an open source routing engine for navigation".

![](imgs/tesla_valhalla.png)

---

## Mount ISO

При монтировании образа получили 4 раздела

![](imgs/Mounted/disks.png)

### Раздел 3

![](imgs/Mounted/d3_main.png)

Список USB ID, видим какого-то сотрудника.

![](imgs/Mounted/d3_usb.png)

Также видим system и auth лог файлы.

![](imgs/Mounted/d3_auth.png)

![](imgs/Mounted/d3_syslog.png)

Хендшейк cid-updater

![](imgs/Mounted/d3_spool_handshake.png)

### Раздел 4

![](imgs/Mounted/d4_main.png)

Видим различные файлы кэша.

![](imgs/Mounted/d4_browser_cache.png)

Также присутствует папка .crashlogs. В них можно увидеть различные ip адреса

![](imgs/Mounted/d4_crashlogs.png)

![](imgs/Mounted/d4_crashlogs_ip.png)

![](imgs/Mounted/d4_crashlogs_ip2.png)

![](imgs/Mounted/d4_crashlogs_ip3.png)

Это различные внутренние сервисы

![](imgs/Mounted/d4_crashlogs_ip_app1.png)

![](imgs/Mounted/d4_crashlogs_ip_app2.png)

Также в одном логе видим московскую часовую зону.

![](imgs/Mounted/d4_crashlogs_timezone.png)

В .ssh видим authorized_keys

![](imgs/Mounted/d4_authorized_keys.png)

В папке media видим токены аутентификации

![](imgs/Mounted/d4_media.png)

Также видим файлы с контактной информации сервисов.

![](imgs/Mounted/d4_service.png)

В папке tmp есть tar файл, в котором можно найти файлы .PGM

![](imgs/Mounted/d4_img1.png)

![](imgs/Mounted/d4_img2.png)

![](imgs/Mounted/d4_img3.png)

![](imgs/Mounted/d4_img4.png)

![](imgs/Mounted/d4_img5.png)

![](imgs/Mounted/d4_img6.png)

![](imgs/Mounted/d4_img7.png)

![](imgs/Mounted/d4_img8.png)

![](imgs/Mounted/d4_img9.png)

