from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to establish database connection
def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route to retrieve data from database
@app.route('/get_data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Extracting parameters from request
    param = request.args.get('param')
    
    # Constructing SQL query (unsafe method)
    query = "SELECT * FROM table WHERE column = '" + param + "'"
    
    # Executing query
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    
    # Formatting data
    data = [dict(row) for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
