# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_correct = False
while not ip_correct:
    ip = input('Введите IP адрес: ')
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
            ip_correct = allnumbers
            if ip_correct is False:
                print('Неправильный IP адрес')
            elif int(ip_split[0]) >= 1 and int(ip_split[0]) <= 223:
                print('unicast')
            elif int(ip_split[0]) >= 224 and int(ip_split[0]) <= 239:
                print('multicast')
            elif broadcast is True:
                print('local broadcast')
            elif unassigned is True:
                print('unassigned')
            else:
                print('unused')
