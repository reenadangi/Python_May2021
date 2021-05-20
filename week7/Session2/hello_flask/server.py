from flask import Flask,render_template 
from mysqlconnection import connectToMySQL

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    mysql = connectToMySQL('mydb')
    friends=mysql.query_db("select * from friends;")
    return render_template('friends.html',friend_list=friends)

@app.route('/<name>')
def hello_user(name):
    # return f"Hello welcome to Flask {name}"
    return render_template('index.html',name=name)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
