import cv2
import os

input_folder = "/Users/nileshkumar/Desktop/Python/freeGuyFrame/"
output_folder = "output_folder/"

os.makedirs(output_folder, exist_ok=True)

image_files = [f for f in os.listdir(input_folder) if f.endswith(
    (".jpg", ".jpeg", ".png", ".bmp"))]

scale_factor = 0.25

for image_file in image_files:
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)

    img = cv2.imread(input_path)

    height, width, _ = img.shape

    # Calculate the new dimensions
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # Resize the image
    resized_img = cv2.resize(img, (new_width, new_height),
                             interpolation=cv2.INTER_AREA)

    # Save the resized image
    cv2.imwrite(output_path, resized_img)

print("Images resized and saved to the output folder.")
