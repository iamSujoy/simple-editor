from flask import Flask, request, jsonify, render_template
from utils.excute import ExcuteCode
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = dict()
        data = json.loads(request.get_data())
        runner = ExcuteCode(data["langauge"], data["code"])
        data['output'] = runner.run()
        print(data)
        return jsonify(data)
    return render_template('index.html') 



