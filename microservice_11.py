#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request #import main Flask class and request object
import pika 
import MySQLdb
import json
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#from urlparse import parse_qs
import cgi
import boto3
import os

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


class Microservice:
    app = Flask(__name__)
    @app.route('/microservicio/consultaproductoscatalogo', methods=['GET'])
    def consulta_producto_catalogo():

        if request.method == "GET":
            
            try:

                #dynamodb = boto3.client('dynamodb',aws_access_key_id=os.environ.get('aws_access_key_id'), aws_secret_access_key=os.environ.get('aws_access_key_secret'), region_name=os.environ.get('region'))
                catalogo = request.args.get('catalogo')


                db = MySQLdb.connect(host="microservices.c2v15my6uhyr.us-east-2.rds.amazonaws.com", user="root", passwd="uniandes1",  port=3306, db="microservices")        
                cur = db.cursor()
                query = ("SELECT * FROM productoxcatalogo WHERE id_catalogo = %s")
                cur.execute(query, [catalogo])
                rows = cur.fetchall()
                items =[]


                columns = [desc[0] for desc in cur.description]
                result = []
                for row in rows:
                    row = dict(zip(columns, row))
                    result.append(row)    

                items = json.dumps({'producto':result}, indent=4, sort_keys=True, cls=DecimalEncoder)    

                db.close()
            
                return items

            except Exception as e:
                print("Error: ")
                print (e)
                return  json.dumps({'msg': "No hay productos asociados al catalogo"})

    if __name__ == '__main__':
        app.run(host="0.0.0.0", debug=True, port=5010)
