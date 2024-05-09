import os
import streamlit as st
import requests
import json
#from dotenv import load_dotenv
from AI_Text_Detection.pipeline.Predict_pipeline import PredictPipeline
from AI_Text_Detection.utils.common import predict_class_aws


#load_dotenv()

Lambda_api_url = os.getenv("LAMBDA_API_URL")
LAMBDA_IMAGE_ENDPOINT = os.getenv("LAMBDA_API_IMAGE_ENDPOINT")

def clear_text():
    st.session_state["text"] = ""

def main():
    st.sidebar.title("Choose Detection Type")
    app_mode = st.sidebar.radio("",
        ["Text Detection", "Image Detection"])

    if app_mode == "Text Detection":
        text_detection()
    elif app_mode == "Image Detection":
        image_detection()

def text_detection():
    # Set title and description
    st.title("AI & Human Text Classification")
    st.write("To detect if your text is written by human or AI, enter your text below.")

    # Text input
    user_input = st.text_area("Enter your input text here:", "", height=250, key='text')

    # Model selection
    selected_model = st.selectbox("Select Model", ["Traditional ML Model", "Finetuned DistilBert Model"])

    predict_col, clear_col, _, _, _, _, _ = st.columns([1,1,1,1,1,1,1], gap="small")

    # Predict button
    if predict_col.button("Predict", key="predict"):
        with st.spinner("Predicting..."):
                if selected_model == "Traditional ML Model":
                        prediction = PredictPipeline().predict([user_input])
                elif selected_model == "Finetuned DistilBert Model":
                        prediction = predict_class_aws(Lambda_api_url, user_input)
                
                # Display prediction result
                st.write(f"Prediction: Your text is **{prediction}** generated.")

    clear_col.button("Clear", key="clear", on_click=clear_text)

def image_detection():
    st.title("Deepfake Detection App")
    st.write("Upload an image to detect if your image was created using AI or not")
    
    if 'uploaded_image' not in st.session_state:
        st.session_state.uploaded_image = None
    # File uploader for image
    uploaded_image = st.file_uploader("Upload an image", type=['jpg', 'jpeg'])

    if uploaded_image is not None:
        # Display uploaded image
        st.image(uploaded_image, caption='Uploaded Image', width=300)
        st.session_state.uploaded_image = uploaded_image
        
        # Send image to API on button click
        if st.button('Predict'):
            try:
                image_data = st.session_state.uploaded_image.read()

                # Set the headers for the request
                headers = {"Content-Type": "image/jpeg"}

                # Send the image data as binary in the request
                response = requests.post(LAMBDA_IMAGE_ENDPOINT, data=image_data, headers=headers) # type: ignore
                results = json.loads(response.text)
                # Print the response
                for result in results:
                    if result['score'] >= 0.5:
                        prediction = result['label']
                    # Display response from API
                        st.write(f"Your image is {prediction}")

            except Exception as e:
                st.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
