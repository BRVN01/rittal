#!/usr/bin/python3.5
from easysnmp import Session
import sys


def snmp_get(oid, community, ip):

    session = Session(
        hostname=ip,
        community=community,
        version=2)

    value = session.get(oid)
    value = '"{}"'.format(value)

    val = value[value.find('value=')+7:value.find('degree')]

    erro = val[:14]

    if (erro == 'NOSUCHINSTANCE'):
        print('Erro na OID:', oid)
        sys.exit(10)

    else:
        return (val[0:6])


# valor = snmp_get('MIB', 'COMMUNITY', 'IP')
# print(valor)
