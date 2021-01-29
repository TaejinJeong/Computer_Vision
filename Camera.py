import cv2

output_path = './Video/test.mp4'
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_output = cv2.VideoWriter(output_path, fourcc, 30.0, (640,320))

idx = 0
while cap.isOpened():

    ret, frame = cap.read()
    if ret:
        resize_frame = cv2.resize(frame, (640, 320))
        video_output.write(resize_frame)

        if idx % 30 == 0:
            print(idx)

        idx += 1
        if idx > 300:
            break
    else:
        break

cap.release()
video_output.release()