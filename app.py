from flask import Flask, request , jsonify
from ia.detector import runIA
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    runIA("name")
    return "<p>Hello, World!</p>"

@app.route("/photo", methods=['POST'])
def photo():
    f = request.files["file"]
    f.save('/Users/fsznajderman/Documents/FLOXX/IA/floxx-ia/ourra22.jpeg')
    result = runIA("name")
    response = jsonify({'nbp': result})

    # Set the Access-Control-Allow-Origin header to allow requests from any domain
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response
    
    
if __name__ == '__main__':
    app.run(port=8080)