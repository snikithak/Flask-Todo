from flask import Flask, render_template, request, redirect
from tinydb import TinyDB, Query
app=Flask(__name__)
db=TinyDB('db.json')

@app.route('/todo/', methods=['GET','POST'])
def hello():
    todo=request.form.get('todo')
    status=request.form.get('status')
    priority=request.form.get('priority')
    
    # if todo:
    #     db.insert({'todo': todo})
    #     if status:
    #         db.insert({'status': status})
    #         if priority:
    #             db.insert({'priority': priority})
    if todo and status and priority:
        db.insert({'todo': todo,'status':status,'priority':priority})
    todos=db.all()
    return render_template('index.html', todos=todos)

@app.route('/delete/<int:id>')
def delete(id):
    db.remove(doc_ids=[id])
    return redirect('/todo')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)