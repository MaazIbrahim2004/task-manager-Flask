from flask import Flask, render_template, url_for
# import Flask class from flask package, a class that used to create an instance of a web app
from flask_sqlalchemy import SQLAlchemy # class used to create instance of database
from datetime import datetime # used to get current date and time

app = Flask(__name__) # reference to app.py, so that flask knows where to look for templates and files
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
db = SQLAlchemy(app) # creating an instance of the database, passing in the app as a parameter
app.app_context().push() # creating an application context, so that we can use the db object


class Todo(db.Model): # class inheriting the base class for all models in SQLAlchemy
    id = db.Column(db.Integer, primary_key=True) # id column in the database
    content = db.Column(db.String(200), unique = True, nullable = False) # username column
    date_created = db.Column(db.DateTime, default = datetime.utcnow) # date created column

    # returns strings whenever we create a new element, by new element we mean a new todo item
    def __repr__(self): # how the object is printed whenever we print it out
        return '<Task %r>' % self.id
    

@app.route('/')  # modifying the function below to run on the root path
def index(): 
    return render_template('index.html') 

if __name__ == "__main__": # if the script of the app(app.py) is executed directly, run app
    app.run(debug=True, port = 8080)  
