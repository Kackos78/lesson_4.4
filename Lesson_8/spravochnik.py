# Сделать телефонный справочник + внешнее хранилище :)

import json

phones_sp = {'дядя коля': {'номер телефона': ['8-800-555-35-35', '8-900-536-35-35'], 'город': 'Сыктыфкар', 'Статус': 'дядя'}, 'нюрка': {'номер телефона': ['8-555-549-34-35'], 'город': 'Сыктыфкар', 'Статус': 'тетя'}}


def save():
    with open('phones.json','w', encoding='utf-8') as phones:
        phones.write(json.dumps(phones_sp, ensure_ascii=False))
    print('Обновленная телефонная книга сохранена в файле phones.json')

def load(phones_sp):
    with open('phones.json','r', encoding='utf-8') as phones:
        phones_sp = json.load(phones)
        print('Справочник был обновлен!')
        return phones_sp

def print_all():
    print('Вот текущий список номеров') 
    for k, v in phones_sp.items():
        print(k, v)

def add_new_contact():
    name = input('Введите имя нового контакта: ')
    if name in phones_sp:
        print('Контакт существует!')
    else:
        coll = int(input('Сколько номеров вы хотите ввести: '))
        numbers = []
        for i in range(coll):
            number = input(f'Введите {i+1} номер: ')
            numbers.append(number)
        city = input('Введите название города: ')
        status = input('Введите статус: ')
        phones_sp[name] = {'номер телефона': numbers, 'город': city, 'Статус': status}
    
def change_contact():
    name = input('Введите имя контакта: ')
    if name not in phones_sp:
        print('Контакта не существует!')
    else: 
        what_to_change = input('Введите что вы хотите изменить: (number, city, status)')
        if what_to_change == 'number':
            phone = input('Введите номер: ')
            if phone in phones_sp[name]['номер телефона']:
                print('Номер существует')
            else:
                phones_sp[name]['номер телефона'].append(phone)
        elif what_to_change == 'city':
            city = input('Введите название города: ')
            phones_sp[name] = {'город': city}
        elif what_to_change == 'status':
            status = input('Введите статус: ')
            phones_sp[name] = {'Статус': status}
        else: print('Непредвиденная ошибка, пожалуйста начните заново :(')

def search():
    what_to_search = input('Введите что нужно найти: (name, number, city, status): ')
    if what_to_search == 'name':
        name = input('Введите имя: ')
        if name in phones_sp:
            print('Результат поиска: ')
            print(f'{name}: {phones_sp.get(name)}')
    elif what_to_search == 'number':
        number = input('Введите номер телефона: ')
        for key in phones_sp:
            if number in phones_sp[key]['номер телефона']:
                print('Телефон найден: ')
                print(phones_sp[key])
                return
        print('Телефон не найден')
        question = input('Хотите ли внести номер в существующий контакт? (Yes/No)')
        if question == 'Yes':
            change_contact()
        else: return
    elif what_to_search == 'city':
        city = input('Введите город: ')
        for key in phones_sp:
            if phones_sp[key]['город'] == city:
                print(f'{key}: {phones_sp.get(key)}')
        
    elif what_to_search == 'status':
        status = input('Введите город: ')
        for key in phones_sp:
            if phones_sp[key]['статус'] == status:
                print(f'{key}: {phones_sp.get(key)}')
    else: print('Ошибка ввода, пожалуйста изучите мануал')

def delete_contact():
    what_name_delete = input('Введите контакт для его удаления: ')
    if what_name_delete in phones_sp:
        phones_sp.popitem(what_name_delete)
        print('Контакт удален.')
    else: print('Контакте не существует.')
    
def print_help():
    help = {'//all': 'Вывести весь телефонный справочник', '/add_new_contact': 'Добавить новый контакт',
             '/change_contact':'Изменить уже существующий контакт',
               '/save':'Сохранить изменения в файл phones.json', '/load':'Загрузить данные из файла phones.json','/search': 'Найти данные в справочнике', '/delete_contact': 'Удалить контакт',
                 '/help': 'Вывод подсказок по использованию справочника'}
    print('Вот полный список комманд: ')
    for k, v in help.items():
        print(f' {k}: \t\t {v}')
    
while True:
    command = input('Введите команду: ')
    if command == '/all':
        print_all()
    elif command == '/add_new_contact':
        add_new_contact()
    elif command == '/change_contact':  
        change_contact()
    elif command == '/save':
        save()
    elif command == '/load':
        phones_sp = load(phones_sp)
    elif command == '/search':
        search()
    elif command == '/delete_contact':
        delete_contact()
    elif command == '/help':
        print_help()
    else: print('Не опознанная команда. Просьба изучить мануал через /help')
