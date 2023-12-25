from _pydecimal import Decimal

import psycopg2

try:
    conn = psycopg2.connect(host = '78.141.227.124',
                            user = 'postgres',
                            database = 'GITHUB',
                            password = '123')
    print('Успешно подключено к Базе Данных')

    cur = conn.cursor()
    # cur.execute("select count(age) from students where age>15") 1-задание
    # cur.execute("select round(avg(age),1) from students where stud_name ILIKE 'A%'") 2-задание
    avg = cur.fetchall()
    print(avg)
except Exception as err:
    print(err)
