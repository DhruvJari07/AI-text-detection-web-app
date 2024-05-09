# AI Text-Image Detection App

This repository contains an AI Text-Image Detection app that can determine whether a given input, either text or image, was generated by an AI model or not.

## Functionality

The AI Text-Image Detection app provides the following functionality:

- **Text Detection:** Users can input text, and the app analyzes it to determine whether it was generated by an AI model or not.
- **Image Detection:** Users can upload an image, and the app performs image analysis to detect whether the image was generated by an AI model or not.

## Model's Used:
Three different models are used, which are as follows:

- **Traditional ML Model (Text):** This model was trained using ensemble model of traditional ML algorithms such as RandomForestClassifier, Linear SVC, Naive Bayes etc.
- **Finetuned DistilBert Model (Text):** The transformer based deep learning model was fine-tuned on task specific data to detect AI generated text.
- **Finetuned ViT Model (Image):** The vision transformer based deep learning model was fine-tuned on task specific data to detect AI generated images.

## Architecture

The AI Text-Image Detection app was deployed using AWS. The following architecture shows each components used and utilized for different models for training as well as deployement:

![Architecture](media/final_architecture_AI_detection.jpg)

- **Frontend:** The user interface where users can input text or upload images for analysis.
- **Backend API:** Handles incoming requests from the frontend and communicates with the AI model for analysis.
- **AI Model:** Utilizes state-of-the-art natural language processing (NLP) and computer vision (CV) techniques to analyze text and images and determine whether they were generated by AI or not.
- **Database (Optional):** Stores analysis results and user interactions for future reference or analytics.

## Demo

Check out the following video demo to see the AI Text-Image Detection app in action:

![AI Text-Image Detection Demo](media/Ai_detection_app_demo.mp4)

Click on the image above to watch the demo video.






