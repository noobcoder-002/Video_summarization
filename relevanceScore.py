import cv2
import numpy as np
import os
import csv


def calculate_relevance_scores(frames_directory, sample_image):

    relevance_scores = {}


    gray_sample_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)


    hist_sample_image = cv2.calcHist(
        [gray_sample_image], [0], None, [256], [0, 256])
    hist_sample_image /= hist_sample_image.sum()

    for frame_filename in os.listdir(frames_directory):
        frame_path = os.path.join(frames_directory, frame_filename)
        frame = cv2.imread(frame_path)


        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        hist_frame = cv2.calcHist([gray_frame], [0], None, [256], [0, 256])
        hist_frame /= hist_frame.sum()

        intersection = cv2.compareHist(
            hist_frame, hist_sample_image, cv2.HISTCMP_INTERSECT)


        relevance_scores[frame_filename] = intersection

    return relevance_scores


def save_relevance_scores_to_csv(relevance_scores, csv_filename):

    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['Image Filename', 'Relevance Score']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for filename, score in relevance_scores.items():
            writer.writerow({'Image Filename': filename,
                            'Relevance Score': score})



frames_directory = '/Users/nileshkumar/Desktop/Python/freeGuyFrame'

sample_image_path = '/Users/nileshkumar/Desktop/Python/videoToFrame/freeGuy.jpeg'
sample_image = cv2.imread(sample_image_path)

relevance_scores = calculate_relevance_scores(frames_directory, sample_image)
csv_filename = 'relevance_scores.csv'  
save_relevance_scores_to_csv(relevance_scores, csv_filename)
