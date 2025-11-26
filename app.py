from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Flask App!',
        'status': 'success',
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'flask-app'
    })

@app.route('/info')
def info():
    return jsonify({
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'deployed_by': 'GitHub Actions'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

