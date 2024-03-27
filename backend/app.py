from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongo:27017/')
db = client['mydatabase']
collection = db['inputs']

@app.route('/')
def index():
    return 'Welcome to the Input Form!'

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    if name and email:
        collection.insert_one({'name': name, 'email': email})
        return jsonify({'message': 'Data inserted successfully!'})
    else:
        return jsonify({'message': 'Name and email are required!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
