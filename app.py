from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load marks data from q-vercel-python.json
import json
with open('q-vercel-python.json') as f:
    students_marks = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students_marks.get(name, 0) for name in names]
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run()
