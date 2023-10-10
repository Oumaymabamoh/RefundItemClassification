from flask import Flask, jsonify
import tensorflow as tf
import numpy as np
import os

app = Flask(__name__)


# Load your trained model and compile it
model = tf.keras.models.load_model('ric_model.h5')
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


def normalize_image(image_path):
    try:
        # Load and preprocess the image
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = img_array / 255.0  # Rescale pixel values to [0, 1]
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


@app.route('/')
def index():
    return "Simple API to classify images, with Flask!"


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        # Initialize an empty list to store predictions
        predictions = []

        # Directory path containing multiple images
        image_dir = './test_data'
        image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir) if
                       filename.endswith('.jpg')]

        # Check if there are no images to process
        if not image_paths:
            return jsonify({'message': 'No new data to process'})

        # Process each image in the batch
        for image_path in image_paths:
            normalized_image = normalize_image(image_path)

            if normalized_image is not None:
                # Make predictions using your model
                prediction = model.predict(normalized_image)
                print(f"Raw predictions: {prediction}")

                # Interpret the result and append it to the predictions list
                class_names = ['jeans', 'sofa', 'tshirt', 'tv']  # Replace with your class labels
                predicted_class = class_names[np.argmax(prediction)]
                predictions.append({'prediction': predicted_class})
            else:
                print(f"Image normalization failed for {image_path}")

        return jsonify({'predictions': predictions})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
