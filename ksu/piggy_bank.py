# {
#   "balance": 1000,
#   "operations": [
#     {
#       "time": "",
#       "name": "",
#       "money": ""
#     },
#     {
#       "time": "",
#       "name": "",
#       "money": ""
#     },
#     {
#       "time": "",
#       "name": "",
#       "money": ""
#     },
#     {
#       "time": "",
#       "name": "",
#       "money": ""
#     }
#   ]
# }
# 1 - начало - подгружать данные из файла, если он есть 
# 1.1 - если файла нету - писать об этом в консоль или предлагать создать его и пополнить баланс
# 2 - если файл есть - получаем файл в переменную и достаем из него информацию (file["balance"] или file["operations"])
# 3 - передать наш баланс в функции, чтобы считать его в дальнейшем
# 4 - создать обработчик операций
# 5 - конец работы программы — проверить баланс и операции

import logging  
import json
import datetime


logging.basicConfig(level=logging.DEBUG, format= '%(levelname)s: %(message)s %(asctime)s', filename='operations_history.log') 

config = {
        'снять': {
            'prompt': 'Введите сумму, которую нужно снять ',
            'multiplier': -1,
            'action': 'снятие',
            'action_message': 'Произведено снятие'
        },
        'пополнить': {
            'prompt': 'Введите сумму пополнения ',
            'multiplier': 1,
            'action': 'зачислена сумма',
            'action_message': 'Произведено пополнение на сумму'
        },
        'разбить': {
            'crash_confirmation': 'Вы уверены? Продолжить/отмена ',
            'action_message_confirmed': 'Копилка разбита, счет обнулен',
            'action_message_denied': 'Разбитие отменено'
        }
    }

def operation(data_dict, config): #создаем функцию для снятия и пополнения
    expenses_amount = int(input(config['prompt']))  #ввод числа и сообщение
    
    if expenses_amount >= 0: #условие чтобы не было отрицательных чисел
        data_dict["balance"] = (config['multiplier'] * expenses_amount) + data_dict["balance"] #арифметика 
        now = datetime.datetime.now()
        data_dict["operations"].append({
            "time": now.strftime("%H:%M:%S"),
            "name": action,
            "money": expenses_amount
        })
        print(f'{config['action_message']} {expenses_amount} руб. Текущий баланс: {data_dict["balance"]}') #вывод чтобы было видно что операция прошла
        with open("operation_data_file.json", "w", encoding="utf-8") as f:
            json.dump(data_dict, f, ensure_ascii=False, indent=2)
    else:
        negative_num_error() 

    return data_dict

def crash(data_dict, config): #для разбития
    confirmation = input(config['crash_confirmation']).lower() #запрашиваем подтверждение

    if confirmation == 'продолжить':
        print(config['action_message_confirmed']) 
        now = datetime.datetime.now()
        data_dict["operations"].append({
            "time": now.strftime("%H:%M:%S"),
            "name": action,
            "money": "счет обнулен"
        })
        data_dict["balance"] = 0
        with open("operation_data_file.json", "w", encoding="utf-8") as f:
            json.dump(data_dict, f, ensure_ascii=False, indent=2)

    elif confirmation == 'отмена':
        print(config['action_message_denied'])
    else:
        print('Ошибка: введена некорректная команда')
        logging.error('Введена некорректная команда')    
         
    return data_dict

def negative_num_error(): 
    print('Ошибка: введено отрицательное число')
    logging.error('Введено отрицательное число')  

# собрать все данные и вернуть из функции
# return ( balance, operations )

def load_data():
    try:
        with open("operation_data_file.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        data_dict = data
        return data_dict
    except FileNotFoundError:
        print('Выполните свою первую транзакцию')
        data_dict = {
            "balance": 0,
            "operations": [

            ]
        }
        data_dict['balance'] = int(input("Введите баланс: "))
        return data_dict

data_dict = load_data()
while True:
    transactions = input('Выполняем действие? да/нет ').lower()
    if transactions == 'да':
        try: #сюда трай для ошибок
            action = input('Выберите действие: пополнить/снять/разбить ').lower() #действие
            if action == 'пополнить': 
                operation(data_dict, config[action]) #Функция пополнения
            elif action == 'снять':
                operation(data_dict, config[action])  #функция снятия
            elif action == 'разбить':
                crash(data_dict, config[action]) #функция  для разбития 
            else:
                print('Действие отсутствует') #штобы краказябру не писали вместо действий
                logging.error('Действие отсутствует') # лог если все-таки написали
        except ValueError: #чтобы краказябру не писали вместо чисел
            print('Ошибка: введены не числа')
            logging.error('Введены не числа')
    elif transactions == 'нет':
        print('Спасибо, что выбрали нас! До свидания!')

        break
    else:
        logging.error('Введена некорректная команда')
        print('Ошибка: введена некорректная команда')


 
