from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# CORS(app, resources={r"/*": {"origins": "http://114.55.128.71:8081"}})

app.config['DATABASE'] = {
    'host': 'localhost',
    'port': '5432',
    'database': 'school',
    'user': 'postgres',
    'password': '123456'
}

def connect_to_database():
    conn = psycopg2.connect(
        host=app.config['DATABASE']['host'],
        port=app.config['DATABASE']['port'],
        dbname=app.config['DATABASE']['database'],
        user=app.config['DATABASE']['user'],
        password=app.config['DATABASE']['password']
    )
    return conn

@app.route('/students', methods=['GET'])
def get_students():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    return jsonify({'students': students})



@app.route('/students/getstudentsById', methods=['GET'])
def get_studentById():
    sid = request.args.get('sid')  
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE sid = %s', (sid,))
    student = cursor.fetchone()
    if student:
        return jsonify({'student': student})
    else:
        return jsonify({'message': 'Student not found'}), 404



@app.route('/addstudents', methods=['POST'])
def add_student():
    conn = connect_to_database()
    cursor = conn.cursor()
    data = request.get_json()
    sid = data.get('sid')
    sname = data.get('sname')
    email = data.get('email')
    grade = data.get('grade')
    password = data.get('password')
    if sid:
        cursor.execute('INSERT INTO students VALUES (%s,%s,%s,%s,%s)',
                       (str(sid),str(sname),str(email),str(grade),str(password)))
        conn.commit()
        return jsonify({'message': 'Students added successfully'})
    else:
        return jsonify({'message': 'Invalid request'}), 400




@app.route('/students/updatestudents', methods=['POST'])
def update_student():

    conn = connect_to_database()
    cursor = conn.cursor()
    data = request.get_json()
    sid = data.get('sid')
    email = data.get('email')
    grade = data.get('grade')
    if sid:
        cursor.execute('UPDATE students SET email = %s WHERE sid = %s', (email, sid))
        cursor.execute('UPDATE students SET grade = %s WHERE sid = %s', (grade, sid))
        conn.commit()
        return jsonify({'message': 'students updated successfully'})
    else:
        return jsonify({'message': 'Invalid request'}), 400

@app.route('/students/deletestudentsById', methods=['GET'])
def deletestudentsById():
    sid = request.args.get('sid')  
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM students WHERE sid = %s', (sid,))
        conn.commit()  
        return jsonify({'message': 'Student deleted successfully'})
    except Exception as e:
        conn.rollback() 
        return jsonify({'message': r'Failed to delete student: {str(e)}'}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/teachers', methods=['GET'])
def get_teachers():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM teachers')
    teachers = cursor.fetchall()
    return jsonify({'teachers': teachers})


@app.route('/teachers/getteachersById', methods=['GET'])
def get_teacherById():
    tid = request.args.get('tid') 
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM teachers WHERE tid = %s', (tid,))
    teacher = cursor.fetchone()
    if teacher:
        return jsonify({'teacher': teacher})
    else:
        return jsonify({'message': 'Teacher not found'}), 404

@app.route('/addteachers', methods=['POST'])
def add_teacher():
    conn = connect_to_database()
    cursor = conn.cursor()
    data = request.get_json()
    tid = data.get('tid')
    tname = data.get('tname')
    email = data.get('email')
    salary = data.get('salary')
    if tid:
        cursor.execute('INSERT INTO teachers VALUES (%s,%s,%s,%s)',
                       (str(tid),str(tname),str(email),str(salary)))
        conn.commit()
        return jsonify({'message': 'Teachers added successfully'})
    else:
        return jsonify({'message': 'Invalid request'}), 400

@app.route('/teachers/updateteachers', methods=['POST'])
def update_teacher():

    conn = connect_to_database()
    cursor = conn.cursor()
    data = request.get_json()
    tid = data.get('tid')
    email = data.get('email')
    salary = data.get('salary')
    if tid:
        cursor.execute('UPDATE teachers SET email = %s WHERE tid = %s', (email, tid))
        cursor.execute('UPDATE teachers SET salary = %s WHERE tid = %s', (salary, tid))
        conn.commit()
        return jsonify({'message': 'teachers updated successfully'})
    else:
        return jsonify({'message': 'Invalid request'}), 400

@app.route('/teachers/deleteteachersById', methods=['GET'])
def deleteteachersById():
    tid = request.args.get('tid')  
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM teachers WHERE tid = %s', (tid,))
        conn.commit()  
        return jsonify({'message': 'Teacher deleted successfully'})
    except Exception as e:
        conn.rollback()  
        return jsonify({'message': r'Failed to delete teacher: {str(e)}'}), 500
    finally:
        cursor.close()
        conn.close()


@app.route('/courses', methods=['GET'])
def get_courses():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses')
    courses = cursor.fetchall()
    return jsonify({'courses': courses})


@app.route('/courses/getcoursesById', methods=['GET'])
def get_courseById():
    cid = request.args.get('cid')  
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses WHERE cid = %s', (cid,))
    course = cursor.fetchone()
    if course:
        return jsonify({'course': course})
    else:
        return jsonify({'message': 'Course not found'}), 404

@app.route('/addcourses', methods=['POST'])
def add_course():
    conn = connect_to_database()
    cursor = conn.cursor()
    data = request.get_json()
    cid = data.get('cid')
    cname = data.get('cname')
    hour = data.get('hour')
    if cid:
        cursor.execute('INSERT INTO courses VALUES (%s,%s,%s)',
                       (str(cid),str(cname),str(hour)))
        conn.commit()
        return jsonify({'message': 'Courses added successfully'})
    else:
        return jsonify({'message': 'Invalid request'}), 400

@app.route('/courses/updatecourses', methods=['POST'])
def update_course():

    conn = connect_to_database()
    cursor = conn.cursor()
    data = request.get_json()
    cid = data.get('cid')
    cname = data.get('cname')
    hour = data.get('hour')

    if cid:
        cursor.execute('UPDATE courses SET cname = %s WHERE cid = %s', (cname, cid))
        cursor.execute('UPDATE courses SET hour = %s WHERE cid = %s', (hour, cid))
        conn.commit()
        return jsonify({'message': 'courses updated successfully'})
    else:
        return jsonify({'message': 'Invalid request'}), 400

@app.route('/courses/deletecoursesById', methods=['GET'])
def deletecoursesById():
    cid = request.args.get('cid') 
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM courses WHERE cid = %s', (cid,))
        conn.commit() 
        return jsonify({'message': 'Course deleted successfully'})
    except Exception as e:
        conn.rollback()  
        return jsonify({'message': r'Failed to delete course: {str(e)}'}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/choices', methods=['GET'])
def get_choices():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM choices')
    choices = cursor.fetchall()
    return jsonify({'choices': choices})


@app.route('/choices/getchoicesById', methods=['GET'])
def get_choiceById():
    no = request.args.get('no')  
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM choices WHERE no = %s', (no,))
    choice = cursor.fetchone()
    if choice:
        return jsonify({'choice': choice})
    else:
        return jsonify({'message': 'Choice not found'}), 404

@app.route('/addchoices', methods=['POST'])
def add_choice():
    conn = connect_to_database()
    cursor = conn.cursor()
    data = request.get_json()
    no = data.get('no')
    sid = data.get('sid')
    tid = data.get('tid')
    cid = data.get('cid')
    score = data.get('score')

    if no:
        cursor.execute('INSERT INTO choices VALUES (%s,%s,%s,%s,%s)',
                       (str(no),str(sid),str(tid),str(cid),str(score)))
        conn.commit()
        return jsonify({'message': 'Choices added successfully'})
    else:
        return jsonify({'message': 'Invalid request'}), 400

@app.route('/choices/updatechoices', methods=['POST'])
def update_choice():

    conn = connect_to_database()
    cursor = conn.cursor()
    data = request.get_json()
    no = data.get('no')
    sid = data.get('sid')
    tid = data.get('tid')
    cid = data.get('cid')
    score = data.get('score')

    if no:
        cursor.execute('UPDATE choices SET sid = %s WHERE no = %s', (sid, no))
        cursor.execute('UPDATE choices SET tid = %s WHERE no = %s', (tid, no))
        cursor.execute('UPDATE choices SET cid = %s WHERE no = %s', (cid, no))
        cursor.execute('UPDATE choices SET score = %s WHERE no = %s', (score, no))
        conn.commit()
        return jsonify({'message': 'choices updated successfully'})
    else:
        return jsonify({'message': 'Invalid request'}), 400

@app.route('/choices/deletechoicesById', methods=['GET'])
def deletechoicesById():
    no = request.args.get('no')  
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM choices WHERE no = %s', (no,))
        conn.commit()  
        return jsonify({'message': 'Choice deleted successfully'})
    except Exception as e:
        conn.rollback() 
        return jsonify({'message': r'Failed to delete choice: {str(e)}'}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    
    app.run(debug=True,host='0.0.0.0', port=8080)
    