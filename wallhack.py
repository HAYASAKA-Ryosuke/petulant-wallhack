from flask   import Flask, render_template, request, redirect, url_for
import mongoengine

mongoengine.connect("wallhackexam")

class Student(mongoengine.Document):
    name = mongoengine.StringField()
    studentnum = mongoengine.IntField()
    classroom = mongoengine.StringField()

#Student.drop_collection()

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/student", methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        print(request.form['studentname'])
        print(request.form['studentnum'])
        print(request.form['classroom'])
        posts = Student()
        posts.name = request.form['studentname'] 
        posts.studentnum = request.form['studentnum']
        posts.classroom = request.form['classroom']
        posts.save()
        return redirect(url_for('student'))
    else:
        return render_template('student.html', posts=Student)

@app.route("/classroom/<classname>", methods=['GET'])
def classroom(classname):
    room = Student.objects(classroom=classname.upper())
    return render_template('classroom.html', posts=room)

app.run(debug=True, host='0.0.0.0')
