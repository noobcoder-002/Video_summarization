import os
import csv
import shutil
threshold = 0.50
csv_file = 'relevance_scores.csv'
input_image_folder = '/Users/nileshkumar/Desktop/Python/freeGuyFrame/'

output_image_folder = 'Relevent_frames/'


output_csv_file = 'selected_images.csv'


if not os.path.exists(output_image_folder):
    os.makedirs(output_image_folder)


selected_images_details = []


with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:

        relevance_score = float(row['Relevance Score'])

        if relevance_score >= threshold:

            image_filename = row['Image Filename']

            input_image_path = os.path.join(input_image_folder, image_filename)
            output_image_path = os.path.join(
                output_image_folder, image_filename)
            shutil.copyfile(input_image_path, output_image_path)

            selected_images_details.append(
                {'Image Filename': image_filename, 'Relevance Score': relevance_score})


with open(output_csv_file, mode='w', newline='') as file:
    fieldnames = ['Image Filename', 'Relevance Score']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerows(selected_images_details)

print(f"{len(selected_images_details)} images with scores above {threshold} were copied to the '{output_image_folder}' folder.")
print(f"Details of selected images were saved to '{output_csv_file}'.")
