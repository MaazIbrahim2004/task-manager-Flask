from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy # class used to create instance of database
from datetime import datetime # used to get current date and time

app = Flask(__name__) # reference to app.py, so that flask knows where to look for templates and files
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
db = SQLAlchemy(app) # creating an instance of the database, passing in the app as a parameter
app.app_context().push() # creating an application context, so that we can use the db object


class Todo(db.Model): # class inheriting the base class for all models in SQLAlchemy
    id = db.Column(db.Integer, primary_key=True) # id column in the database. So that each item has a unique id
    content = db.Column(db.String(200), unique = True, nullable = False) # username column
    date_created = db.Column(db.DateTime, default = datetime.utcnow) # date created column

    # returns strings whenever we create a new element, by new element we mean a new todo item
    def __repr__(self): # how the object is printed whenever we print it out
        return '<Task %r>' % self.id 
    
# modifying the function below to run on the root path
@app.route('/', methods=['Post','Get']) # accepts post (send) and get (data) requests methods
def index(): # request is a parameter that contains all the data that the user sends to the server
    if request.method == 'POST':
        task_content = request.form['content'] # if the request method is post, get the content from the form
        new_task = Todo(content = task_content) # new task object to add to db
        try:
            db.session.add(new_task) # add new task to the database
            db.session.commit() # commit changes to the database
            return redirect('/') # redirect to the homepage
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks) 

@app.route('/delete/<int:id>') # route to delete a task
def delete(id):
    task_to_delete = Todo.query.get_or_404(id) # assign the task with the id passed in the url

    try:
        db.session.delete(task_to_delete) # delete the task
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'
    
@app.route('/update/<int:id>', methods=['GET', 'POST']) # route to update a task
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/') 
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task = task)

if __name__ == "__main__": # if the script of the app(app.py) is executed directly, run app
    app.run(debug=True, port = 8080)  
