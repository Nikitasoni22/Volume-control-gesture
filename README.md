# 🎛️ Gesture-Based Volume Control using OpenCV

Control your system volume using hand gestures in real-time using Computer Vision 🤚📷

---

## 🚀 Features

* 🎯 Real-time hand tracking using MediaPipe
* 🔊 Control system volume with finger distance
* 📉 Smooth volume transition (no sudden jumps)
* 🎥 Webcam-based interaction
* ⚡ Fast and responsive

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy
* Pycaw (for system volume control)

---

## 📂 Project Structure

```
volume-control-gesture/
│
├── volume_control_gesture.py   # Main program
├── hand_tracking_module.py     # Hand tracking logic
├── requirements.txt            # Dependencies
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository

```
git clone https://github.com/your-username/volume-control-gesture.git
cd volume-control-gesture
```

2. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main file:

```
python volume_control_gesture.py
```

---

## 🧠 How it Works

* Detects hand landmarks using MediaPipe
* Measures distance between thumb and index finger
* Maps distance to system volume range
* Uses interpolation for smooth control

---

## 🔥 Future Improvements

* Add gesture-based mute/unmute
* Multi-hand support
* GUI overlay improvements

---

## 🙌 Acknowledgements

* MediaPipe by Google
* OpenCV community

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
