from flask   import Flask, render_template, request, redirect, url_for
import mongoengine

mongoengine.connect("wallhackexam")

class Exam(mongoengine.Document):
    summary = mongoengine.StringField()
    subject = mongoengine.StringField()
    datetime = mongoengine.DateTimeField()
    score = mongoengine.IntField(min_value=0,max_value=100)

class Student(mongoengine.Document):
    name = mongoengine.StringField()
    studentnum = mongoengine.IntField()
    classroom = mongoengine.StringField()
    studentid = mongoengine.StringField(primary_key=True)
    exam = mongoengine.ListField(mongoengine.ReferenceField("Exam"))

app = Flask(__name__)


@app.route("/deleteall", methods=['GET'])
def deleteall():
    Exam.drop_collection()
    Student.drop_collection()
    return "deleted"

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/student-add", methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        print(request.form['studentname'])
        print(request.form['studentnum'])
        print(request.form['classroom'])
        posts = Student()
        posts.name = request.form['studentname']
        posts.studentnum = request.form['studentnum']
        posts.classroom = request.form['classroom']
        student_id = request.form['classroom'] + str(request.form['studentnum'])
        posts.studentid = student_id
        posts.save()
        return redirect(url_for('student-add'))
    else:
        return render_template('student-add.html', posts=Student)

@app.route("/classroom/<classname>", methods=['GET'])
def classroom(classname):
    room = Student.objects(classroom=classname.upper())
    return render_template('classroom.html', posts=room)

@app.route("/classroom/<classname>/<studentnumber>", methods=['GET','POST'])
def studentprofile(classname,studentnumber):
    room = Student.objects(classroom=classname.upper(),studentnum=studentnumber)
    if request.method == 'POST':
        student = room[0]
        math = Exam()
        math.summary = request.form["summary"]
        math.subject = "math"
        math.datetime= request.form["mathdatetime"]
        math.score = request.form["mathscore"]

        english = Exam()
        english.summary = request.form["summary"]
        english.subject = "english"
        english.datetime= request.form["englishdatetime"]
        english.score = request.form["englishscore"]

        science = Exam()
        science.summary = request.form["summary"]
        science.subject = "science"
        science.datetime= request.form["sciencedatetime"]
        science.score = request.form["sciencescore"]

        social = Exam()
        social.summary = request.form["summary"]
        social.subject = "social"
        social.datetime= request.form["socialdatetime"]
        social.score = request.form["socialscore"]

        language = Exam()
        language.summary = request.form["summary"]
        language.subject = "language"
        language.datetime= request.form["languagedatetime"]
        language.score = request.form["languagescore"]

        student.exam=[math, english, science, social, language]

        math.save()
        english.save()
        science.save()
        social.save()
        language.save()
        student.save()
        return render_template('student.html', posts=room)
    else:
        return render_template('student.html', posts=room)

app.run(debug=True, host='0.0.0.0')
