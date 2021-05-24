from flask import Flask, render_template, request, redirect
import json
import test

app = Flask(__name__)


# Home
@app.route("/")
def index():
    return render_template('index.html')


# Dynamic page changer
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        add_to_json(data)
        test.get_csv()
        return redirect('thankyou.html')
    else:
        return 'something went wrong :('


# -------------------------------------------------------------------------------------------------
def add_to_json(data):
    json_data = json.load(open('data.json'))
    json_data.append(data)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2, default=str)


# RUN OUR SERVER ----------------
# > set FLASK_APP=main.py
# > set FLASK_ENV=development  |-- if debug
# > flask run
