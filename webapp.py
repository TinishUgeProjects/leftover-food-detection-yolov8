import io
from PIL import Image
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename
import os
from ultralytics import YOLO

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def predict_img():
    if request.method == "POST":
        if 'file' in request.files:
            f = request.files['file']
            if f.filename == '':
                return redirect(request.url)
            if f:
                filepath = os.path.join('uploads', secure_filename(f.filename))
                f.save(filepath)

                file_extension = f.filename.rsplit('.', 1)[1].lower()

                if file_extension in ['jpg', 'jpeg', 'png']:
                    img = cv2.imread(filepath)
                    image = Image.open(filepath)

                    # Perform the detection
                    yolo = YOLO('best.pt')
                    detections = yolo.predict(image, save=True)
                    return redirect(url_for('display', filename=f.filename))
                else:
                    return "Invalid file format. Please upload a JPG, JPEG, or PNG image."

    return "No file selected."

@app.route('/display/<filename>')
def display(filename):
    folder_path = 'runs/detect'
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    latest_subfolder = max(subfolders, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
    directory = folder_path+'/'+latest_subfolder
    files = os.listdir(directory)
    latest_file = files[0]
    filename = os.path.join(directory, latest_file)
    return send_file(filename, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)
