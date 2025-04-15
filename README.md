# Real-Time Object Detection and RViz Visualization with YOLOv8 + ROS2

This project integrates **YOLOv8 object detection** with **ROS2** to visualize detected object positions in **RViz2** as red spherical markers. Perfect for robotic perception and spatial awareness demos.

---

## Overview

We use **YOLOv8** on a Windows host to detect objects from the webcam. The center of each detected bounding box is sent to **ROS2 on WSL/Linux** via UDP, where it's rendered in **RViz**.

---

## Architecture

```
[Camera + YOLO (Windows)]
         |
     (UDP Socket)
         ↓
[ROS2 Node (WSL)]
         ↓
   [RViz Marker]
```

---

## Features

- Real-time webcam detection via YOLOv8
- UDP socket communication between Windows ↔ WSL
- Marker publishing in ROS2
- Live object tracking in RViz2
- Prints object name + coordinates (e.g., `Sent: person: (324.2, 265.8)`)

---

## Requirements

### Windows (for YOLO sender)
- Python 3.10+
- OpenCV
- Ultralytics
- Webcam

Install with:
```bash
pip install ultralytics opencv-python
```

### WSL/Linux (ROS2 side)
- Ubuntu 22.04 + ROS2 Humble
- Python 3.10
- `cv_bridge`, `numpy`, `rclpy`, `visualization_msgs`

Activate your venv:
```bash
python3 -m venv ~/ros2_ws/venv
source ~/ros2_ws/venv/bin/activate
pip install numpy==1.24.4 opencv-python pickle5
```

---

## How to Run

### 1. Start RViz2 in WSL
```bash
source /opt/ros/humble/setup.bash
rviz2
```
> Set the **Fixed Frame** to `base_link` and add a `Marker` display subscribed to `/visualization_marker`.

---

### 2. In WSL – Start ROS2 Marker Receiver
```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/venv/bin/activate
export PYTHONPATH=/opt/ros/humble/lib/python3.10/site-packages:$PYTHONPATH
python3 socket_marker_publisher.py
```

---

### 3. In Windows – Run YOLO Sender
```bash
python yolo_socket_sender.py
```

---

## Output Example

Terminal:
```
Sent: person: (345.2, 288.1)
Sent: cell phone: (189.5, 122.3)
```

RViz:
- Red dot moves as object moves in front of webcam 👀
- Marker updates every 0.1s

---

## Folder Structure

```
project/
├── yolo_socket_sender.py
├── socket_marker_publisher.py
├── camera_sender.py (optional)
├── camera_socket_receiver.py (optional)
├── README.md
├── COMP-3766 - Video presentation.mp4
```
