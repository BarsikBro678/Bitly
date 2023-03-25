# Обрезка ссылок с помощью Битли

Данный проект если вы введете ссылку в терминал, выведет битлинк (укороченная ссылка).

Если вы введете битлинк, программа посчитает сумму кликов по нему за месяц.

Если ссылка неверная, будет выведено "Ошибка при запросе bitly".

### Как установить

После установки сторонних библиотек, необходимо создать в корневой папке файл с названием .env и записать в него:
```
BITLY_TOKEN=2219e255ad14f84fa82f4ca6c784d8f89d984016
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

Введите команду "python main.py _ваша_ссылка_" __в терминале__.

### Примеры результата
```
Ввод                                                        Вывод
```
```
python main.py https://google.com                           Битлинк:  https://bitly.is/3iUkkp3
```
```
python main.py https://bitly.is/3iUkkp3                     Количество кликов по ссылке : 0            
```
```
python main.py google.com                                   Ошибка при запросе bitly
```
```
pyhton main.py https://gaagle.ra                            Ошибка при запросе bitly
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
