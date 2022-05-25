from flask import redirect, render_template, request
from app import app, get_db_connection, execute_db_action

@app.template_filter('not_doing')
def get_todos(todos):
    filtered = list(filter(lambda todo: todo[2] == False and todo[3] == False, todos))
    return filtered

@app.template_filter('doing')
def get_doing(todos):
    filtered = list(filter(lambda todo: todo[2] == True, todos))
    return filtered

@app.template_filter('done')
def get_done(todos):
    filtered = list(filter(lambda todo: todo[3] == True, todos))
    return filtered


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM items;')
    todos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('item')
    action = "INSERT INTO items (name) VALUES (%s);"
    execute_db_action(action, name)
    return redirect(request.referrer)

@app.route('/doing', methods = ['PUT', 'POST'])
def doing():
    id = request.form['doing_id']
    action = "UPDATE items SET doing = (%s) WHERE id = (%s);"
    execute_db_action(action, True, id)
    return redirect(request.referrer)   

@app.route('/done', methods = ['POST'])
def done():
    id = request.form['id']
    action = "UPDATE items SET doing = (%s), done = (%s) WHERE id = (%s);"
    execute_db_action(action, False, True, id)
    return redirect(request.referrer)


@app.route('/delete', methods = ['POST', 'DELETE'])
def delete():
    id = request.form.get('delete_id')
    action = "DELETE FROM items where id = (%s);"
    execute_db_action(action, id)
    return redirect(request.referrer)