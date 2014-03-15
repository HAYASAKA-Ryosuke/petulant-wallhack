from flask   import Flask, render_template, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
posts  = client['mongotest']['testData']

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['check'] == "yes!":
            return "True"
        else:
            return "False"
    else:
        return render_template('index.html', posts=posts)

app.run(debug=True, host='0.0.0.0')
