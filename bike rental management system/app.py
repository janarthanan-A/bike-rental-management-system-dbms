from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'sri'

# MySQL Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'  # Your MySQL password here
app.config['MYSQL_DB'] = 'db3'  # Your database name here
mysql = MySQL(app)

# Route to render the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to display available bikes
@app.route('/bikes')
def bikes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bikes")  # Query to fetch bike data
    bike_info = cur.fetchall()
    cur.close()
    return render_template('homepage.html', bikes=bike_info)  # Render bike info

# Route to search bikes by ID
@app.route('/search', methods=['POST', 'GET'])
def search():
    search_results = []
    search_term = ''
    if request.method == "POST":
        search_term = request.form['bike_id']
        cur = mysql.connection.cursor()
        query = "SELECT * FROM bikes WHERE bike_id LIKE %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results = cur.fetchmany(size=1)
        cur.close()
        return render_template('homepage.html', bikes=search_results)

# Route to insert a new bike
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        bike_id = request.form['bike_id']
        model = request.form['model']
        brand = request.form['brand']
        price_per_hour = request.form['price_per_hour']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO bikes (bike_id, model, brand, price_per_hour) VALUES (%s, %s, %s, %s)",
                    (bike_id, model, brand, price_per_hour))
        mysql.connection.commit()
        return redirect(url_for('bikes'))

# Route to delete a bike
@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM bikes WHERE bike_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('bikes'))

# Route to edit bike details (Display the Edit Form)
@app.route('/edit/<string:id_data>', methods=['GET'])
def edit(id_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bikes WHERE bike_id=%s", (id_data,))
    bike = cur.fetchone()  # Fetch the bike details to edit
    cur.close()
    return render_template('edit_bike.html', bike=bike)

# Route to handle the update of bike details
@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        bike_id = request.form['bike_id']
        model = request.form['model']
        brand = request.form['brand']
        price_per_hour = request.form['price_per_hour']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE bikes SET model=%s, brand=%s, price_per_hour=%s WHERE bike_id=%s",
                    (model, brand, price_per_hour, bike_id))
        mysql.connection.commit()
        return redirect(url_for('bikes'))  # Redirect back to the bike list page

if __name__ == "__main__":
    app.run(debug=True)
