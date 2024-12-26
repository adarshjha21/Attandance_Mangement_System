import os
import cv2

# Paths to your positive and negative image directories
positive_images_path = 'path/to/positive/images'
negative_images_path = 'path/to/negative/images'

# Create a text file for positive samples
with open('positives.txt', 'w') as pos_file:
    for filename in os.listdir(positive_images_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Get the full path of the image
            img_path = os.path.join(positive_images_path, filename)
            # Get the dimensions of the image
            img = cv2.imread(img_path)
            height, width = img.shape[:2]
            # Write to the file
            pos_file.write(f"{img_path} 1 0 0 {width} {height}\n")

# Create a text file for negative samples
with open('negatives.txt', 'w') as neg_file:
    for filename in os.listdir(negative_images_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(negative_images_path, filename)
            neg_file.write(f"{img_path}\n")

# Train the Haar Cascade
# Set parameters
num_pos = len(open('positives.txt').readlines())
num_neg = len(open('negatives.txt').readlines())
num_stages = 10  # Number of stages for training
min_hit_rate = 0.995  # Minimum hit rate
max_false_alarm_rate = 0.5  # Maximum false alarm rate
feature_type = 'Haar'  # Feature type

# Command to train the classifier
os.system(f"opencv_traincascade -data data/ -vec positives.vec -bg negatives.txt -numPos {num_pos} -numNeg {num_neg} -numStages {num_stages} -minHitRate {min_hit_rate} -maxFalseAlarmRate {max_false_alarm_rate} -featureType {feature_type}")

print("Training completed!")