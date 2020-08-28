# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""
type_int = input('Введите тип интерфейса (access/trunk): ')
interface = input('Введите номер интерфейса в формате Fa*/*,Gi*/*: ')

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

access_input = 'Введите номер VLAN: '
trunk_input = 'Введите разрешенные VLANы: '
inputs = dict(access = access_input, trunk = trunk_input)

templates = dict(access = access_template,trunk = trunk_template)
vlan = input(inputs[type_int])

print('interface {}'.format(interface))
print('\n'.join(templates[type_int]).format(vlan))
