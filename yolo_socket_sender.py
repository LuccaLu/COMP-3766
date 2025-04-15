import socket
import cv2
from ultralytics import YOLO

HOST = '192.168.165.170'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    results = model(frame, verbose=False)
    annotated_frame = results[0].plot()
    cv2.imshow('YOLO Detection', annotated_frame)

    for box, cls in zip(results[0].boxes.xyxy, results[0].boxes.cls):
        x1, y1, x2, y2 = box.tolist()
        label = model.names[int(cls)]
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        message = f"{label}: ({center_x:.1f}, {center_y:.1f})"
        print(f"Sent: {message}")
        client_socket.sendto(f"{center_x},{center_y}".encode(), (HOST, PORT))
        break  

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
client_socket.close()
cv2.destroyAllWindows()
