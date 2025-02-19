from flask import Flask, render_template, request, send_file, flash, redirect, jsonify
from io import BytesIO
from encrypt import encrypt_message
import numpy as np
from PIL import Image
from decrypt import decrypt_message

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        try:
            # Basic file check
            if 'image' not in request.files:
                flash('No file uploaded', 'error')
                return redirect(request.url)
            
            file = request.files['image']
            if file.filename == '':
                flash('No file selected', 'error')
                return redirect(request.url)
            
            # Get form data
            message = request.form.get('message', '').strip()
            password = request.form.get('password', '').strip()
            
            if not message or not password:
                flash('Please fill all fields', 'error')
                return redirect(request.url)

            try:
                # Read image directly from request
                img = Image.open(file)
                # Convert to RGB if necessary
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
            except Exception as e:
                flash('Invalid image file', 'error')
                return redirect(request.url)
            
            # Create BytesIO object for output
            output = BytesIO()
            
            # Encrypt the message
            encrypt_message(img, message, password, output)
            
            # Prepare the file for sending
            output.seek(0)
            
            return send_file(
                output,
                as_attachment=True,
                download_name=f'encrypted_{file.filename}',
                mimetype='image/png'
            )
            
        except Exception as e:
            flash(f'Error during encryption: {str(e)}', 'error')
            return redirect(request.url)

    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        try:
            # Basic file check
            if 'image' not in request.files:
                return jsonify({'error': 'No file uploaded'}), 400
            
            file = request.files['image']
            if file.filename == '':
                return jsonify({'error': 'No file selected'}), 400
            
            # Get password
            password = request.form.get('password', '').strip()
            if not password:
                return jsonify({'error': 'Password is required'}), 400

            try:
                # Read image directly from request
                img = Image.open(file)
                # Convert to RGB if necessary
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
            except Exception as e:
                return jsonify({'error': 'Invalid image file'}), 400
            
            # Decrypt the message
            try:
                decrypted_message = decrypt_message(img, password)
                if decrypted_message:
                    # Return the decrypted message as JSON
                    return jsonify({
                        'success': True,
                        'message': decrypted_message
                    })
                else:
                    return jsonify({
                        'error': 'No message found in image'
                    }), 400
            except ValueError as e:
                return jsonify({
                    'error': str(e)
                }), 400
            
        except Exception as e:
            return jsonify({
                'error': f'Decryption failed: {str(e)}'
            }), 500

    # For GET requests, just render the template
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
