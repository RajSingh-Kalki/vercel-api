from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data of 100 imaginary students
students = {
    "John": 10,
    "Jane": 20,
    "Alice": 30,
    "Bob": 40,
    # Add more students' marks as needed
}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students.get(name, None) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
