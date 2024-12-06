# AI-Powered Yoga Pose Detection and Correction: Proof of Concept

## Objective

This project aims to develop an AI-powered feature for yoga practitioners, focusing on detecting yoga poses and providing feedback for posture alignment and accuracy. The solution offers real-time feedback to enhance the yoga experience, helping practitioners improve their pose execution and reduce the risk of injury.

## Use Case

The selected use case for this project is **Pose Detection & Correction**. The goal is to use AI to identify yoga poses and provide feedback to help users improve their alignment and posture.

## Problem Understanding & Creativity

Yoga practitioners, especially beginners, often struggle with maintaining the correct posture. This project leverages AI and pose detection models to identify key landmarks on a user's body during yoga practice, assess whether they are performing a pose correctly, and provide real-time feedback to improve their posture.

The innovative approach involves combining pose detection with pose correction feedback, which includes displaying the pose name, providing detailed alignment instructions, and suggesting improvements based on the detected pose.

## Model Development

### Dataset

The dataset used for training the model is the **Yoga Pose Classification** dataset from Kaggle. This dataset contains labeled images for different yoga poses, which are used for training and evaluation of the model.

**Dataset Link**: [Yoga Pose Classification Dataset](https://www.kaggle.com/datasets/ujjwalchowdhury/yoga-pose-classification)

### Data Preprocessing

The images from the dataset are preprocessed by:
- **Resizing** them to a fixed size.
- **Normalizing** pixel values.
- Applying **data augmentation** techniques like rotation and flipping to enhance the model’s ability to generalize.

### Model Architecture

For pose detection, we utilized **MediaPipe Pose**, a pre-trained model provided by Google that detects 33 key body landmarks in real-time. These landmarks are used to infer the yoga pose and provide feedback for posture alignment.

### Training the Model

The model was trained using **transfer learning**, where we fine-tuned the pre-trained **MediaPipe Pose** model for the specific task of detecting yoga poses. The feedback provided by the system was enhanced iteratively by analyzing the model's predictions and adjusting the feedback mechanism based on pose detection accuracy.

### Model Performance

The model is evaluated on:
- **Accuracy**: The model’s ability to correctly identify poses based on key points detected.
- **Feedback Quality**: The effectiveness of the feedback in helping users improve their poses.

### Optimization

The model was optimized for real-time performance using **MediaPipe Pose**, which runs efficiently on both CPU and GPU. The feedback system was optimized by improving the alignment accuracy and response time of pose detection.

---

## User-Centric Application

### User Interface

The application provides a user-friendly interface where users can either use a webcam or upload an image to check their pose. The application displays the detected pose name and provides feedback for improving posture.

### Key Features:
1. **Pose Detection**: Identifies the yoga pose using MediaPipe Pose.
2. **Pose Feedback**: Provides real-time feedback about alignment and posture.
3. **Pose Name and Description**: Displays the detected pose with a short description for the user to understand the correct pose.
4. **Scalability**: The application can scale for multiple users practicing yoga simultaneously.

### Integration with Yoga App (Optional)

Though not implemented in this PoC, the system can be integrated into a yoga app by creating an API endpoint that receives image data or real-time video feed and returns feedback on the yoga pose.

---

## Code Walkthrough

### Key Files:

- **pose_detection.py**: Contains code for detecting key points and classifying poses based on the detected landmarks.
- **feedback.py**: Provides the feedback mechanism, analyzing the detected pose and providing corrective instructions.
- **app.py**: (Optional) This is the FastAPI or Flask application that could serve as the backend for the yoga pose detection system.

---

## Results

### Pose Detection and Feedback:

The system can accurately detect and label poses like Tree Pose, Warrior 2, etc., and provides immediate feedback on whether the user’s alignment is correct.

### Performance Visualization:

The model detects 33 key landmarks on the user's body and compares them with the standard pose for feedback generation. For example, if the user is performing the Tree Pose incorrectly, the feedback system will suggest alignment adjustments for better execution.

---

## Scalability

The system is designed to handle multiple users practicing yoga simultaneously. As the dataset grows, additional poses can be added to the model, and the feedback system can be fine-tuned for better accuracy.

---

## Next Steps

1. **Improvement of Feedback Accuracy**: More refined feedback can be provided by enhancing the pose detection model and adding more detailed correction suggestions.
2. **Integration with Yoga App**: Develop a mobile or web application where users can interact with the system directly through their devices.
3. **Multi-Pose Detection**: Extend the model to detect multiple poses simultaneously for group sessions.

---

## Conclusion

This AI-powered yoga pose detection and correction tool demonstrates how AI can enhance the yoga experience by providing real-time feedback, improving posture accuracy, and preventing injuries. The system is user-friendly, scalable, and has the potential for integration into a full yoga app.

---

## Submission

- **Code Repository**: All code is available in the GitHub repository (https://github.com/debargyadinda/YogaPoseCorrection/).
- **Documentation**: This README file contains the detailed explanation of the approach, model, results, and next steps.

---

### GitHub Repository Description (short):

"AI-powered Yoga Pose Detection and Correction system for real-time feedback on posture alignment and improvement."

How to Use:

    Clone the repository:

git clone https://github.com/yourusername/YogaPoseCorrection.git
cd YogaPoseCorrection

Install dependencies:

pip install -r requirements.txt

Run the model:

python pose_detection.py --image_path path/to/image.jpg

Get feedback on a pose:

    python feedback.py --image_path path/to/image.jpg

This README.md file is now properly formatted to provide clear instructions and documentation for your project.
