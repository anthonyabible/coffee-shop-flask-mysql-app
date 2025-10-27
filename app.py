from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "devkey"

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3309
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'coffee123'  # or blank if your container allows it
app.config['MYSQL_DB'] = 'campuscoffee'

mysql = MySQL(app)


def query(sql, params=None, commit=False):
    conn = mysql.connection
    cur = conn.cursor(dictionary=True)
    cur.execute(sql, params or ())
    data = None
    if sql.strip().lower().startswith(("select", "show")):
        data = cur.fetchall()
    if commit:
        conn.commit()
    cur.close()
    return data

# -------- Your existing pages --------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

# -------- Sanity check: DB ping --------
@app.route('/db-ping')
def db_ping():
    rows = query("SELECT VERSION() AS ver")
    return f"MySQL OK — version: {rows[0]['ver']}"

# -------- Products: list/search --------
@app.route('/products')
def products_list():
    q = request.args.get("q", "").strip()
    if q:
        rows = query(
            "SELECT * FROM Product WHERE PName LIKE %s OR PCategory LIKE %s ORDER BY PName",
            (f"%{q}%", f"%{q}%")
        )
    else:
        rows = query("SELECT * FROM Product ORDER BY PName")
    return render_template("products/list.html", rows=rows, q=q)

# -------- Products: new --------
@app.route('/products/new', methods=['GET','POST'])
def products_new():
    if request.method == 'POST':
        name = request.form.get('name','').strip()
        desc = request.form.get('desc','').strip()
        price = request.form.get('price','0').strip()
        qty   = request.form.get('qty','0').strip()
        cat   = request.form.get('cat','').strip()
        if not name:
            flash("Name is required.","danger"); return redirect(url_for('products_new'))
        query("INSERT INTO Product (PName,PDescription,UnitPrice,Quantity,PCategory) VALUES (%s,%s,%s,%s,%s)",
              (name,desc,price,qty,cat), commit=True)
        flash("Product created.","success"); return redirect(url_for('products_list'))
    return render_template('products/form.html', mode='new', row=None)

# -------- Products: edit --------
@app.route('/products/<int:pid>/edit', methods=['GET','POST'])
def products_edit(pid):
    row = query("SELECT * FROM Product WHERE PID=%s", (pid,))
    if not row:
        flash("Product not found.","warning"); return redirect(url_for('products_list'))
    row = row[0]
    if request.method == 'POST':
        name = request.form.get('name','').strip()
        desc = request.form.get('desc','').strip()
        price = request.form.get('price','0').strip()
        qty   = request.form.get('qty','0').strip()
        cat   = request.form.get('cat','').strip()
        if not name:
            flash("Name is required.","danger"); return redirect(url_for('products_edit', pid=pid))
        query("""UPDATE Product SET PName=%s,PDescription=%s,UnitPrice=%s,Quantity=%s,PCategory=%s WHERE PID=%s""",
              (name,desc,price,qty,cat,pid), commit=True)
        flash("Product updated.","success"); return redirect(url_for('products_list'))
    return render_template('products/form.html', mode='edit', row=row)

# -------- Products: delete --------
@app.route('/products/<int:pid>/delete', methods=['POST'])
def products_delete(pid):
    query("DELETE FROM Product WHERE PID=%s", (pid,), commit=True)
    flash("Product deleted.","success"); return redirect(url_for('products_list'))

# -------- Chart JSON + page --------
@app.route('/charts/inventory')
def chart_inventory():
    data = query("SELECT PName, Quantity FROM Product ORDER BY PName")
    return jsonify({
        "type": "column2d",
        "dataSource": {
            "chart": {"caption":"Inventory Levels by Product","xAxisName":"Product","yAxisName":"Units","theme":"fusion"},
            "data": [{"label": r["PName"], "value": int(r["Quantity"])} for r in data]
        }
    })

@app.route('/analytics')
def analytics_page():
    return render_template('charts/inventory.html')

if __name__ == '__main__':
    app.run(debug=True)
