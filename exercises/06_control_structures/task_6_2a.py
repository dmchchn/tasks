# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input(' Введите IP адрес: ')
ip_split = ip.split('.')
if len(ip_split) != 4:
    print('Неправильный IP адрес')
else:
    try:
        allnumbers = int(ip_split[0]) >= 0 and int(ip_split[0]) <= 255 and int(ip_split[1]) >= 0 and int(ip_split[1]) <= 255 and int(ip_split[2]) >= 0 and int(ip_split[2]) <= 255 and int(ip_split[3]) >= 0 and int(ip_split[3]) <= 255
    except ValueError:
        print('Неправильный IP адрес')
    except IndexError:
        print('Неправильный IP адрес')
    else:
        broadcast = int(ip_split[0]) == 255 and int(ip_split[1]) == 255 and int(ip_split[2]) == 255 and int(ip_split[3]) == 255
        unassigned = int(ip_split[0]) == 0 and int(ip_split[1]) == 0 and int(ip_split[2]) == 0 and int(ip_split[3]) == 0
        if allnumbers is False:
            print('Неправильный IP адрес')
        elif int(ip_split[0]) >= 1 and int(ip_split[0]) <= 223:
            print('unicast')
        elif int(ip_split[0]) >= 224 and int(ip_split[0]) <= 239:
            print('multicast')
        elif broadcast:
            print('local broadcast')
        elif unassigned:
            print('unassigned')
        else:
            print('unused')
