from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
import psycopg2
from logging.config import dictConfig
import logging
import sys
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Kết nối cơ sở dữ liệu
def get_db_connection():
    return psycopg2.connect(database="CNPM", user="postgres", password="anhkhoa191217", host="localhost", port="5432")

# Yêu cầu đăng nhập
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login_for_student'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/index')
@login_required
def index():
    username = session.get('username')
    logger.debug(f"Session username: {username}")  # Thêm dòng log này

    if not username:
        return redirect(url_for('login_for_student'))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name FROM "User" WHERE username = %s', (username,))
    user = cur.fetchone()
    logger.debug(f"User fetched: {user}")  # Thêm dòng log này
    cur.close()
    conn.close()

    if user:
        name = user[0]
        logger.debug(f"Name: {name}")  # Thêm dòng log này
        return render_template('index.html', name=name)
    else:
        return "User not found", 404


@app.route('/')
def login_for_student():
    return render_template('login_for_student.html') 

@app.route('/login_for_spso')
def login_for_spso():
    return render_template('login_for_spso.html') 

@app.route('/upload_file')
@login_required
def upload_file():
    return render_template('upload_file.html') 

@app.route('/buy_paper')
@login_required
def buy_paper():
    return render_template('buy_paper.html') 

@app.route('/printing_history')
@login_required
def printing_history():
    username = session.get('username')  # Lấy username từ session
    if not username:
        return redirect(url_for('login_for_student'))  # Nếu không có session, chuyển hướng đến trang login
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Lấy dữ liệu lịch sử in của người dùng
    logger.debug(f"Fetching printing history for username: {username}")
    cur.execute(
        'SELECT username, printer_id, file_type, file_name, file_size, no_pages, status, time '
        'FROM "Uses" WHERE username = %s',
        (username,)
    )
    printing_history = cur.fetchall()  # Lấy tất cả kết quả
    
    # Đếm số lượng record của user
    cur.execute(
        'SELECT COUNT(*) FROM "Uses" WHERE username = %s',
        (username,)
    )
    record_count = cur.fetchone()[0]  # Lấy số lượng bản ghi
    
    logger.debug(f"Printing history fetched: {printing_history}")
    logger.debug(f"Total records for {username}: {record_count}")
    cur.close()
    conn.close()
    
    # Truyền dữ liệu vào template
    return render_template('printing_history.html', history=printing_history, record_count=record_count)




@app.route('/system_error')
@login_required
def system_error():
    return render_template('system_error.html') 

@app.route('/homescreen_spso')
@login_required
def homescreen_spso():
    return render_template('homescreen_spso.html') 

@app.route('/spso_dashboard')
@login_required
def spso_dashboard():
    return render_template('spso_dashboard.html') 

@app.route('/student_dashboard')
@login_required
def student_dashboard():
    return render_template('student_dashboard.html') 

@app.route('/login_student', methods=['POST'])
def login_student():
    conn = get_db_connection()
    cur = conn.cursor()
    username = request.form['username']
    password = request.form['password']
    logger.debug(f"Login attempt: username={username}, password={password}")  # Log input

    cur.execute('SELECT * FROM "User" WHERE username = %s AND password = %s', (username, password))
    user = cur.fetchone()
    logger.debug(f"User found: {user}")  # Log result from database

    cur.close()
    conn.close()

    if user:
        session['username'] = username
        logger.debug(f"Session saved: {session['username']}")  # Log session
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login_for_student', wrongpw='false'))


@app.route('/login_spso', methods=['POST'])
def login_spso():
    conn = get_db_connection()
    cur = conn.cursor()
    username = request.form['username']
    password = request.form['password']

    cur.execute('SELECT * FROM "User" WHERE username = %s AND password = %s', (username, password))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        session['username'] = username
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login_for_spso', wrongpw='false'))

if __name__ == '__main__':
    print('xin chao')
    app.run(debug=True)
