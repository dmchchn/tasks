# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
network = argv[1]
netmask = network.split('/')
ip = netmask[0]
mask = netmask[1]
ip = ip.split('.')
okt1, okt2, okt3, okt4 = int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])
ip_bin = f'{okt1:08b}{okt2:08b}{okt3:08b}{okt4:08b}'
ip_by_mask = ip_bin[0:int(mask)]+(32-int(mask))*'0'
mask_bin = int(mask)*'1'+(32-int(mask))*'0'
oktmask1, oktmask2, oktmask3, oktmask4 = mask_bin[0:8], mask_bin[8:16], mask_bin[16:24], mask_bin[24:32]
ipbm = ip_by_mask
okt1, okt2, okt3, okt4 = ipbm[0:8], ipbm[8:16], ipbm[16:24], ipbm[24:32]
print(f'''
Network:
{int(okt1, 2):<8} {int(okt2, 2):<8} {int(okt3, 2):<8} {int(okt4, 2):<8}
{okt1:<8} {okt2:<8} {okt3:<8} {okt4:<8}
Mask:
/{mask}
{int(oktmask1,2):<8} {int(oktmask2,2):<8} {int(oktmask3,2):<8} {int(oktmask4,2):<8}
{oktmask1:<8} {oktmask2:<8} {oktmask3:<8} {oktmask4:<8}''')
