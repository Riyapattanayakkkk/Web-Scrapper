import os 
from flask import Flask, render_template,request, jsonify
import pandas as pd
from extract import startfun

app = Flask(__name__)

@app.route('/')
def index():
    items, department,data = startfun()

    return render_template('index.html', items=items, departments=department, table=data.to_html())

@app.route('/send-data', methods=['POST'])
def receive_data():
    data = request.json
    input1 = data.get('input1')
    input2 = data.get('input2')
    
    # Process the received data
    print("Received Data:")
    print("Input 1:", input1)
    print("Input 2:", input2)

    # You can do further processing here

    return jsonify({"message": "Data received successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
