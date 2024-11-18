import pymysql
import random
from datetime import datetime

import sys
import io
# вывод в кодировке UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

host = 'localhost'
user = 'root'
password = 'A1l2e3k4s5e6y7'
db_name = 'casting'

def random_date():
    year = random.randint(1960, 2005)
    month = random.randint(1, 12)
    day = 0
    if month == 2:
        day = random.randint(1, 28)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1,30)     
    else: 
        day = random.randint(1, 31)
    return datetime(year, month, day).date()

def generate_passport():
    first_part = ''.join(random.choices('0123456789', k=4))
    second_part = ''.join(random.choices('0123456789', k=6))
    passport_number = f"{first_part} {second_part}"
    return passport_number

def generate_education():
    with open("uni.txt", "r", encoding="utf-8") as uni_file, open("education.txt", "r",
                                                                  encoding="utf-8") as education_file:
        edu = education_file.readlines()
        uni = uni_file.readlines()
        random_edu = random.choice(edu)

        if "Высшее образование" in random_edu:
            rand_uni = random.choice(uni)
        else:
            rand_uni = ""

    result_str = random_edu.strip() + " " + rand_uni.strip()
    return result_str


def generate_work():
    with open("work_experience.txt", "r", encoding="utf-8") as work_file:
        work = work_file.readlines()
        random_work = random.choice(work)
    return random_work.strip()


def table_actor():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)

        names_file = open("fullnames.txt", "r", encoding="utf-8")
        names = names_file.readlines()
        names_file.close()
        random.shuffle(names)
        rand_names = []
        for line in names:
            parts = line.split()
            rand_names.append(parts)

        for i in range(10000):
            index = random.randint(0, len(names) - 1)
            date = random_date()
            passport = generate_passport()
            education = generate_education()
            work = generate_work()
         
            with connection.cursor() as cursor:
                insert_query = ("INSERT INTO actor (surname, name, patronymic, date_of_birth, "
                                "passport_number, education, work_experience) "
                                " VALUES (%s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(insert_query, (rand_names[index][0], rand_names[index][1], rand_names[index][2],
                                            date, passport, education, work))
                connection.commit()

    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")
        
    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")


def table_role_type():
    try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            print("Соединение с базой данных установлено (Функция role_type)")

            role_list = ["Главная", "Второстепенная", "Эпизодическая"]

            with connection.cursor() as cursor:

                for role in role_list:
                    insert_query = ("INSERT INTO role_type (name) "
                                    " VALUES (%s)")

                    cursor.execute(insert_query, (role,))
                connection.commit()
        

    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")
        

    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")



def table_genres():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)

        genres = ["Боевик", "Байопик", "Детектив", "Военный", "Вестерн", "Документальный", "Исторический",
                  "Комедия", "Драма", "Криминал", "Мюзикл", "Мелодрама", "Приключения", "Фантастика", 
                  "Фентези", "Триллер", "Ужасы", "Нуар", "Спорт", "Научный"]

        with connection.cursor() as cursor:

            for gnr in genres:
                insert_query = ("INSERT INTO genres (name) "
                                    " VALUES (%s)")
                cursor.execute(insert_query, (gnr,))
            connection.commit()

    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")
        

    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")


def insert_data_from_file(file_name, table_name):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print(f"Successfully connected in {table_name}...")
        print("#" * 20)

        # Используем with для работы с файлами
        with open(file_name, "r", encoding="utf-8") as dir_file:
            directors = dir_file.readlines()

        random.shuffle(directors)

        dr = []
        for line in directors:
            parts = line.strip().split(maxsplit=1)
            dr.append(parts)

        with connection.cursor() as cursor:
            for i in range(200):
                date = random_date()
                passport = generate_passport()

                # Параметры для запроса на вставку
                insert_query = (f"INSERT INTO {table_name} (name, surname, date_of_birth, passport_number) "
                                "VALUES (%s, %s, %s, %s)")

                cursor.execute(insert_query, (dr[i][0], dr[i][1], date, passport))

            connection.commit()
            print(f"200 записей успешно добавлены в таблицу {table_name}.")

    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")

    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")

def table_casdir():
    insert_data_from_file("casting_dir.txt", "casting_director")

def table_dir():
    insert_data_from_file("director.txt", "director")

def table_film():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected in table_film...")
        print("#" * 20)

        film_file = open("films.txt", "r", encoding="utf-8")
        films = [line.strip() for line in film_file.readlines()]
        film_file.close()
        random.shuffle(films)

        count_dir = [0] * 201
        count_cas = [0] * 201

        for i in range(1000):

            dir = random.randint(1, 200)
            while (count_dir[dir] > 5):
                dir = random.randint(1, 200)
            count_dir[dir] += 1

            cas = random.randint(1, 200)
            while (count_cas[cas] > 5):
                cas = random.randint(1, 200)
            count_cas[cas] += 1

            with connection.cursor() as cursor:
                insert_query = ("INSERT INTO film (name, id_director, id_casting_director) "
                                " VALUES (%s, %s, %s)")
                cursor.execute(insert_query, (films[i], dir, cas))
                connection.commit()


    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")

    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")


def table_role():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected in table_role...")
        print("#" * 20)

        role_file = open("roles.txt", "r", encoding="utf-8")
        roles = [line.strip() for line in role_file.readlines()]
        role_file.close()

        for i in range(1000):

            count = random.randint(5, 20)
            for j in range(count):
                index = random.randint(0, len(roles) - 1)
                role = roles.pop(index)
                role_type = random.randint(1, 3)

  
                with connection.cursor() as cursor:
                    insert_query = ("INSERT INTO role (name, id_role_type, id_film) "
                                    " VALUES (%s, %s, %s)")
                    cursor.execute(insert_query, (role, role_type, i + 1))
                    connection.commit()


    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")

    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")


def table_gnr_film():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)

        for i in range(1000):
            count = random.randint(1, 5)
            for j in range (count):
                id_genre = random.randint(1, 20)
                
                with connection.cursor() as cursor:
                    insert_query = ("INSERT INTO film_genres (id_film, id_genres) "
                                    " VALUES (%s, %s)")
                    cursor.execute(insert_query, (i + 1, id_genre))
                    connection.commit()

    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")
    
    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")
       

def table_app():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,  
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)

        f1_file = open("f1.txt", "r", encoding="utf-8")
        f1 = [line.strip() for line in f1_file.readlines()]
        f1_file.close()

        f2_file = open("f2.txt", "r", encoding="utf-8")
        f2 = [line.strip() for line in f2_file.readlines()]
        f2_file.close()

        photodir = "C:/Documents/Photos/actor/"

        for i in range(10000):
            count = random.randint(5, 7)
            film1 = random.choice(f1)
            film2 = random.choice(f2)
            filmography = film1 + film2

            for j in range(count):
                role_id = random.randint(1, 12381)
                photo = photodir + str(i + 1) + ".jpg"

                with connection.cursor() as cursor:

                    cursor.execute("SELECT id_film FROM role WHERE id_role = %s", (role_id,))
                    result = cursor.fetchone()

                    film_id = result['id_film']
                    cursor.execute("SELECT id_director FROM film WHERE id_film = %s", (film_id,))
                    dir_result = cursor.fetchone()
                    cursor.execute("SELECT id_casting_director FROM film WHERE id_film = %s", (film_id,))
                    cas_result = cursor.fetchone()

                    id_dir = dir_result['id_director']
                    id_cas = cas_result['id_casting_director']

                    insert_query = ("INSERT INTO application (filmography, photos, id_actor, id_role, "
                                    " id_casting_director, id_director)"
                                    " VALUES (%s, %s, %s, %s, %s, %s)")
                    cursor.execute(insert_query, (filmography, photo, i + 1, role_id, id_cas, id_dir))
                    connection.commit()


    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")
    
    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")



def table_first():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected in table_first...")
        print("#" * 20)

        numbers = list(range(1, 59994))
        str1 = "Этап пройден"
        str2 = "Этап не пройден"

        for i in range(59993):
            score1 = random.randint(18, 100)
            score2 = random.randint(18, 100)

            if(len(numbers) > 2):
                rand_index = random.randint(1, len(numbers) - 1)
                num = numbers.pop(rand_index)
            else:
                num = numbers[0]

            if(score1 + score2 > 100):
                passed = str1
            else:
                passed = str2

            with connection.cursor() as cursor:

                insert_query = ("INSERT INTO first_stage (directors_assessment, casting_directors_assessment, "
                                "id_application, passing) "
                                " VALUES (%s, %s, %s, %s)")
                cursor.execute(insert_query, (score1, score2, num, passed))
                connection.commit()

    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")
    
    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")


def table_second():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)

        str1 = "Этап пройден"
        str2 = "Этап не пройден"

        with connection.cursor() as cursor:

            select_query = "SELECT id_application FROM first_stage WHERE passing = 'Этап пройден'"
            cursor.execute(select_query)
            results = cursor.fetchall()

            for result in results:
                id_app = result['id_application']

                score1 = random.randint(10, 80)
                score2 = random.randint(10, 80)

                if (score1 + score2 > 100):
                    passed = str1
                else:
                    passed = str2

                insert_query = ("INSERT INTO audition (directors_assessment, casting_directors_assessment, "
                            "id_application, passing) "
                            " VALUES (%s, %s, %s, %s)")
                cursor.execute(insert_query, (score1, score2, id_app, passed))
                connection.commit()


    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")
    
    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")


def table_third():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)

        str1 = "Роль получена"
        str2 = "Роль не получена"

        with connection.cursor() as cursor:

            select_query = ("SELECT id_application, directors_assessment, casting_directors_assessment"
                            " FROM first_stage WHERE passing = 'Этап пройден'")
            cursor.execute(select_query)
            results = cursor.fetchall()

            second_query = ("SELECT id_application, directors_assessment, casting_directors_assessment"
                            " FROM audition WHERE passing = 'Этап пройден'")
            cursor.execute(second_query)
            second_st = cursor.fetchall()

            for sec_result in second_st:
                id_app = sec_result['id_application']
                dir_asm = sec_result['directors_assessment']
                cas_asm = sec_result['casting_directors_assessment']

                for result in results:
                    if result['id_application'] == id_app:
                        second_dir_asm = result['directors_assessment']
                        second_cas_asm = result['casting_directors_assessment']
                        break

                score1 = random.randint(20, 100)
                score2 = random.randint(20, 100)

                total = dir_asm + cas_asm + second_dir_asm + second_cas_asm + score1 + score2

                if (total > 400):
                    passed = str1
                else:
                    passed = str2

                insert_query = ("INSERT INTO doubles_audition (directors_assessment, casting_directors_assessment, "
                            "id_application, results, getting_a_role) "
                            " VALUES (%s, %s, %s, %s, %s)")
                cursor.execute(insert_query, (score1, score2, id_app, total, passed))
                connection.commit()


    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")
    
    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")


def clear_all_data():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        print("Соединение с базой данных установлено.")

        with connection.cursor() as cursor:

            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

            cursor.execute(f"""
                SELECT TABLE_NAME 
                FROM INFORMATION_SCHEMA.TABLES 
                WHERE TABLE_SCHEMA = '{db_name}' AND TABLE_TYPE = 'BASE TABLE';
            """)

            tables = cursor.fetchall()
            print(f"Найдено {len(tables)} таблиц: {[table[0] for table in tables]}")
            
            if not tables:
                print("В базе данных нет таблиц для очистки.")
                return
            
            for (table_name,) in tables:
                cursor.execute(f"TRUNCATE TABLE `{table_name}`;")
                print(f"Таблица `{table_name}` успешно очищена.")

            cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

            connection.commit()
            print("Все таблицы очищены.")
    
    except pymysql.MySQLError as e:
        print(f"Ошибка при работе с базой данных: {e}")
    
    finally:
        if connection:
            connection.close()
            print("Соединение с базой данных закрыто.")

def main():
    clear_all_data()
    table_actor()
    table_role_type()
    table_genres()
    table_dir()
    table_casdir()

    table_film()

    table_role()
    table_gnr_film()

    table_app()
    table_first()
    table_second()
    table_third()

    
if __name__ == "__main__":
    main()

