import cv2
import mediapipe as mp

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Function to visualize the pose with feedback
def visualize_pose(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    
    if results.pose_landmarks:
        # Draw landmarks on image
        mp.solutions.drawing_utils.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    return image

# Function to process the pose feedback and visualization
def process_pose(image_path):
    feedback = evaluate_pose(image_path)
    print(f"Feedback: {feedback}")
    
    image = visualize_pose(image_path)
    cv2.imshow('Pose Feedback', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Testing the function with an image
image_path = '/home/your_username/proj/YogaPoseCorrection/assets/yoga_poses/Tree/00000034.jpg'  # replace with actual path
process_pose(image_path)
