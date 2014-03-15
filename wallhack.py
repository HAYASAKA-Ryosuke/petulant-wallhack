from flask   import Flask, render_template
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
posts  = client['mongotest']['testData']

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', posts=posts)

app.run(debug=True, host='0.0.0.0')
