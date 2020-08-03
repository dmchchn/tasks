# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "O      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
# Solution

string1=ospf_route.replace('O','OSPF').replace(',','').split()
string1.remove('via')
print(
        'Protocol:           {}'.format(string1[0]),'\n'
        'Prefix:             {}'.format(string1[1]),'\n'
        'AD/Metric:          {}'.format(string1[2]),'\n'
        'Next-Hop:           {}'.format(string1[3]),'\n'
        'Last update:        {}'.format(string1[4]),'\n'
        'Outbound Interface: {}'.format(string1[5]),'\n')
