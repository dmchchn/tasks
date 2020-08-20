# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
network = input('Введите адрес сети и маску через "/" (пример: 186.19.47.234/27): ')
netmask = network.split('/')
ip = netmask[0]
mask = netmask[1]
ip = ip.split('.')
oct1, oct2, oct3, oct4 = int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])
maskb = '1'*int(mask)+((32-int(mask))*'0')
octmask1, octmask2, octmask3, octmask4 = maskb[0:8], maskb[8:16], maskb[16:24], maskb[24:32]
print(f'''
Network:
{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
{oct1:<08b} {oct2:<08b} {oct3:<08b} {oct4:<08b}
Mask:
/{mask}
{int(octmask1,2):<8} {int(octmask2,2):<8} {int(octmask3,2):<8} {int(octmask4,2):<8}
{int(octmask1,2):<08b} {int(octmask2,2):<08b} {int(octmask3,2):<08b} {int(octmask4,2):<08b}''')
