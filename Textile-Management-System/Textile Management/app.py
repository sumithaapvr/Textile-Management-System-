import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

config = {
    'user': 'root',
    'password': 'sindhukumar@22',
    'host': 'localhost',
    'database': 'python',
    'raise_on_warnings': True
}


def get_db_connection():
    return mysql.connector.connect(**config)


@app.route('/user', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']

            # Connect to the database
            db = mysql.connector.connect(**config)
            cursor = db.cursor(dictionary=True)

            # Query to check if the user exists
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            cursor.close()
            db.close()

            if user:
                flash('Login successful!', 'success')
                return render_template('home.html')
            else:
                flash('Invalid username or password!', 'danger')
                return redirect(url_for('user_login'))
        except mysql.connector.Error as err:
            flash(f"Database error: {err}", 'danger')
            return redirect(url_for('user_login'))

    return render_template('login.html')

# Route for the dashboard (or any other page after login)
@app.route('/dashboard')
def dashboard():
    return "Welcome to the dashboard!"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/employee')
def employee():
    return render_template('employee.html')

@app.route('/wholesaler')
def wholesaler():
    return render_template('wholesaler.html')

@app.route('/product')
def product():
    return render_template('products.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/yarn')
def yarn():
    return render_template('yarn.html')

@app.route('/fabric')
def fabric():
    return render_template('fabric.html')

@app.route('/home2')
def home2():
    return render_template('home2.html')

@app.route('/dealer')
def dealer():
    return render_template('dealer.html')

@app.route('/view')
def view():
    return render_template('view.html')
@app.route('/user')
def user():
    return render_template('login.html')
@app.route('/view2')
def view2():
    return render_template('view2.html')
@app.route('/view3')
def view3():
    return render_template('view3.html')
@app.route('/view4')
def view4():
    return render_template('view4.html')
@app.route('/view5')
def view5():
    return render_template('view5.html')
@app.route('/login', methods=['POST'])
def login():
    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        name = request.form['name']
        roll = request.form['roll']
        experience = request.form['experience']
        phone = request.form['phone']
        salary = request.form['salary']
        date_of_join = request.form['date_of_join']

        sql = "INSERT INTO employees (name, roll, experience, phone, salary, date_of_join) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, roll, experience, phone, salary, date_of_join)

        cursor.execute(sql, val)
        db.commit()
        
        cursor.close()
        db.close()
        return "Data inserted successfully"
    except mysql.connector.Error as err:
        return f"Error inserting data: {err}"

@app.route('/submit', methods=['GET'])
def show_form():
    return render_template('dealer.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        dealer_name = request.form['dealer_name']
        location = request.form['location']
        ti_up = request.form['ti_up']
        phone_number = request.form['phone_number']

        sql = "INSERT INTO dealers (name, location, ti_up, phone_number) VALUES (%s, %s, %s, %s)"
        val = (dealer_name, location, ti_up, phone_number)

        cursor.execute(sql, val)
        db.commit()
        
        cursor.close()
        db.close()
        return redirect('/')
    except mysql.connector.Error as err:
        return f"Error inserting data: {err}"

@app.route('/yarn', methods=['GET'])
def show_yarn_form():
    return render_template('yarn.html')

@app.route('/yarn', methods=['POST'])
def submit_yarn_details():
    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        thread_count = request.form['threadCount']
        material = request.form['material']
        color = request.form['color']
        thickness = request.form['thickness']
        length = request.form['length']
        weight = request.form['weight']
        unit_price = request.form['unitPrice']
        total_production = request.form['totalProduction']
        available_stock = request.form['availableStock']
        date_of_manufacture = request.form['dateOfManufacture']

        sql = """
        INSERT INTO yarn_details (thread_count, material, color, thickness, length, weight, unit_price, total_production, available_stock, date_of_manufacture) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = (thread_count, material, color, thickness, length, weight, unit_price, total_production, available_stock, date_of_manufacture)

        cursor.execute(sql, val)
        db.commit()
        
        cursor.close()
        db.close()
        return "Data inserted successfully"
    except mysql.connector.Error as err:
        return f"Error inserting data: {err}"

@app.route('/fabric', methods=['GET', 'POST'])
def submit_fabric_details():
    if request.method == 'POST':
        try:
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            material = request.form['material']
            color = request.form['color']
            thickness = request.form['thickness']
            length = request.form['length']
            weight = request.form['weight']
            unit_price = request.form['unitPrice']
            total_production = request.form['totalProduction']
            available_stock = request.form['availableStock']
            date_of_manufacture = request.form['dateOfManufacture']

            sql = """
            INSERT INTO fabric_details (material, color, thickness, length, weight, unit_price, total_production, available_stock, date_of_manufacture) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            val = (material, color, thickness, length, weight, unit_price, total_production, available_stock, date_of_manufacture)

            cursor.execute(sql, val)
            db.commit()
            
            cursor.close()
            db.close()
            return "Data inserted successfully"
        except mysql.connector.Error as err:
            return f"Error inserting data: {err}"

    return render_template('fabric.html')

@app.route('/home', methods=['GET'])
def show_home_form():
    return render_template('home2.html')

@app.route('/home', methods=['POST'])
def submit_home_textile_details():
    if request.method == 'POST':
        try:
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            productId = request.form['productId']
            productName = request.form['productName']
            category = request.form['category']
            material = request.form['material']
            size = request.form['size']
            color = request.form['color']
            design = request.form['design']
            price = request.form['price']
            stockQuantity = request.form['stockQuantity']

            sql = "INSERT INTO products (productId, productName, category, material, size, color, design, price, stockQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (productId, productName, category, material, size, color, design, price, stockQuantity)

            cursor.execute(sql, val)
            db.commit()
            
            cursor.close()
            db.close()
            return redirect('/')
        except mysql.connector.Error as err:
            return f"Error inserting data: {err}"
    else:
        return redirect('/')


@app.route('/employees')
def employees():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        cursor.close()
        db.close()
        return render_template('view.html', employees=employees)
    except mysql.connector.Error as err:
        return f"Error retrieving data: {err}"
    
@app.route('/employees/<int:employee_id>/update', methods=['GET'])
def get_employee_for_update(employee_id):
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
        employee = cur.fetchone()
        cur.close()
        db.close()
        return render_template('update_employee.html', employee=employee)
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error retrieving employee: {err}"}), 500

@app.route('/employees/<int:employee_id>/update', methods=['POST'])
def update_employee(employee_id):
    try:
        db = get_db_connection()
        cur = db.cursor()
        data = request.form
        sql = "UPDATE employees SET name=%s, roll=%s, experience=%s, phone=%s, salary=%s, date_of_join=%s WHERE id=%s"
        values = (data['name'], data['roll'], data['experience'], data['phone'], data['salary'], data['date_of_join'], employee_id)
        cur.execute(sql, values)
        db.commit()
        cur.close()
        db.close()
        return jsonify({"message": "Employee updated"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error updating employee: {err}"}), 500

@app.route('/employees/<int:employee_id>/delete', methods=['DELETE'])
def delete_employee(employee_id):
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("DELETE FROM employees WHERE id=%s", (employee_id,))
        db.commit()
        cur.close()
        db.close()
        return jsonify({"message": "Employee deleted"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error deleting employee: {err}"}), 500
    
@app.route('/dealers')
def dealers():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM dealers")
        dealers = cursor.fetchall()
        cursor.close()
        db.close()
        return render_template('view2.html', dealers=dealers)
    except mysql.connector.Error as err:
        return f"Error retrieving data: {err}", 500

@app.route('/dealers/<int:dealer_id>/update', methods=['GET'])
def get_dealer_for_update(dealer_id):
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM dealers WHERE id = %s", (dealer_id,))
        dealer = cur.fetchone()
        cur.close()
        db.close()
        return render_template('update_dealer.html', dealer=dealer)
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error retrieving dealer: {err}"}), 500

@app.route('/dealers/<int:dealer_id>/update', methods=['POST'])
def update_dealer(dealer_id):
    try:
        db = get_db_connection()
        cur = db.cursor()
        data = request.form
        sql = "UPDATE dealers SET name=%s, location=%s, ti_up=%s, phone=%s WHERE id=%s"
        values = (data['name'], data['location'], data['ti_up'], data['phone'], dealer_id)
        cur.execute(sql, values)
        db.commit()
        cur.close()
        db.close()
        return jsonify({"message": "Dealer updated"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error updating dealer: {err}"}), 500

@app.route('/dealers/<int:dealer_id>/delete', methods=['DELETE'])
def delete_dealer(dealer_id):
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("DELETE FROM dealers WHERE id=%s", (dealer_id,))
        db.commit()
        cur.close()
        db.close()
        return jsonify({"message": "Dealer deleted"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error deleting dealer: {err}"}), 500
    
@app.route('/yarn_details')
def yarn_details():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM yarn_details")
        yarn_details = cursor.fetchall()
        cursor.close()
        db.close()
        return render_template('view3.html', yarn_details=yarn_details)
    except mysql.connector.Error as err:
        return f"Error retrieving yarn details: {err}", 500

@app.route('/yarn_details/<int:yarn_id>/update', methods=['GET'])
def get_yarn_for_update(yarn_id):
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM yarn_details WHERE id = %s", (yarn_id,))
        yarn = cur.fetchone()
        cur.close()
        db.close()
        if yarn:
            return render_template('update_yarn.html', yarn=yarn)
        else:
            return "Yarn not found", 404
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error retrieving yarn: {err}"}), 500

@app.route('/yarn_details/<int:yarn_id>/update', methods=['POST'])
def update_yarn(yarn_id):
    try:
        db = get_db_connection()
        cur = db.cursor()
        data = request.form
        sql = "UPDATE yarn_details SET thread_count=%s, material=%s, color=%s, thickness=%s, length=%s, weight=%s, unit_price=%s, total_production=%s, available_stock=%s, date_of_manufacture=%s WHERE id=%s"
        values = (data['thread_count'], data['material'], data['color'], data['thickness'], data['length'], data['weight'], data['unit_price'], data['total_production'], data['available_stock'], data['date_of_manufacture'], yarn_id)
        cur.execute(sql, values)
        db.commit()
        cur.close()
        db.close()
        return jsonify({"message": "Yarn updated"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error updating yarn: {err}"}), 500

@app.route('/yarn_details/<int:yarn_id>/delete', methods=['DELETE'])
def delete_yarn(yarn_id):
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("DELETE FROM yarn_details WHERE id=%s", (yarn_id,))
        db.commit()
        cur.close()
        db.close()
        return jsonify({"message": "Yarn deleted"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error deleting yarn: {err}"}), 500
@app.route('/fabric_details')
def fabric_details():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM fabric_details")
        fabric_details = cursor.fetchall()
        cursor.close()
        db.close()
        return render_template('view4.html', fabric_details=fabric_details)
    except mysql.connector.Error as err:
        return f"Error retrieving fabric details: {err}", 500

@app.route('/fabric_details/<int:fabric_id>/update', methods=['GET'])
def get_fabric_for_update(fabric_id):
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM fabric_details WHERE id = %s", (fabric_id,))
        fabric = cur.fetchone()
        cur.close()
        db.close()
        return render_template('update_fabric.html', fabric=fabric)
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error retrieving fabric: {err}"}), 500

@app.route('/fabric_details/<int:fabric_id>/update', methods=['POST'])
def update_fabric(fabric_id):
    try:
        db = get_db_connection()
        cur = db.cursor()
        data = request.form
        sql = "UPDATE fabric_details SET  material=%s, color=%s, thickness=%s, length=%s, weight=%s, unit_price=%s, total_production=%s, available_stock=%s, date_of_manufacture=%s WHERE id=%s"
        values = ( data['material'], data['color'], data['thickness'], data['length'], data['weight'], data['unit_price'], data['total_production'], data['available_stock'], data['date_of_manufacture'], fabric_id)
        cur.execute(sql, values)
        db.commit()
        cur.close()
        db.close()
        return jsonify({"message": "Fabric updated"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error updating fabric: {err}"}), 500

@app.route('/fabric_details/<int:fabric_id>/delete', methods=['DELETE'])
def delete_fabric(fabric_id):
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("DELETE FROM fabric_details WHERE id=%s", (fabric_id,))
        db.commit()
        cur.close()
        db.close()
        return jsonify({"message": "Fabric deleted"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error deleting fabric: {err}"}), 500
    
@app.route('/products')
def products():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        cursor.close()
        db.close()
        return render_template('view5.html', products=products)
    except mysql.connector.Error as err:
        return f"Error retrieving product details: {err}", 500

@app.route('/products/<int:product_id>/update', methods=['GET'])
def get_product_for_update(product_id):
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM products WHERE productId = %s", (product_id,))
        product = cur.fetchone()
        cur.close()
        db.close()
        return render_template('update_home.html', product=product)
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error retrieving product: {err}"}), 500

@app.route('/products/<int:product_id>/update', methods=['POST'])
def update_product(product_id):
    try:
        db = get_db_connection()
        cur = db.cursor()
        data = request.form
        sql = "UPDATE products SET productName=%s, category=%s, material=%s, size=%s, color=%s, design=%s, price=%s, stockQuantity=%s WHERE productId=%s"
        values = (data['productName'], data['category'], data['material'], data['size'], data['color'], data['design'], data['price'], data['stockQuantity'], product_id)
        cur.execute(sql, values)
        db.commit()
        cur.close()
        db.close()
        return jsonify({"message": "Product updated"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error updating product: {err}"}), 500

@app.route('/products/<int:product_id>/delete', methods=['DELETE'])
def delete_product(product_id):
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("DELETE FROM products WHERE productId=%s", (product_id,))
        db.commit()
        cur.close()
        db.close()
        return jsonify({"message": "Product deleted"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Error deleting product: {err}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
