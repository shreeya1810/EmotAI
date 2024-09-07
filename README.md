# EmotAI

**EmotAI** is an advanced emotion detection system that analyzes emotions from image inputs using ensemble learning techniques. The system achieves 85% accuracy in detecting emotional states and offers a full-stack solution with a **Flask** backend and **React** frontend for real-time sentiment analysis.

## Features

- **85% Accuracy** in detecting emotions from facial images
- **Real-time emotion detection** with a full-stack web interface
- **Ensemble Learning** approach combining multiple models for improved accuracy

## Methodology

1. **Data Preprocessing**: Facial images are preprocessed using OpenCV for face detection.
2. **Ensemble Learning**: Multiple deep learning models are combined for emotion classification, leveraging the strengths of different architectures like CNN, VGG, and ResNet.
3. **Real-time Detection**: The Flask backend processes images and detects emotions, while the React frontend displays the results in real-time.

## Results

- **85% Accuracy** in emotion detection across 7 primary emotions (Happy, Sad, Angry, Fear, Surprise, Disgust, Neutral)
- **Fast Processing**: Real-time feedback with minimal latency for live emotion analysis

## Requirements

- Python 3.7+
- Flask, Keras, TensorFlow, OpenCV, React.
