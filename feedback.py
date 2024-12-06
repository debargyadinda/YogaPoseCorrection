import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Function to calculate the angle between three points
def calculate_angle(a, b, c):
    a = [a.x, a.y]
    b = [b.x, b.y]
    c = [c.x, c.y]

    radians = math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0])
    angle = abs(radians * 180.0 / math.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

# Function to provide feedback based on pose keypoints
def evaluate_pose(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    
    feedback = []
    if results.pose_landmarks:
        # Example of Tree Pose (focus on angle of arms and legs)
        left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        left_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
        left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        
        # Calculate arm angle (this is a basic example)
        angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
        if angle < 150:
            feedback.append("Adjust left arm angle. Aim for 180 degrees.")
        else:
            feedback.append("Left arm position looks good!")
        
        # Additional pose checks can be added for different poses
        # Example for Warrior pose
        # Evaluate other key points and angles, then provide feedback

    return feedback
