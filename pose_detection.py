import cv2
import mediapipe as mp
import numpy as np
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Initialize Mediapipe for pose detection
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Load the pre-trained model
model = joblib.load('/models/final_model.pkl')  # Update with the latest model file

# Function to extract landmarks for a single image
def extract_landmarks(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    if results.pose_landmarks:
        landmarks = [
            [lm.x, lm.y, lm.z] for lm in results.pose_landmarks.landmark
        ]
        return np.array(landmarks).flatten()  # Flatten for model input
    return None

# Evaluate model performance on test data
def evaluate_model(test_data_path):
    # Assuming test_data_path has test images structured like `/assets/yoga_poses/`
    true_labels = []
    predicted_labels = []
    for label in os.listdir(test_data_path):
        folder_path = os.path.join(test_data_path, label)
        if os.path.isdir(folder_path):
            for image_file in os.listdir(folder_path):
                image_path = os.path.join(folder_path, image_file)
                landmarks = extract_landmarks(image_path)
                if landmarks is not None:
                    prediction = model.predict([landmarks])
                    predicted_labels.append(prediction[0])
                    true_labels.append(label)
    
    # Performance metrics
    print("Classification Report:")
    print(classification_report(true_labels, predicted_labels))
    print("Accuracy:", accuracy_score(true_labels, predicted_labels))

# Example usage:
# evaluate_model('/assets/yoga_poses/test/')
