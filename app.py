from flask import Flask, render_template 
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysqldb'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.189.126.125'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/insert/<studentname>/<email>")
def insert(studentname, email):
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute("INSERT INTO students (studentName, email) values (%s, %s)",(studentname, email)) # execute an SQL statment
    mysql.connection.commit()
    return 'Insert finished' #Return the data in a string format

@app.route("/update/<id>/<studentname>/<email>")
def update(id, studentname, email):
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute("UPDATE students SET studentName=%s, email=%s WHERE studentID=%s",(studentname, email, id)) # execute an SQL$
    mysql.connection.commit()
    return 'Update finished' #Return the data in a string format

@app.route("/delete/<id>")
def delete(id):
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute("DELETE FROM students WHERE studentID=%s",(id)) # execute an SQ$
    mysql.connection.commit()
    return 'Delete finished' #Return the data in a string format

@app.route("/mytemplate")
def mytemplate():
    return render_template("mytemplate.html", name='Mr X', country='Germany')

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='80') #Run the flask app at port 5000

