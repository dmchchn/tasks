# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
# Solution
cmd1 = command1.split()[-1].split(',')
cmd2 = command2.split()[-1].split(',')
cmd1 = set(cmd1)
cmd2 = set(cmd2)
commands=cmd1.intersection(cmd2)
result=list(commands)
result.sort()
print(result)
