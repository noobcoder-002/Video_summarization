import cv2
import os
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')
nltk.download('stopwords')


def select_keyframes(frames_directory, num_keyframes=5):

    frame_files = os.listdir(frames_directory)

    num_keyframes = min(num_keyframes, len(frame_files))

    relevance_scores = []

    for frame_filename in frame_files:

        frame_path = os.path.join(frames_directory, frame_filename)
        frame = cv2.imread(frame_path)

        relevance_score = calculate_relevance_score(frame)

        relevance_scores.append((frame_filename, relevance_score))

    # Sort frames by relevance score in descending order
    relevance_scores.sort(key=lambda x: x[1], reverse=True)

    # Select the top N keyframes based on relevance
    selected_frames = [frame[0] for frame in relevance_scores[:num_keyframes]]

    return selected_frames


def calculate_relevance_score(frame):
    """
    Calculate a relevance score for a frame based on color histogram difference.

    Args:
        frame (numpy.ndarray): The input video frame.

    Returns:
        float: The relevance score for the frame (lower values are more relevant).
    """

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hist = cv2.calcHist([gray_frame], [0], None, [256], [0, 256])

    hist /= hist.sum()

    reference_hist = np.array([0.01] * 256)
    difference = cv2.compareHist(reference_hist, hist, cv2.HISTCMP_CHISQR)

    return difference


def process_query(query):

    tokens = word_tokenize(query)

    # Convert tokens to lowercase
    tokens = [word.lower() for word in tokens]

    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [
        word for word in tokens if word not in string.punctuation and word not in stop_words]

    return tokens


def summarize_video(frames_directory, selected_keyframes, output_video_path):

    first_frame_path = os.path.join(frames_directory, selected_keyframes[0])
    first_frame = cv2.imread(first_frame_path)
    height, width, layers = first_frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 30.0, (width, height))

    for frame_filename in selected_keyframes:
        frame_path = os.path.join(frames_directory, frame_filename)
        frame = cv2.imread(frame_path)
        out.write(frame)

    out.release()
    cv2.destroyAllWindows()


def main():
    frames_directory = 'framesVideo2'
    user_query = "important moments in the video"

    selected_frames = select_keyframes(frames_directory)

    query_tokens = process_query(user_query)

    summarize_video(frames_directory, selected_keyframes, output_video_path)


if __name__ == "__main__":
    main()
