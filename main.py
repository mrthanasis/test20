from flask import Flask, jsonify, request
import io
import csv
from flask import make_response, Response
app=Flask(__name__)
from app import lastdaysresults
import pandas as pd

@app.route("/lastxdays",methods=['GET','POST'])
def lastxdays():
    if request.method=='POST':
        some_jason=request.get_json()
        result=lastdaysresults(some_jason['days'])[0]
        return jsonify(result)
    else:
        return jsonify({'Error':"App Error"})

@app.route("/periods",methods=['GET','POST'])
def periods():
    if request.method=='POST':
        some_jason=request.get_json()
        result=lastdaysresults(some_jason['days'])[1]
        return jsonify(result)
    else:
        return jsonify({'Error':"App Error"})

@app.route("/breakdown",methods=['GET','POST'])
def breakdown():
    if request.method=='POST':
        some_jason=request.get_json()
        result=lastdaysresults(some_jason['days'])[2]
        return jsonify(result)
    else:
        return jsonify({'Error':"App Error"})


@app.route("/download",methods=['GET','POST'])

def download():
	if request.method=='POST':
		some_jason=request.get_json()
		result=pd.DataFrame(lastdaysresults(some_jason['days'])[0]).to_csv(sep=',')
		return Response(result,mimetype="text/csv",headers={"Content-disposition":"attachment; filename=lastxdays.csv"})
	else:
		return jsonify({'Error':"App Error"})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=9091)