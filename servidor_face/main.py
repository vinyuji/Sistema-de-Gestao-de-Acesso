from flask import Flask, request, render_template, jsonify
import os
import cv2
import face_recognition
import numpy as np
from datetime import datetime
import requests
from flask import send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ESP_RELE_URL = 'http://192.168.0.141/open'  # IP do ESP que controla o servicos

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Rosto da câmera ao vivo
CAM_URL = 'http://192.168.0.140/capture' # Ip do Esp Cam Capture

CAM_STREAM = 'http://192.168.0.140:81/stream' # Ip do Esp Cam Stream

def load_known_faces():
    known_encodings = []
    known_names = []

    for file in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, file)
        img = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(img)
        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(os.path.splitext(file)[0])
    return known_encodings, known_names

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/capture', methods=['POST'])
def capture_face():
    name = request.form['name']
    img_resp = requests.get(CAM_URL)
    img_array = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)
    path = os.path.join(UPLOAD_FOLDER, f"{name}.jpg")
    cv2.imwrite(path, img)
    return f"Rosto de {name} salvo com sucesso!"

@app.route('/check', methods=['GET'])
def check_faces():
    known_encodings, known_names = load_known_faces()

    img_resp = requests.get(CAM_URL)
    img_array = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)

    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb_img)
    encodings = face_recognition.face_encodings(rgb_img, faces)

    for encoding in encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding)
        if True in matches:
            matched_idx = matches.index(True)
            name = known_names[matched_idx]
            print(f"[INFO] {name} reconhecido!")
            # Envia sinal para ESP com relé
            try:
    
                requests.get(ESP_RELE_URL)
            except Exception as e:
                print("Erro ao enviar sinal para ESP:", e)

            return jsonify({'status': 'recognized', 'name': name})

    return jsonify({'status': 'not_recognized'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
