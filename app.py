from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import logging

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load marks data from q-vercel-python.json with error handling
try:
    with open('q-vercel-python.json') as f:
        students_data = json.load(f)
        students_marks = {student['name']: student['marks'] for student in students_data}
except Exception as e:
    students_data = []
    students_marks = {}
    app.logger.error(f"Error loading JSON file: {e}")

@app.route('/api', methods=['GET'])
def get_marks():
    try:
        names = request.args.getlist('name')
        marks = [students_marks.get(name, 0) for name in names]
        return jsonify({"marks": marks})
    except Exception as e:
        app.logger.error(f"Error in /api endpoint: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run()
