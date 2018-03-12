#!/usr/bin/python
import MySQLdb
import json
import sys
import boto
import time
import boto.sdb
import boto.dynamodb2
from flask import Flask, request 
from boto.dynamodb2.fields import HashKey, RangeKey, KeysOnlyIndex, GlobalAllIndex
from boto.dynamodb2.table import Table
from boto.dynamodb2.types import NUMBER


conn = boto.dynamodb.connect_to_region(
    'us-east-1',
    aws_access_key_id='AKIAIQCRHLBZV3V555MQ',
    aws_secret_access_key='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')

print(conn.list_tables())

#tabla=conn.get_table('Producto')

#millis = int(round(time.time() * 1000))
#itemdata={
#    'id_producto':56,
#    'referencia': 'ARTI-0001',
#    'nombre': 'Arte Techo',
#    'categoria': 'Lámpara Techo',
#    'catalogo': 'Catálogo Inicial',
#    'proveedor': 'Edna Acosta'
#}


#item = tabla.new_item(
#	hash_key='id_producto',
#    range_key='nombre',
#    attrs=itemdata
#)
#item.put()

#item = tabla.get_item(nombre='Mati Lamp')

#item

#print(conn.list_tables())
#print ('hola')
