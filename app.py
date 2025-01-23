from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load data from the JSON file
with open('q-vercel-python.json') as f:
    students = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students.get(name, None) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)

