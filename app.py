import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('DATABASE')
if os.path.exists("env.py"):
    app.config["MONGO_URI"] = os.environ.get('MONGO_URI')    


mongo = PyMongo(app)

# Start of task routes

@app.route('/')
def view_tasks():
    return render_template("viewtasks.html", tasks=mongo.db.tasks.find())

@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

@app.route('/add_task')
def add_task():
    return render_template("addtask.html", projects=mongo.db.projects.find(), staff=mongo.db.staff.find())

@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks')) 

@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task =  mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_projects =  mongo.db.projects.find()
    all_staff =  mongo.db.staff.find()
    return render_template('edittask.html', task=the_task, 
                           projects=all_projects, staff=all_staff)

@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    tasks = mongo.db.tasks
    tasks.update( {'_id': ObjectId(task_id)},
    {
        'task_name':request.form.get('task_name'),
        'project_name':request.form.get('project_name'),
        'task_description': request.form.get('task_description'),
        'staff_name': request.form.get('staff_name'),
        'due_date': request.form.get('due_date'),
        'key':request.form.get('key'),
        'external':request.form.get('external'),        
        'billable':request.form.get('billable'),
        'completed':request.form.get('completed')
    })
    return redirect(url_for('get_tasks'))

@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('get_tasks'))

# Start of project routes



# Start of staff routes

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)