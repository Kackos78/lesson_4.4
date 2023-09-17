import telebot
import json

# До конца не доделан, хочу добавить все функции из spravochnik + кнопки
# имя бота 'phones_sp'

bot = telebot. TeleBot('6591806500:AAEJxvgrur2WNZCRGJaECc5gziBXRxM3H5s')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
phones_sp = {'дядя коля': {'номер телефона': ['8-800-555-35-35', '8-900-536-35-35'], 'город': 'Сыктыфкар', 'Статус': 'дядя'}, 'нюрка': {'номер телефона': ['8-555-549-34-35'], 'город': 'Сыктыфкар', 'Статус': 'тетя'}}

@bot.message_handler(commands=['save'])
def save(massage):
    with open('phones.json','w', encoding='utf-8') as phones:
        phones.write(json.dumps(phones_sp, ensure_ascii=False))
        bot.send_message(massage.chat.id, f'Данные сохранены' )

@bot.message_handler(commands=['load'])
def load(massage):
    with open('phones.json','r', encoding='utf-8') as phones:
        phones_sp = json.load(phones)
        bot.send_message(massage.chat.id, f'Данные обновлены' )
        return phones_sp

@bot.message_handler(commands=['print_all'])
def print_all(massage):
    bot.send_message(massage.chat.id, f'Вот текущий список номеров' )
    for k, v in phones_sp.items():
        bot.send_message(massage.chat.id, f'{k}: {v}')

# @bot.message_handler(commands=['add_new_contact'])
# def add_new_contact(massage):
#     name = bot.send_message(massage.from_user.id, 'Введите Имя нового контакта: ', reply_markup = keyboard1)
#     if name in phones_sp:
#         bot.send_message(massage.chat.id,'Контакт существует!')
#     else:
#         coll = bot.send_message(massage.from_user.id, 'Сколько номеров вы хотите ввести: ', reply_markup = keyboard1)
#         numbers = []
#         for i in range(coll):
#             number = bot.send_message(massage.from_user.id, f'Введите {i+1} номер: ', reply_markup = keyboard1)
#             numbers.append(number)
#         city = bot.send_message(massage.from_user.id, 'Введите название города: ', reply_markup = keyboard1)
#         status = bot.send_message(massage.from_user.id, 'Введите статус: ', reply_markup = keyboard1)
#         phones_sp[name] = {'номер телефона': numbers, 'город': city, 'Статус': status}
#         bot.send_message(massage.chat.id, phones_sp[name] )

@bot.message_handler(commands=['add_new_contact'])
def add_new_contact(message):
    msg = bot.send_message(message.from_user.id, 'Введите имя нового контакта: ', reply_markup = keyboard1)
    bot.register_next_step_handler(msg, check_name)

def check_name(message):
    bot.send_message(message.chat.id, f'Обработка имени "{message.text}"...')
    if message.text in phones_sp:
        bot.send_message(message.chat.id,'Контакт существует!')
    else:
        coll = bot.send_message(message.from_user.id, 'Сколько номеров вы хотите ввести: ', reply_markup = keyboard1)
        bot.register_next_step_handler(coll, coll_of_input_phones)
        
def coll_of_input_phones(message):
    bot.send_message(message.chat.id, 'Обработка колличества номеров...')
    coll = int(message.text)
    numbers = []
    phone = bot.send_message(message.from_user.id, f'Введите номер: ', reply_markup = keyboard1)
    for i in range(coll):
        bot.register_next_step_handler(phone , input_phones , numbers,)
    
    

def input_phones(message , numbers):
    phone = bot.send_message(message.from_user.id, f'Введите следущий номер: ', reply_markup = keyboard1)
    number = message.text
    numbers.append(number)
    print(numbers)

bot.polling(none_stop=True)