import unittest
from tensorflow.keras.models import load_model
from data_preprocessing import load_data

class TestPoseDetection(unittest.TestCase):

    def test_model_accuracy(self):
        # Load the trained model
        model = load_model('models/trained_model.h5')

        # Path to the dataset
        data_dir = '/home/tatsuhirosatou/proj/YogaPoseCorrection/assets/yoga_poses/'

        # Load validation data
        _, validation_generator = load_data(data_dir)

        # Evaluate the model
        val_loss, val_accuracy = model.evaluate(validation_generator)

        # Test that accuracy is above a threshold
        self.assertGreater(val_accuracy, 0.7, "Model accuracy is too low")

if __name__ == '__main__':
    unittest.main()
