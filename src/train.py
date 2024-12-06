from model import build_model
from data_preprocessing import load_data

def train_model():
    # Path to the dataset
    data_dir = '/home/tatsuhirosatou/proj/YogaPoseCorrection/assets/yoga_poses/'
    
    # Load data
    train_generator, validation_generator = load_data(data_dir)

    # Build model
    model = build_model(num_classes=train_generator.num_classes)
    
    # Train the model
    history = model.fit(
        train_generator,
        epochs=10,
        validation_data=validation_generator
    )

    # Save the trained model
    model.save('models/trained_model.h5')

if __name__ == '__main__':
    train_model()
