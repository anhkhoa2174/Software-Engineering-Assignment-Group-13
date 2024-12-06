from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2 

app = Flask(__name__) 
DB_CONFIG = {
    "dbname": "CNPM",
    "user": "postgres",
    "password": "123456",
    "host": "localhost",
    "port": 5432,
}
# Khởi tạo cơ sở dữ liệu và bảng
conn = psycopg2.connect(**DB_CONFIG) 
  
cur = conn.cursor() 

# cur.execute('''
#     CREATE TABLE IF NOT EXISTS products (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100),
#         price FLOAT
#     );
# ''') 

conn.commit() 
cur.close() 
conn.close()

user_name = "tien_dat"

# Route hiển thị danh sách sản phẩm
# @app.route('/') 
# def index(): 
#     conn = psycopg2.connect(database="CNPM", 
#                             user="postgres", 
#                             password="123456", 
#                             host="localhost", port="5432") 
#     cur = conn.cursor() 
#     cur.execute('SELECT * FROM products') 
#     data = cur.fetchall() 
#     cur.close() 
#     conn.close() 
#     return render_template('index.html', data=data) 



# Tạo route link đến các file html
@app.route('/index')
def index():
    # conn = psycopg2.connect(database="CNPM", 
    #                         user="postgres", 
    #                         password="123456", 
    #                         host="localhost", port="5432") 
    # cur = conn.cursor() 
    # data = cur.fetchall() 
    # cur.close() 
    # conn.close() 
    return render_template('index.html') 

@app.route('/')
def login_for_student():
    return render_template('login_for_student.html') 

@app.route('/login_for_spso')
def login_for_spso():
    return render_template('login_for_spso.html') 

@app.route('/upload_file')
def upload_file():
    return render_template('upload_file.html') 

@app.route('/buy_paper')
def buy_paper():
    transactions = get_transactions()
    no_papers = get_paper_number()
    return render_template('buy_paper.html', transactions=transactions, no_papers=no_papers) 

def get_transactions():
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        cursor.execute(f'''SELECT * FROM "Transaction" WHERE "student_username" = '{user_name}' ORDER BY "trans_id" DESC''')
        transactions = cursor.fetchall()
        cursor.close()
        connection.close()

        return transactions
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_paper_number():
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute(f'''SELECT "account_balance" FROM "Student" WHERE "username" = '{user_name}' ''')
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
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Secure parameterized SQL query
        # cursor.execute(f'''UPDATE "Student" SET "account_balance" = '{balance}' WHERE "username" = '{user_name}' ''')
        cursor.execute(f'''INSERT INTO "Transaction" (price, no_pages, status, student_username) 
                           VALUES ({no_paper*1000}, {no_paper}, 'Đang chờ thanh toán', '{user_name}')
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
        if balance is None or trans_id is None:
            return jsonify({'error': 'Invalid input data'}), 400

        # Connect to the database
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Secure parameterized SQL query
        cursor.execute(f'''UPDATE "Student" SET "account_balance" = '{balance}' WHERE "username" = '{user_name}' ''')
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
        connection = psycopg2.connect(**DB_CONFIG)
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
def printing_history():
    return render_template('printing_history.html') 

@app.route('/system_error')
def system_error():
    return render_template('system_error.html') 

@app.route('/homescreen_spso')
def homescreen_spso():
    return render_template('homescreen_spso.html') 

@app.route('/spso_dashboard')
def spso_dashboard():
    return render_template('spso_dashboard.html') 

@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html') 

  
# Route thêm sản phẩm
# @app.route('/create', methods=['POST']) 
# def create(): 
#     conn = psycopg2.connect(database="CNPM", 
#                             user="postgres", 
#                             password="123456", 
#                             host="localhost", port="5432") 
#     cur = conn.cursor() 
#     name = request.form['name'] 
#     price = request.form['price'] 
#     cur.execute(
#         'INSERT INTO products (name, price) VALUES (%s, %s)', 
#         (name, price))
#     conn.commit() 
#     cur.close() 
#     conn.close() 
#     return redirect(url_for('index')) 
  
# Route cập nhật sản phẩm
# @app.route('/update', methods=['POST']) 
# def update(): 
#     conn = psycopg2.connect(database="CNPM", 
#                             user="postgres", 
#                             password="123456", 
#                             host="localhost", port="5432") 
#     cur = conn.cursor() 
#     name = request.form['name'] 
#     price = request.form['price'] 
#     id = request.form['id'] 
#     cur.execute(
#         'UPDATE products SET name=%s, price=%s WHERE id=%s', 
#         (name, price, id))
#     conn.commit() 
#     cur.close() 
#     conn.close() 
#     return redirect(url_for('index')) 
  
# Route xóa sản phẩm
# @app.route('/delete', methods=['POST']) 
# def delete(): 
#     conn = psycopg2.connect(database="CNPM", 
#                             user="postgres", 
#                             password="123456", 
#                             host="localhost", port="5432") 
#     cur = conn.cursor() 
#     id = request.form['id'] 
#     cur.execute('DELETE FROM products WHERE id=%s', (id,)) 
#     conn.commit() 
#     cur.close() 
#     conn.close() 
#     return redirect(url_for('index')) 

# Login cho student
@app.route('/login_student', methods=['POST'])
def login_student():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Lấy thông tin từ form
    username = request.form['username']
    password = request.form['password']

    # Kiểm tra thông tin trong bảng User
    cur.execute('SELECT * FROM "User" WHERE username = %s AND password = %s', (username, password))
    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        global user_name 
        user_name = username
        # Nếu thông tin hợp lệ
        return redirect(url_for('index'))
    else:
        # Nếu thông tin không hợp lệ
        return redirect(url_for('login_for_student', wrongpw='false'))
    
# Login cho spso
@app.route('/login_student', methods=['POST'])
def login_spso():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Lấy thông tin từ form
    username = request.form['username']
    password = request.form['password']

    # Kiểm tra thông tin trong bảng User
    cur.execute('SELECT * FROM "User" WHERE username = %s AND password = %s', (username, password))
    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        # Nếu thông tin hợp lệ
        return redirect(url_for('index'))
    else:
        # Nếu thông tin không hợp lệ
        return redirect(url_for('login_for_spso', wrongpw='false'))
     
if __name__ == '__main__':
    app.run(debug=True)
