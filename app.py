from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load data from the JSON file
with open('q-vercel-python.json') as f:
    student_data = json.load(f)

# Create a dictionary with names as keys and marks as values
students = {student["name"]: student["marks"] for student in student_data}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students.get(name, None) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
