import streamlit as st
from AI_Text_Detection.pipeline.Predict_pipeline import PredictPipeline

def main():
    # Set title and description
    st.title("AI & Human Text Classification")
    st.write("To detect if your text is written by human or AI, enter your text below.")

    # Text input
    user_input = st.text_area("Enter your text here:", "")

    # Predict button
    if st.button("Predict"):
        # Instantiate PredictPipeline
        predictor = PredictPipeline()

        # Make prediction
        prediction = predictor.predict([user_input])

        # Display prediction result
        st.write(f"Prediction: Your text is **{prediction}** generated.")


if __name__ == "__main__":
    main()
