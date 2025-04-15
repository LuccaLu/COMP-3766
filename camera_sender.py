import cv2
import socket
import struct
import pickle

server_address = ('192.168.165.170', 8485) 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            continue

        data = pickle.dumps(frame)
        size = struct.pack(">L", len(data))
        sock.sendall(size + data)
        print(f"Sent frame of size {len(data)}")

except Exception as e:
    print(f"Exception: {e}")

finally:
    cap.release()
    sock.close()
    print("Camera and socket closed cleanly.")
