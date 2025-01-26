from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Load marks data from q-vercel-python.json
with open('q-vercel-python.json') as f:
    students_data = json.load(f)
    students_marks = {student['name']: student['marks'] for student in students_data}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students_marks.get(name, 0) for name in names]
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run()
