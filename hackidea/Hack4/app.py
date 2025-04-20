from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.debug_code import run_user_code

app = Flask(__name__)
CORS(app)

@app.route('/api/fetch', methods=['POST'])
def debug():
    data = request.get_json()
    code = data.get('code')
   

    if not code or not isinstance(code, str):
        return jsonify({"error": "Invalid code provided"}), 400

    try:
       
        output = run_user_code(code)  
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)