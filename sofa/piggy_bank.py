# балансовые операции в json файл. ошибки так же в лог

# now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S")) # Выведет: 14:30:05 (пример)

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

#czet = начальная цена. output = то что мы вычисляем.
#balace = конечная цена


# with open("student.json", "r", encoding="utf-8") as f:
#     student = json.load(f)

# print(student["name"])      # Анна
# print(student["courses"])   with open("student.json", "r", encoding="utf-8") as f:
#     student = json.load(f)

# print(student["name"])      # Анна
# print(student["courses"])   


import logging
import json
import datetime

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s - %(asctime)s", filename="copilko.log")


def load_data():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            slovar = json.load(file)
    except:     
        slovar = {
            "balance": 0,
            "operation": []
            }
        
        slovar["balance"] = int(input("введите баланс "))

    return slovar

slovar = load_data

def replenishment(output, slovar):    #пополнение

    slovar["balance"] += output
    now = datetime.datetime.now()
    slovar["operation"].append(
        {   
            "time": now.strftime("%H:%M:%S"),
            "name": "пополнение",
            "money": output
            
        }
    )

    with open("data.json", "w", encoding= "utf-8") as file:  #записываем баланс в файл
        json.dump(slovar, file, ensure_ascii= False, indent= 2)
    if output <= 0:
        logging.info(f"пополнение на сумму {output} невозможно")

    return slovar

def withdrawal(output, slovar):    #вывод

    slovar["balance"] = slovar["balance"] - output
    now = datetime.datetime.now()
    slovar["operation"].append(
        {   
            "time": now.strftime("%H:%M:%S"),
            "name": "вывод деняг",
            "money": output
            
        }
    )

    with open("data.json", "w", encoding= "utf-8") as file:  #записываем баланс в файл
        json.dump(slovar, file, ensure_ascii= False, indent= 2)

    if balance < output:      #если уходит в ноль
        logging.info(f"счет ушел в минус: {czet - output}") 

    return slovar


def devastation(): #обнуление
    
    slovar["balance"] = 0
    now = datetime.datetime.now()
    slovar["operation"].append(
        {   
            "time": now.strftime("%H:%M:%S"),
            "name": "разбитие",
            "money": 0
            
        }
    )

    with open("data.json", "w", encoding= "utf-8") as file:  #записываем баланс в файл
        json.dump(slovar, file, ensure_ascii= False, indent= 2)

    return slovar



while True:

    try:
        do = int(input("введите функцию. 1 - пополнение, 2 - вывод денег, 3 - «разбить» копилку "))

        if do in [1, 2]:      #проверка функции пополнение или вывод
            output = int(input("Сколько пополнянем/выводим?")) #общая переменная 

            if output < 0:
                raise ValueError

        if do == [1]:
            replenishment(output, slovar)
            if output == 0:
                logging.info(f"Пополнение счета на {output} невозможно") 
        if do == [2]:
            balance == withdrawal(output, slovar)

        elif do in [3]:      #проверка функции разбивание
            balance = devastation()

        else:
            logging.warning("такой функции не существует")
    
        exit_programm = int(input("Хотите выйти из приложения? 1 - да, 2 - нет "))
        if exit_programm == 1:
            print("до скорого")
            break

    except ZeroDivisionError:
        logging.error("Введены не числа")
    except ValueError:
        logging.error("Введены буквы/отрицательные числа")
    except Exception as e:
        logging.error("Что-то сломалось")
