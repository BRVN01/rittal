#!/usr/bin/python3.5

import coleta_snmp
import sys

community = 'pub'
corredor_4_ip = "10.2.9.26"
corredor_5_ip = "10.2.9.27"
corredor_6_ip = "10.2.9.28"

dici_corredor_4_frio = {
    'F38': 'cmcIIIVarValueStr.2.2',
    'P38': 'cmcIIIVarValueStr.4.2',
    'K38': 'cmcIIIVarValueStr.11.2',
    'F35': 'cmcIIIVarValueStr.7.2',
    'P35': 'cmcIIIVarValueStr.10.2',
    'K35': 'cmcIIIVarValueStr.8.2'
    }

dici_corredor_4_quente = {
    'K38': 'cmcIIIVarValueStr.3.2',
    'K35': 'cmcIIIVarValueStr.9.2'
    }

dici_corredor_4_umidade = {
    'F38': 'cmcIIIVarValueStr.2.12',
    'P38': 'cmcIIIVarValueStr.4.11',
    'F35': 'cmcIIIVarValueStr.7.12',
    'P35': 'cmcIIIVarValueStr.10.12',
    'K35': 'cmcIIIVarValueStr.8.11'
    }


def fun_snmp(mib, community, ip):
    return snmp.snmp_get(mib, community, ip)


def media_corredore(dicionario, ip):
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

# Pega média do corredor 4
temp_cor4_frio = media_corredore(dici_corredor_4_frio, corredor_4_ip)
temp_cor4_quente = media_corredore(dici_corredor_4_quente, corredor_4_ip)
temp_cor4_umidade = media_corredore(dici_corredor_4_umidade, corredor_4_ip)

# Pega média do corredor 5

# Pega média do corredor 6


print('Corredor 4 - Quente: {0:.1f}°C - Frio: {1:.1f}°C - Umidade: {2:.1f} %'.format(temp_cor4_quente, temp_cor4_frio, temp_cor4_umidade))

