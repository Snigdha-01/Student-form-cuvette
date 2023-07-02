from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')  # Update the connection URL as per your MongoDB configuration
db = client['mydatabase']  # Replace 'mydatabase' with your database name
collection = db['students']  # Replace 'students' with your collection name


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email=request.form['email']
        college = request.form['college']
        branch = request.form['branch']
        student = {'name': name, 'college': college, 'branch': branch, 'email':email}
        collection.insert_one(student)

    # Fetch all the students from the MongoDB collection
    students = collection.find()

    return render_template('index.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
