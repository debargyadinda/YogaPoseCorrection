from tensorflow.keras.models import load_model
from data_preprocessing import load_data

def evaluate_model():
    # Path to the trained model
    model = load_model('models/trained_model.h5')

    # Path to the dataset
    data_dir = '/home/tatsuhirosatou/proj/YogaPoseCorrection/assets/yoga_poses/'

    # Load data
    _, validation_generator = load_data(data_dir)

    # Evaluate the model
    val_loss, val_accuracy = model.evaluate(validation_generator)
    print(f"Validation Accuracy: {val_accuracy*100:.2f}%")

if __name__ == '__main__':
    evaluate_model()
