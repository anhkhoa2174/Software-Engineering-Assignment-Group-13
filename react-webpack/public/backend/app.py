from flask import Flask, render_template, request, redirect, url_for 
import psycopg2 

app = Flask(__name__) 

# Khởi tạo cơ sở dữ liệu và bảng
conn = psycopg2.connect(database="CNPM",  user="postgres", password="anhkhoa191217",  host="localhost", port="5432") 
  
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


# Route hiển thị danh sách sản phẩm
# @app.route('/') 
# def index(): 
#     conn = psycopg2.connect(database="CNPM", 
#                             user="postgres", 
#                             password="anhkhoa191217", 
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
    #                         password="anhkhoa191217", 
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
    return render_template('buy_paper.html') 


  
# Route thêm sản phẩm
# @app.route('/create', methods=['POST']) 
# def create(): 
#     conn = psycopg2.connect(database="CNPM", 
#                             user="postgres", 
#                             password="anhkhoa191217", 
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
#                             password="anhkhoa191217", 
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
#                             password="anhkhoa191217", 
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
    conn = psycopg2.connect(database="CNPM",
                            user="postgres",
                            password="anhkhoa191217",
                            host="localhost",
                            port="5432")
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
        return redirect(url_for('login_for_student', wrongpw='false'))
    
# Login cho spso
@app.route('/login_student', methods=['POST'])
def login_spso():
    conn = psycopg2.connect(database="CNPM",
                            user="postgres",
                            password="anhkhoa191217",
                            host="localhost",
                            port="5432")
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
