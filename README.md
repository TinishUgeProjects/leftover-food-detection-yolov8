# 🥡 Leftover Food Detection using YOLOv8

Leftover Food Detection using YOLOv8 is a computer vision-based solution developed to identify and classify leftover food items from images or video feeds. The primary aim is to promote food sustainability by monitoring waste in canteens, restaurants, and households. Leveraging the Ultralytics YOLOv8 object detection model, the system is trained on a custom dataset to detect categories like rice, curry, roti, vegetables, etc. The project includes a Flask-based web dashboard for uploading images, viewing detections, and logging waste analytics for further study.

## 🚀 Features
- Trained YOLOv8 model for classifying leftover food.
- Real-time detection via webcam or video input.
- Automatic logging of detections for analytics.
- Simple Flask web UI to upload images/videos and view results.

## 🛠️ Tech Stack
- Python
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV
- Flask (for web dashboard)
- Pandas (for analytics)

## 🧪 Model Training
```bash
yolo task=detect mode=train model=yolov8n.pt data=dataset.yaml epochs=50 imgsz=640
```

## 🔍 Detection
```bash
python detect.py --source 0 --weights weights/best.pt --conf 0.5
```

## 🌐 Web Interface
```bash
cd app
python app.py
```

## 📊 Future Improvements
- Integrate cloud upload and auto alert system.
- Nutritional estimation based on detected food.
- Waste tracking dashboard.
