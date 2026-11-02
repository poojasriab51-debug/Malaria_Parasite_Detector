# Malaria Parasite Detector

## About the Project

Malaria is a disease caused by parasites that can be identified by examining blood smear images under a microscope. 
<img width="2940" height="1660" alt="62F36472-F71D-4961-926E-E41B9CF0A9A2" src="https://github.com/user-attachments/assets/1a812e77-c63c-4d89-8476-6550af20c6c4" />
Manually examining these images requires time and careful observation, especially when dealing with a large number of samples.
This project explores how image classification using deep learning can help identify malaria-infected and uninfected blood cell images.
I developed a Convolutional Neural Network (CNN) model to classify cell images into two categories: **Parasitized** and **Uninfected**. 
The trained model is integrated into a Streamlit application, where users can upload an image and view the model's prediction.
The main idea behind this project is to make the classification process simple and accessible through a small web application.

## How It Works

1. The user uploads a blood cell image through the Streamlit interface.
2. The uploaded image is resized to 128 × 128 pixels.
3. The image is converted into the format required by the trained CNN model.
4. The model processes the image and predicts whether the cell is Parasitized or Uninfected.
5. The prediction is displayed on the application.

## Model Architecture

The project uses a custom CNN built with TensorFlow and Keras.

The model consists of:

- Convolutional layers for extracting image features.
- Batch Normalization for stabilising training.
- Max Pooling layers for reducing spatial dimensions.
- A Flatten layer to convert feature maps into a one-dimensional representation.
- A Dense layer with ReLU activation.
- Dropout to help reduce overfitting.
- A final Dense layer with sigmoid activation for binary classification.

**Input image size:** 128 × 128 × 3  
**Output classes:** Parasitized and Uninfected  
**Loss function:** Binary Crossentropy  
**Optimizer:** Adam

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pillow (PIL)
- Streamlit

## Dataset

The model was developed using the Cell Images for Detecting Malaria dataset.

The dataset contains two categories:

- **Parasitized:** Blood cell images containing malaria parasites.
- **Uninfected:** Blood cell images without malaria parasites.

Each category contains 13,780 images, giving a total of 27,560 images.

## Project Objective

The objective of this project was to gain practical experience in image classification, CNN architecture, model training and deployment. It also helped me understand how a trained deep learning model can be connected to a user-facing application.

## What I Learned

- Understanding image classification.
- Learning about malaria parasite detection.
- Exploring machine learning for healthcare applications.
- Improving my Python and GitHub skills.

## Disclaimer

This project is developed for educational and learning purposes. Its predictions should not be considered a medical diagnosis or a replacement for professional laboratory examination.
