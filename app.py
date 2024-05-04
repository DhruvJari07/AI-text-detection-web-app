import os
import streamlit as st
from AI_Text_Detection.pipeline.Predict_pipeline import PredictPipeline
from AI_Text_Detection.utils.common import predict_class_aws
from dotenv import load_dotenv

load_dotenv()

Lambda_api_url = os.getenv("LAMBDA_API_URL")

def main():
    # Set title and description
    st.title("AI & Human Text Classification")
    st.write("To detect if your text is written by human or AI, enter your text below.")

    # Text input
    user_input = st.text_area("Enter your input text here:", "", height=300)

    # Model selection
    selected_model = st.selectbox("Select Model", ["Traditional ML Model", "Finetuned DistilBert Model"])


    # Predict button
    if st.button("Predict"):
        with st.spinner("Predicting..."):
                if selected_model == "Traditional ML Model":
                        prediction = PredictPipeline().predict([user_input])
                elif selected_model == "Finetuned DistilBert Model":
                        prediction = predict_class_aws(Lambda_api_url, user_input)
                
                # Display prediction result
                st.write(f"Prediction: Your text is **{prediction}** generated.")


if __name__ == "__main__":
    main()
