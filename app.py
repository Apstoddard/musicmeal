from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello World'})

# post request to get the data from the frontend
@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    print(data)
    return jsonify({'message': 'Data received'})

if __name__ == '__main__':
    app.run(debug=True)