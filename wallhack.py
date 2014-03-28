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
    exam = mongoengine.ReferenceField("Exam")

app = Flask(__name__)


@app.route("/deleteall", methods=['GET'])
def deleteall():
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
        print("id")
        print(room[0].studentid)
        print(room[0].studentnum)
        print(room[0].classroom)
        student = Student(studentid=room[0].classroom+str(room[0].studentnum))
        student.name = room[0].name
        student.studentnum = room[0].studentnum
        student.classroom = room[0].classroom
        student.studentid = room[0].classroom+str(room[0].studentnum)
        math = Exam()
        math.summary = request.form["summary"]
        math.subject = "math"
        math.datetime= request.form["mathdatetime"]
        math.score = request.form["mathscore"]
        student.exam=math
        math.save()
        student.save()

        student = Student(studentid=room[0].classroom+str(room[0].studentnum))
        student.name = room[0].name
        student.studentnum = room[0].studentnum
        student.classroom = room[0].classroom
        student.studentid = room[0].classroom+str(room[0].studentnum)
        english = Exam()
        english.summary = request.form["summary"]
        english.subject = "english"
        english.datetime= request.form["englishdatetime"]
        english.score = request.form["englishscore"]
        student.exam=english
        english.save()
        student.save()

        student = Student(studentid=room[0].classroom+str(room[0].studentnum))
        student.name = room[0].name
        student.studentnum = room[0].studentnum
        student.classroom = room[0].classroom
        student.studentid = room[0].classroom+str(room[0].studentnum)
        science = Exam()
        science.summary = request.form["summary"]
        science.subject = "science"
        science.datetime= request.form["sciencedatetime"]
        science.score = request.form["sciencescore"]
        student.exam=science
        science.save()
        student.save()

        student = Student(studentid=room[0].classroom+str(room[0].studentnum))
        student.name = room[0].name
        student.studentnum = room[0].studentnum
        student.classroom = room[0].classroom
        student.studentid = room[0].classroom+str(room[0].studentnum)
        social = Exam()
        social.summary = request.form["summary"]
        social.subject = "social"
        social.datetime= request.form["socialdatetime"]
        social.score = request.form["socialscore"]
        student.exam=social
        social.save()
        student.save()

        student = Student(studentid=room[0].classroom+str(room[0].studentnum))
        student.name = room[0].name
        student.studentnum = room[0].studentnum
        student.classroom = room[0].classroom
        student.studentid = room[0].classroom+str(room[0].studentnum)
        language = Exam()
        language.summary = request.form["summary"]
        language.subject = "language"
        language.datetime= request.form["languagedatetime"]
        language.score = request.form["languagescore"]
        student.exam=language
        language.save()
        student.save()
        return render_template('student.html', posts=room)
    else:
        return render_template('student.html', posts=room)

app.run(debug=True, host='0.0.0.0')
