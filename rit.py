#!/usr/bin/python3.5

import dicionariosRacks
import coleta_snmp
import sys

community = 'pub'

# Importando dicionários, neles temos as MIBs relacionado aos racks.
rack4_frio = dicionariosRacks.dici_corredor_4_frio
rack4_quente = dicionariosRacks.dici_corredor_4_quente
rack4_umidade = dicionariosRacks.dici_corredor_4_umidade

rack5_frio = dicionariosRacks.dici_corredor_5_frio
rack5_quente = dicionariosRacks.dici_corredor_5_quente
rack5_umidade = dicionariosRacks.dici_corredor_5_umidade

rack6_frio = dicionariosRacks.dici_corredor_6_frio
rack6_quente = dicionariosRacks.dici_corredor_6_quente
rack6_umidade = dicionariosRacks.dici_corredor_6_umidade
ip = dicionariosRacks.ip

# Essa função faz a consulta snmp no script coleta_snmp
def fun_snmp(mib, community, ip):
    return coleta_snmp.snmp_get(mib, community, ip)

# Essa função pega a média de diversos sensores
# (média fria, média quente e média umidade)
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
cor4_frio = media_corredore(rack4_frio, ip['cor4'])
cor4_quente = media_corredore(rack4_quente, ip['cor4'])
cor4_umidade = media_corredore(rack4_umidade, ip['cor4'])

# Pega média do corredor 5
cor5_frio = media_corredore(rack5_frio, ip['cor5'])
cor5_quente = media_corredore(rack5_quente, ip['cor5'])
cor5_umidade = media_corredore(rack5_umidade, ip['cor5'])

# Pega média do corredor 6
cor6_frio = media_corredore(rack6_frio, ip['cor6'])
cor6_quente = media_corredore(rack6_quente, ip['cor6'])
cor6_umidade = media_corredore(rack6_umidade, ip['cor6'])

racks = [
    [cor4_frio, cor4_quente, cor4_umidade],
    [cor5_frio, cor5_quente, cor5_umidade],
    [cor6_frio, cor6_quente, cor6_umidade]
    ]

for num in range(3):
    print('Corredor {0} - Quente: {1:.1f}°C - Frio: {2:.1f} - Umidade: {3:.1f}%'.format(
        str(num + 4), racks[num][1], racks[num][0], racks[num][2]))
