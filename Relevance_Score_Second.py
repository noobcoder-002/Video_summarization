import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import csv

# Define the folder containing the images
image_folder = '/Users/nileshkumar/Desktop/Python/freeGuyFrame'

# Define the user query for scoring criteria
user_query = 'car'  # Define your specific query logic

# Load the pre-trained ResNet50 model (or use any other model that suits your needs)
model = ResNet50(weights='imagenet')

# Function to load and preprocess an image


def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = preprocess_input(img)
    return img

# Function to score an image based on the user query


def score_image(image_path, model, user_query):
    img = load_and_preprocess_image(image_path)
    img = np.expand_dims(img, axis=0)

    # Get predictions from the pre-trained model
    predictions = model.predict(img)

    # Use your custom logic here to calculate a score based on the user query
    score = custom_scoring_logic(predictions, user_query)

    return score

# Define your custom scoring logic based on the query


def custom_scoring_logic(predictions, user_query):
    # Implement your scoring logic here
    # Example: Extract relevant information from predictions and apply scoring criteria

    # For example, if you want to score based on the highest prediction probability:
    max_prob = np.max(predictions)
    score = max_prob

    # You can replace this logic with your specific criteria

    return score


# Iterate through the images in the folder and score them
image_scores = {}
for filename in os.listdir(image_folder):
    # Adjust the file extensions as needed
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        image_path = os.path.join(image_folder, filename)
        score = score_image(image_path, model, user_query)
        image_scores[filename] = score

# Sort the image scores by their scores (descending order)
sorted_image_scores = {k: v for k, v in sorted(
    image_scores.items(), key=lambda item: item[1], reverse=True)}


csv_filename = 'image_scores.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['Image File', 'Score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for image_file, score in sorted_image_scores.items():
        writer.writerow({'Image File': image_file, 'Score': score})

print(f'Image scores have been saved to {csv_filename}')
