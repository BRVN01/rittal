#!/usr/bin/env python3

import dicionariosRacks
import coleta_snmp
import sys

community = 'pub'

# Importando dicionários, neles temos as MIBs relacionado aos racks.
rack4_DADO3 = dicionariosRacks.dici_NOME
rack4_DADO1 = dicionariosRacks.dici_NOME
rack4_DADO2 = dicionariosRacks.dici_NOME

rack5_DADO3 = dicionariosRacks.dici_NOME
rack5_DADO1 = dicionariosRacks.dici_NOME
rack5_DADO2 = dicionariosRacks.dici_NOME

rack6_DADO3 = dicionariosRacks.dici_NOME
rack6_DADO1 = dicionariosRacks.dici_NOME
rack6_DADO2 = dicionariosRacks.dici_NOME
ip = dicionariosRacks.ip

# Essa função faz a consulta snmp no script coleta_snmp
def fun_snmp(mib, community, ip):
    return coleta_snmp.snmp_get(mib, community, ip)

# Essa função pega a média de diversos sensores
# (média fria, média DADO1 e média DADO2)
def media_POSIÇÃOe(dicionario, ip):
    lista = []
    for i in dicionario.keys():
        try:
            temperatura = float(fun_snmp(dicionario[i], community, ip))

        except:
            print('Erro na MIB, verificar a MIB:', dicionario[i])
            sys.exit(10)

        lista.append(temperatura)

    soma = sum(lista)
    return soma / len(dicionario.keys())

# Pega média do POSIÇÃO 4
POSIÇÃO_DADO3 = media_POSIÇÃO(rack4_DADO3, ip['POSIÇÃO'])
POSIÇÃO_DADO1 = media_POSIÇÃO(rack4_DADO1, ip['POSIÇÃO'])
POSIÇÃO_DADO2 = media_POSIÇÃO(rack4_DADO2, ip['POSIÇÃO'])

# Pega média do POSIÇÃO 5
POSIÇÃO_DADO3 = media_POSIÇÃO(rack5_DADO3, ip['POSIÇÃO'])
POSIÇÃO_DADO1 = media_POSIÇÃO(rack5_DADO1, ip['POSIÇÃO'])
POSIÇÃO_DADO2 = media_POSIÇÃO(rack5_DADO2, ip['POSIÇÃO'])

# Pega média do POSIÇÃO 6
POSIÇÃO_DADO3 = media_POSIÇÃO(rack6_DADO3, ip['POSIÇÃO'])
POSIÇÃO_DADO1 = media_POSIÇÃO(rack6_DADO1, ip['POSIÇÃO'])
POSIÇÃO_DADO2 = media_POSIÇÃO(rack6_DADO2, ip['POSIÇÃO'])

racks = [
    [POSIÇÃO_DADO3, POSIÇÃO_DADO1, POSIÇÃO_DADO2],
    [POSIÇÃO_DADO3, POSIÇÃO_DADO1, POSIÇÃO_DADO2],
    [POSIÇÃO_DADO3, POSIÇÃO_DADO1, POSIÇÃO_DADO2]
    ]

for num in range(3):
    print('POSIÇÃO {0} - DADO1: {1:.1f}°C - DADO3: {2:.1f} - DADO2: {3:.1f}%'.format(
        str(num + 4), racks[num][1], racks[num][0], racks[num][2]))
