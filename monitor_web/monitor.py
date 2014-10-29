#!pyenv/bin/python
import os
import re
import MySQLdb 
from flask import  Flask,request,render_template
import json

app = Flask(__name__)
db = MySQLdb.connect(user='root',passwd='root',db='falcon',charset='utf8')
db.autocommit(True)
cur = db.cursor()

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.json
        try:
            sql = "INSERT INTO `stat` (`host`,`mem_free`,`mem_usage`,`mem_total`,`load_avg`,`time`) VALUES('%s', '%d', '%d', '%d', '%s', '%d')" % (data['Host'], data['MemFree'], data['MemUsage'], data['MemTotal'], data['LoadAvg'], int(data['Time']))
            ret = cur.execute(sql)
        except MySQLdb.IntegrityError:
            pass
        return 'ok'
    else:
        return render_template('index.html')

@app.route('/data',methods=['GET'])
def getData():
    cur.execute("select `time`,`mem_usage` from `stat`")
    one_res = [[i[0]*1000,i[1]] for i in cur.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(one_res))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
