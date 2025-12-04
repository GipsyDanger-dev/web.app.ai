import os
from flask import Flask, render_template, send_from_directory

# Mendapatkan lokasi absolut folder tempat app.py berada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Menentukan lokasi folder static dan templates
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def index():
    return render_template('index.html')

# Route Khusus untuk Model
@app.route('/model_web/<path:filename>')
def serve_model(filename):
    # Mengarahkan langsung ke folder static/model_web
    model_dir = os.path.join(STATIC_DIR, 'model_web')
    return send_from_directory(model_dir, filename)

if __name__ == '__main__':
    print(f"✅ Aplikasi berjalan!")
    print(f"📂 Folder Static: {STATIC_DIR}")
    print(f"📂 Folder Model: {os.path.join(STATIC_DIR, 'model_web')}")
    app.run(debug=True, port=5000)