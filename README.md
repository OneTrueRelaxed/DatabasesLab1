<h2>Лабораторна робота №1 студента групи КМ-81 Волинця Сергія</h2>

Перед виконанням програми додайте в кореневу папку файли зі ЗНО за 
2019-2020 роки, та сконфігуруйте файл .env під вашу систему.
Для цього необхідно заповнити наступні поля:
-db=''- назва Вашой БД
-user='' - ім'я користувача
-password='' - пароль для користувача
-url='localhost' - тут можна вставити айпішник Вашої машини
-zno2020='' - шлях до файлу з результатами ЗНО за 2020
-zno2019='' - шлях до файлу з результатами ЗНО за 2019
-table=''- назва таблиці

Запуск програми
Для всіх варіантів ОС треба виконати:

docker-compose up
Далі запуск відрізняється залежно від системи

GNU/Linux Для того щоб запустити
python3 -m pip install virtualenv
python3 -m venv env
source env/bin/activate
source .env
python3 -m pip install -r requirements.txt
python3 main.py

Windows OS Треба послідовно виконати наступні дії в окремому терміналі
python -m pip install --user virtualenv
pyython -m venv env
.\env\Scripts\activate
python -m pip install -r requirements.txt
source .env
python main.py
python це execute команда python3, можливо у вас вона відрізняється

Також можливо, що у Вас замість python може бути команда py. За більш детальною
інформацією звертайтесь до документації пайтона по вашій ОC.

Легенда до query_result.csv
Файл містить результати порівняння найгірших балів у кожному регіоні за 2019-2020
роки.

![image](physical.png)
