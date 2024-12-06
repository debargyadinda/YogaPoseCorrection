import cv2
import mediapipe as mp

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Function to detect keypoints using MediaPipe
def get_keypoints(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    keypoints = {}
    if results.pose_landmarks:
        for idx, landmark in enumerate(results.pose_landmarks.landmark):
            keypoints[mp_pose.PoseLandmark(idx).name] = (landmark.x, landmark.y)
    
    return keypoints

# Define ideal keypoints (simplified example, can be more detailed)
ideal_keypoints = {
    'LEFT_SHOULDER': (0.5, 0.2),  # Example values, should be based on the ideal pose
    'RIGHT_SHOULDER': (0.5, 0.2),
    'LEFT_ELBOW': (0.4, 0.5),
    'RIGHT_ELBOW': (0.6, 0.5),
    'LEFT_WRIST': (0.4, 0.7),
    'RIGHT_WRIST': (0.6, 0.7),
    # Add more body parts as necessary
}

# Function to check if pose is accurate
def is_pose_accurate(detected_keypoints, ideal_keypoints, threshold=0.05):
    feedback = "Pose is accurate."
    
    for part, ideal_coords in ideal_keypoints.items():
        if part in detected_keypoints:
            detected_coords = detected_keypoints[part]
            distance = ((detected_coords[0] - ideal_coords[0])**2 + (detected_coords[1] - ideal_coords[1])**2)**0.5
            if distance > threshold:
                feedback = "Pose is incorrect."
                break
    
    return feedback

# Main function to process the image and give feedback
def evaluate_pose(image_path):
    keypoints = get_keypoints(image_path)
    feedback = is_pose_accurate(keypoints, ideal_keypoints)
    
    # Display the feedback on the image
    image = cv2.imread(image_path)
    cv2.putText(image, feedback, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # Show the image with feedback
    cv2.imshow("Pose Feedback", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run pose evaluation on an image
image_path = '/home/tatsuhirosatou/proj/YogaPoseCorrection/assets/yoga_poses/Tree/00000015.jpg'  # Replace with your image path
evaluate_pose(image_path)
