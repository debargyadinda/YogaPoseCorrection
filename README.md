# AI-Powered Yoga Pose Detection and Correction: Proof of Concept

## Objective

This project aims to develop an AI-powered feature for yoga practitioners, focusing on detecting yoga poses and providing feedback for posture alignment and accuracy. The solution offers real-time feedback to enhance the yoga experience, helping practitioners improve their pose execution and reduce the risk of injury.

## Use Case

The selected use case for this project is **Pose Detection & Correction**. The goal is to use AI to identify yoga poses and provide feedback to help users improve their alignment and posture.

## Problem Understanding & Creativity

Yoga practitioners often struggle with maintaining the correct posture, especially beginners. This project leverages AI and pose detection models to identify key landmarks on a user's body during yoga practice, assess whether they are performing a pose correctly, and provide real-time feedback to improve their posture.

The innovative approach involves combining pose detection with pose correction feedback, which includes displaying the pose name, providing detailed alignment instructions, and suggesting improvements based on the detected pose.

## Model Development

### Dataset

The dataset used for training the model is the **Yoga Pose Classification** dataset from Kaggle, available [here](https://www.kaggle.com/datasets/ujjwalchowdhury/yoga-pose-classification). The dataset contains labeled images for different yoga poses, which will be used for both training and evaluation of the model.

### Data Preprocessing

The dataset images are preprocessed by:
- **Resizing** them to a fixed size (224x224 pixels).
- **Normalizing** pixel values between 0 and 1.
- Data augmentation techniques like **rotation**, **flipping**, and **shifting** were applied to enhance the model's ability to generalize.

### Model Architecture

For pose detection, we utilized **MediaPipe Pose**, a pre-trained model provided by Google that detects 33 key body landmarks in real-time. The landmarks are used to infer the yoga pose and provide feedback for posture alignment.

In addition, a feedback system was implemented to guide the user in adjusting their pose, showing the name of the pose along with a description.

### Training the Model

The model was trained using **transfer learning**, where we fine-tuned an existing pre-trained model (MediaPipe Pose) for our specific task. The feedback provided was enhanced iteratively by analyzing the model's predictions and adjusting the feedback mechanism based on the pose detection accuracy.

### Model Performance

The performance of the model was evaluated based on:
- **Accuracy**: The model's ability to correctly identify poses based on key points detected.
- **Feedback Quality**: The effectiveness of the feedback in helping users improve their poses.

### Optimization

The model was optimized for real-time performance using **MediaPipe Pose**, which runs efficiently on both CPU and GPU. The feedback system was optimized by improving the alignment accuracy and response time of the pose detection.

## User-Centric Application

### User Interface

The application provides a user-friendly interface where users can either use a webcam or upload an image to check their pose. The application displays the detected pose name and provides feedback for improving posture.

### Key Features:
- **Pose Detection**: Identifies the yoga pose using MediaPipe Pose.
- **Pose Feedback**: Provides real-time feedback about the alignment and posture.
- **Pose Name and Description**: Displays the detected pose with a short description for the user to understand the correct pose.

### Scalability

The application can handle multiple users practicing yoga simultaneously. As the dataset grows, new poses can be added to the model, and the feedback system can be fine-tuned to improve accuracy. Additionally, it is designed to handle an increasing number of concurrent requests, making it scalable for broader use.

### Integration with Yoga App (Optional)

Though not implemented in this PoC, this feature could be integrated into a yoga app by creating an API endpoint that receives image data or a real-time video feed and returns feedback on the yoga pose.

## Code Walkthrough

### Key Files:
- **pose_detection.py**: This script contains the code for detecting keypoints and classifying poses based on the detected landmarks.
- **feedback.py**: This script provides the feedback mechanism, analyzing the detected pose and providing corrective instructions.
- **app.py**: (Optional) This is the FastAPI or Flask application that could serve as the backend for the yoga pose detection system.


## Results

### Pose Detection and Feedback:
The system can accurately detect and label poses like Tree Pose, Warrior 2, etc., providing immediate feedback on whether the user's alignment is correct. The feedback is dynamic and adjusts according to the keypoints detected.

### Performance Visualization:
The pose detection model detects 33 key landmarks on the user's body and compares them with the standard pose for feedback generation. For example, if the user is performing the Tree Pose incorrectly, the feedback system will suggest alignment adjustments for better execution.

### Scalability:
The system is designed to be scalable, able to handle multiple users practicing yoga simultaneously. As the dataset grows, additional poses can be added to the model, and the feedback system can be fine-tuned for better accuracy. Furthermore, the backend can be extended to handle more requests by implementing more robust infrastructure for concurrent usage.

## Next Steps

- **Improvement of Feedback Accuracy**: More refined feedback can be provided by enhancing the pose detection model and adding more detailed correction suggestions.
- **Integration with Yoga App**: Develop a mobile or web application where users can interact with the system directly through their devices.
- **Multi-Pose Detection**: Extend the model to detect multiple poses simultaneously for group sessions.

## Conclusion

This AI-powered yoga pose detection and correction tool demonstrates how AI can enhance the yoga experience by providing real-time feedback, improving posture accuracy, and preventing injuries. The system is user-friendly and scalable, with potential for integration into a full yoga app.

## Submission

- **Code Repository**: All code is available in the GitHub repository [YogaPoseCorrection](https://github.com/debargyadinda/YogaPoseCorrection/).
- **Documentation**: This README file contains the detailed explanation of the approach, model, results, and next steps.

### Example Usage:

To run the system, use the following command:

```bash
python pose_detection.py --image_path path/to/image.jpg
