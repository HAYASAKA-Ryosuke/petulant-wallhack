from flask   import Flask, render_template, request
import mongoengine

mongoengine.connect("wallhacke-test")

app = Flask(__name__)
class Student(mongoengine.Document):
    name= mongoengine.StringField()

posts = Student()


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
