# -*- coding: utf-8 -*-
__author__ = 'Fanzhong'

from flask import Flask, render_template
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import json
app = Flask(__name__)

'''
This is my website index
I'll create my website from now
data: 2015.04.10
'''
def get_from_s3():
    conn = S3Connection('AKIAJZ5NU5RXHVW3QXPA', 'dHE5tDMMk/WwAoyvrd44TaKsJfnNqLSjEUGOmXt5')
    bucketname = conn.get_bucket('scrapy_data_2')
    print bucketname
    k = Key(bucketname)
    k.key = 'my_scrapy'
    k.get_contents_to_filename('getjson.json')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/qiche")
def qiche():
    testdata=[]
    try:
        with open("getjson.json") as jsf:
            for each_line in jsf:
                js = json.loads(each_line,encoding='utf-8')
                getjson = json.dumps(js, ensure_ascii=False)
                print(type(getjson))
    except IOError as err:
        print('err was' + str(err))
        #return render_template('qiche.html' , testdata={'error':'nothingloaded'})
    return render_template('qiche.html' , testdata=testdata)

if __name__ == '__main__':
    get_from_s3()
    app.run(debug = True)