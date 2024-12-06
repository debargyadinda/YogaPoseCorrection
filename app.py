import cv2
import mediapipe as mp

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Function to detect keypoints using MediaPipe
def get_keypoints(frame):
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    
    keypoints = {}
    if results.pose_landmarks:
        for idx, landmark in enumerate(results.pose_landmarks.landmark):
            keypoints[mp_pose.PoseLandmark(idx).name] = (landmark.x, landmark.y)
    
    return keypoints

# Function to show the pose feedback and webcam feed
def show_pose_feedback():
    # Try opening default camera first (index 0)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open the default camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image from camera.")
            break
        
        keypoints = get_keypoints(frame)
        
        if keypoints:
            # Display pose feedback (you can customize the feedback here)
            pose_name = "Tree Pose"  # Example, can be dynamic based on pose detection logic
            cv2.putText(frame, pose_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Display the webcam feed with feedback
        cv2.imshow("Pose Feedback", frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Run the function to show pose feedback
show_pose_feedback()
