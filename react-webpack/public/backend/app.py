from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from functools import wraps
import psycopg2
from logging.config import dictConfig
import logging
import sys
import base64
from io import BytesIO
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
    cur.execute('SELECT name, profile_picture FROM "User" WHERE username = %s', (username,))
    user = cur.fetchone()
    logger.debug(f"User fetched: {user}")  # Thêm dòng log này

     # Lấy thông báo của người dùng
    cur.execute('SELECT content, time FROM "Notification" WHERE username = %s ORDER BY time DESC', (username,))
    notifications = cur.fetchall()  # Lấy tất cả thông báo của người dùng

    cur.close()
    conn.close()

    if user:
        name = user[0]
        profile_picture2 = user[1]
        logger.debug(f"Name: {name}")  # Thêm dòng log này
        logger.debug(f"Fetched profile picture for {username}: {name}")  # Log ảnh đại diện đã được lấy
        if profile_picture2:
            profile_picture2_base64 = base64.b64encode(profile_picture2).decode('utf-8')  # Chuyển sang chuỗi base64
        else:
            profile_picture2_base64 = None
        return render_template('index.html', name=name, profile_picture2_base64=profile_picture2_base64,notifications=notifications)
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
    username = session.get('username')  # Lấy username từ session
    if not username:
        return redirect(url_for('login_for_student'))  # Nếu không có session, chuyển hướng đến trang login
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Truy vấn tên người dùng từ bảng "User"
    cur.execute('SELECT name, profile_picture FROM "User" WHERE username = %s', (username,))
    user = cur.fetchone()
     # Lấy thông báo của người dùng
    cur.execute('SELECT content, time FROM "Notification" WHERE username = %s ORDER BY time DESC', (username,))
    notifications = cur.fetchall()  # Lấy tất cả thông báo của người dùng
    if user:
        name = user[0]  # Lấy tên từ kết quả truy vấn
        profile_picture3 = user[1] 
        logger.debug(f"Fetched name for user {username}: {name}")
        logger.debug(f"Fetched profile picture for {username}: {name}")  # Log ảnh đại diện đã được lấy
        if profile_picture3:
            profile_picture3_base64 = base64.b64encode(profile_picture3).decode('utf-8')  # Chuyển sang chuỗi base64
        else:
            profile_picture3_base64 = None
    else:
        cur.close()
        conn.close()
        return "User not found", 404

    cur.close()
    conn.close()
    
    # Truyền dữ liệu vào template
    return render_template('upload_file.html', name=name, profile_picture3_base64=profile_picture3_base64,notifications=notifications)
 

@app.route('/buy_paper')
@login_required
def buy_paper():
    transactions = get_transactions()
    no_papers = get_paper_number()
    username = session.get('username')  # Lấy username từ session
    if not username:
        return redirect(url_for('login_for_student'))  # Nếu không có session, chuyển hướng đến trang login
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Truy vấn tên người dùng từ bảng "User"
    cur.execute('SELECT name, profile_picture FROM "User" WHERE username = %s', (username,))
    user = cur.fetchone()
     # Lấy thông báo của người dùng
    cur.execute('SELECT content, time FROM "Notification" WHERE username = %s ORDER BY time DESC', (username,))
    notifications = cur.fetchall()  # Lấy tất cả thông báo của người dùng
    if user:
        name = user[0]  # Lấy tên từ kết quả truy vấn
        profile_picture4 = user[1]
        logger.debug(f"Fetched name for user {username}: {name}")
        logger.debug(f"Fetched profile picture for {username}: {name}")  # Log ảnh đại diện đã được lấy
        if profile_picture4:
            profile_picture4_base64 = base64.b64encode(profile_picture4).decode('utf-8')  # Chuyển sang chuỗi base64
        else:
            profile_picture4_base64 = None
    else:
        cur.close()
        conn.close()
        return "User not found", 404

    cur.close()
    conn.close()
    
    # Truyền dữ liệu vào template
    return render_template('buy_paper.html', 
                           name=name, 
                           profile_picture4_base64=profile_picture4_base64,
                           notifications=notifications, 
                           transactions=transactions, 
                           no_papers=no_papers) 

def get_transactions():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        username = session.get('username')
        
        cursor.execute(f'''SELECT * FROM "Transaction" WHERE "student_username" = '{username}' ORDER BY "trans_id" DESC''')
        transactions = cursor.fetchall()
        cursor.close()
        connection.close()

        return transactions
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_paper_number():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        username = session.get('username')
        
        cursor.execute(f'''SELECT "account_balance" FROM "Student" WHERE "username" = '{username}' ''')
        no_papers = cursor.fetchall()
        print(no_papers)
        cursor.close()
        connection.close()

        return no_papers
    except Exception as e:
        print(f"Error: {e}")
        return []

@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    try:
        # Get JSON data from the request
        data = request.json
        # balance = data.get('account_balance')
        no_paper = data.get('paper_number')

        if no_paper is None:
            return jsonify({'error': 'Invalid input data'}), 400

        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor()
        username = session.get('username')

        # Secure parameterized SQL query
        # cursor.execute(f'''UPDATE "Student" SET "account_balance" = '{balance}' WHERE "username" = '{user_name}' ''')
        cursor.execute(f'''INSERT INTO "Transaction" (price, no_pages, status, student_username) 
                           VALUES ({no_paper*1000}, {no_paper}, 'Đang chờ thanh toán', '{username}')
                           RETURNING trans_id;''')
        # Commit changes
        trans_id = cursor.fetchone()[0]
        connection.commit()
        # Check if any rows were updated
        if cursor.rowcount > 0:
            return jsonify({'message': 'Account balance updated successfully', 'trans_id': trans_id}), 200
        else:
            return jsonify({'error': 'No user found with the given username'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Clean up resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.route('/update_balance', methods=['POST'])
def update_balance():
    try:
        # Get JSON data from the request
        data = request.json
        balance = data.get('account_balance')
        trans_id = data.get('trans_id')
        username = session.get('username')
        if balance is None or trans_id is None:
            return jsonify({'error': 'Invalid input data'}), 400

        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor()

        # Secure parameterized SQL query
        cursor.execute(f'''UPDATE "Student" SET "account_balance" = '{balance}' WHERE "username" = '{username}' ''')
        cursor.execute(f'''UPDATE "Transaction" SET "status" = 'Đã thanh toán' WHERE "trans_id" = {trans_id};''')
        
        # Commit changes
        connection.commit()

        # Check if any rows were updated
        if cursor.rowcount > 0:
            return jsonify({'message': 'Account balance updated successfully'}), 200
        else:
            return jsonify({'error': 'No user found with the given username'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Clean up resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.route('/update_error', methods=['POST'])
def update_error():
    try:
        # Get JSON data from the request
        data = request.json
        trans_id = data.get('trans_id')
        if trans_id is None:
            return jsonify({'error': 'Invalid input data'}), 400

        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor()

        # Secure parameterized SQL query
        cursor.execute(f'''UPDATE "Transaction" SET "status" = 'Lỗi thanh toán' WHERE "trans_id" = {trans_id};''')
        
        # Commit changes
        connection.commit()

        # Check if any rows were updated
        if cursor.rowcount > 0:
            return jsonify({'message': 'Account balance updated successfully'}), 200
        else:
            return jsonify({'error': 'No user found with the given username'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Clean up resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# @app.route('/get_transactions', methods=['GET'])
# def get_trans():
#     try:
#         connection = psycopg2.connect(**DB_CONFIG)
#         cursor = connection.cursor()
#         username = session.get('username')

#         # Fetch updated data
#         cursor.execute(f'''SELECT * FROM "Transaction" WHERE "student_username" = '{user_name}' ORDER BY "trans_id" DESC''')
#         transactions = cursor.fetchall()

#         # Convert data to JSON-friendly format
#         transactions_data = [{'tran_id': col[0], 'date': col[5], 'no_pages': col[2], 'price': col[1], 'status': col[3]} for col in transactions]

#         return jsonify(transactions_data)

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()



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
        'SELECT username, printer_id, file_type, file_name, file_size, no_pages, status, time, paper_orientation, print_sides, num_copies '
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
    
    # Truy vấn tên người dùng từ bảng "User"
    cur.execute('SELECT name, profile_picture FROM "User" WHERE username = %s', (username,))
    user = cur.fetchone()
     # Lấy thông báo của người dùng
    cur.execute('SELECT content, time FROM "Notification" WHERE username = %s ORDER BY time DESC', (username,))
    notifications = cur.fetchall()  # Lấy tất cả thông báo của người dùng
    if user:
        name = user[0]  # Lấy tên từ kết quả truy vấn
        profile_picture = user[1]  # Lấy ảnh từ cơ sở dữ liệu (dạng bytea)
        logger.debug(f"Fetched name for user {username}: {name}")
        # Chuyển đổi ảnh nhị phân (bytea) thành base64
        if profile_picture:
            profile_picture_base64 = base64.b64encode(profile_picture).decode('utf-8')  # Chuyển sang chuỗi base64
        else:
            profile_picture_base64 = None
    else:
        cur.close()
        conn.close()
        return "User not found", 404
    
    cur.close()
    conn.close()
    # Truyền dữ liệu vào template
    return render_template('printing_history.html', history=printing_history, record_count=record_count, name=name, profile_picture_base64=profile_picture_base64,notifications=notifications)
    
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

@app.route('/spso_printing_history')
@login_required
def spso_printing_history():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Truy vấn dữ liệu từ bảng spso_printinghistory
    logger.debug("Fetching SPSO printing history")
    cur.execute('SELECT name, printer_id, file_name, file_size, no_pages, status, time, paper_orientation, print_sides, num_copies, file_type, user_id FROM spso_printinghistory')
    spso_history = cur.fetchall()  # Lấy tất cả kết quả
    
    logger.debug(f"SPSO printing history fetched: {spso_history}")
    
    cur.close()
    conn.close()
    
    # Truyền dữ liệu vào template
    return render_template('spso_printing_history.html', spso_history=spso_history)


@app.route('/student_dashboard')
@login_required
def student_dashboard():
    username = session.get('username')  # Lấy username từ session
    if not username:
        return redirect(url_for('login_for_student'))  # Nếu không có session, chuyển hướng đến trang login
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Truy vấn tên người dùng từ cơ sở dữ liệu
    cur.execute('SELECT name, profile_picture FROM "User" WHERE username = %s', (username,))
    user = cur.fetchone()
     # Lấy thông báo của người dùng
    cur.execute('SELECT content, time FROM "Notification" WHERE username = %s ORDER BY time DESC', (username,))
    notifications = cur.fetchall()  # Lấy tất cả thông báo của người dùng
    
    if user:
        name = user[0]  # Lấy tên từ kết quả truy vấn
        profile_picture1 = user[1]  # Lấy ảnh từ cơ sở dữ liệu (dạng bytea)
        logger.debug(f"Fetched profile picture for {username}: {name}")  # Log ảnh đại diện đã được lấy
        if profile_picture1:
            profile_picture1_base64 = base64.b64encode(profile_picture1).decode('utf-8')  # Chuyển sang chuỗi base64
        else:
            profile_picture1_base64 = None
    else:
        cur.close()
        conn.close()
        return "User not found", 404
    
    cur.close()
    conn.close()
    
    return render_template('student_dashboard.html', name=name, profile_picture1_base64=profile_picture1_base64, notifications=notifications)



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
        return redirect(url_for('index'), )
    else:
        return redirect(url_for('login_for_student', wrongpw='true'))

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
        return redirect(url_for('homescreen_spso'))
    else:
        return redirect(url_for('login_for_spso', wrongpw='false'))

if __name__ == '__main__':
    app.run(debug=True)
