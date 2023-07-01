import csv
import datetime

# Open the input CSV files
with open('ocr.csv', newline='') as ocr_file, open('emotions.csv', newline='') as emotions_file:

    # Create CSV readers for both files
    ocr_reader = csv.DictReader(ocr_file)
    emotions_reader = csv.DictReader(emotions_file)

    # Create a dictionary to store the emotion data for each frame
    emotions_data = {}

    # Process the emotions CSV file and populate the emotions data dictionary
    for row in emotions_reader:
        inference_id = row['inference_id']
        meeting_id = row['meeting_id']
        frame_no = row['frame_no']
        emotions = row['emotion']
print("hello")
print("hello2")