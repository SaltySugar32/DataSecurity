# Лабораторная №4

Работу выполнили: 
- Полеся Виталий
- Скопецкий Анатолий
  
---

Датасеты для анализа трафика находятся в папке `data`:
1. Захваченный трафик с первой части лабораторной работы, дополнительно настроив
OpenVPN и захватив трафик с него.
2. Захват трафика openvpn, wireguard и ipsec с отключенной телеметрией в ОС, для
уменьшения загрязнения трафика. Можно использовать на выбор Windows или Linux.
Текущий выбор остается для выполнения пункта 3.
3. Захват трафика без включенного VPN.
4. Захват трафика 2 VPN по очереди и без включенного VPN (всё захватывается в один файл).
Последовательность использования VPN не имеет значения, между переключениями VPN
не выключаем захват. В конце захватываем трафик с выключенным VPN. !ВАЖНО: в этом
пункте для необходимо перейти по нижеперечисленным ссылкам для обеих VPN по
отдельности и после их выключения еще раз для получения чистого трафика.

---

В папке `analysed_md` нахпдятся md отчеты проанализированного трафика, содержащие следующие пункты:

1. Проверка на наличие VPN трафика (application_category_name)
2. Вывод информации о следующих данных:
['src_ip','dst_ip','bidirectional_packets','bidirectional_bytes','application_name','application_cat
egory_name'] с возможностью вывода для уникальных значений ['src_ip','dst_ip',
'application_name']
3. Вывод начала и конца захвата трафика
4. Вывод полезной информации на основании данных, что есть в трафике. Каждый
определяет полезность тех или иных данных на свое усмотрение. Пример вывода
где'bidirectional_bytes' является суммой для 'application_name'


---

В файле `RandomForestClassifier.ipynb` происходит тренировка модели RandomForestClassifier на трафике,
полученном в пункте 4