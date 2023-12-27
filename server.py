from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def authenticate_token(token):
    
    return token == 'your_secret_token'
    
@app.route('/<token>/upload', methods=['POST'])
def upload_files(token):
    if not authenticate_token(token):
        return jsonify({'error': 'Invalid token'}), 401

    uploaded_files = request.files.getlist('file')

    for file in uploaded_files:
        file.save(os.path.join('uploads', file.filename))

    return jsonify({'message': 'Files uploaded successfully', 'token': token}), 200

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    app.run(debug=True, host='0.0.0.0', port=5000)
