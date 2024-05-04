import os
import streamlit as st
from AI_Text_Detection.pipeline.Predict_pipeline import PredictPipeline
from AI_Text_Detection.utils.common import predict_class_aws
from dotenv import load_dotenv

load_dotenv()

Lambda_api_url = os.getenv("LAMBDA_API_URL")

def clear_text():
    st.session_state["text"] = ""

def main():
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

if __name__ == "__main__":
    main()
