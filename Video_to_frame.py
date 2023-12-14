import cv2
import os

video_path = '/Users/nileshkumar/Desktop/Python/videoToFrame/Free Guy _ Official Trailer _ 20th Century Studios.mp4'

output_directory = 'freeGuyFrame'
os.makedirs(output_directory, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1
    frame_filename = os.path.join(
        output_directory, f'frame_{frame_count:04d}.jpg')

    cv2.imwrite(frame_filename, frame)


cap.release()
cv2.destroyAllWindows()

print(f"Total {frame_count} frames saved in '{output_directory}' directory.")
