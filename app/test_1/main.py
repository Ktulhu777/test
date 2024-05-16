import psycopg2
import requests
from app.config import DB_NAME, DB_HOST, DB_USER, DB_PASS

# Подключение к PostgreSQL
conn = psycopg2.connect(host=DB_HOST,
                        user=DB_USER,
                        database=DB_NAME,
                        password=DB_PASS)
cursor = conn.cursor()


# Эмуляция получения  данных от вебхука Битрикс24
def get_webhook_data(contact_id: int = 10, contact_name: str = "Вова") -> tuple[int, str]:
    return contact_id, contact_name


contact_id, contact_name = get_webhook_data()

# Проверка имени в БД
cursor.execute("SELECT COUNT(*) FROM names_man WHERE name = %s", (contact_name,))
result = cursor.fetchone()
count_man = result[0]

cursor.execute("SELECT COUNT(*) FROM names_woman WHERE name = %s", (contact_name,))
result = cursor.fetchone()
count_woman = result[0]

# Определение пола и обновление данных в Битрикс24
if count_man > 0:
    gender = "Мужчина"
elif count_woman > 0:
    gender = "Женщина"
else:
    gender = "Не определен"

update_data = {
    'ID': contact_id,
    'Gender': gender
}

# Обновление данных контакта в Битрикс24
update_url = 'url'
response = requests.post(update_url, json=update_data)

# Закрытие соединения с PostgreSQL
cursor.close()
conn.close()
