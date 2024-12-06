import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_data(data_dir, img_size=(224, 224), batch_size=32):
    # Define the ImageDataGenerator with validation split
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )
    
    # Load training data
    train_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training',
    )
    
    # Load validation data
    validation_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation',
    )

    return train_generator, validation_generator
