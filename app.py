from flask import Flask, render_template, request, redirect, url_for, send_file
import sqlite3
import pandas as pd

app = Flask(__name__)

# Configuração do Banco de Dados
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Rota para adicionar cliente
@app.route('/add', methods=['POST'])
def add_client():
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (name, address, phone, email) VALUES (?, ?, ?, ?)", (name, address, phone, email))
    conn.commit()
    conn.close()

    return redirect(url_for('view_clients'))

# Rota para visualizar clientes
@app.route('/view')
def view_clients():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    conn.close()

    return render_template('view_clients.html', clients=clients)

# Rota para consultar clientes
@app.route('/search', methods=['GET'])
def search_client():
    name = request.args.get('name')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE name LIKE ?", ('%' + name + '%',))
    clients = cursor.fetchall()
    conn.close()

    return render_template('view_clients.html', clients=clients)

# Rota para exportar clientes para Excel
@app.route('/export', methods=['POST'])
def export_clients():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM clients", conn)
    df.to_excel('clientes.xlsx', index=False)
    conn.close()

    return send_file('clientes.xlsx', as_attachment=True)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)