from working_files.auth import auth_public
from working_files.sender import send
from working_files.preprocess import preprocess
from csv import DictReader

session = auth_public()
# txt файл находится в data/ и имеет следующую структуру:
# имя-фамилия ученика через пробел и его ссылка на vk из журнала через Tab
# см data/students.txt
preprocess()

# В data/message_text.txt должно быть сообщение текущей рассылки
with open('data/message_text.txt', encoding='utf-8') as message:
    base_message = message.read()

with open('data/students.csv', encoding='utf-8') as file:
    data = DictReader(file)
    for row in data:
        # Если написать в message.txt 'name', то заменится именем ученика
        personal_message = base_message.replace('name', row['name'].split()[0])
        # В img относительный адрес до фотки
        send(session, row['id'], personal_message, row['name'], img='images/XOfinal.jpg')
