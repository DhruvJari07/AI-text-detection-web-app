FROM python:3.10-slim

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit runs on
EXPOSE 8501

# Command to run the Streamlit application
CMD ["streamlit", "run", "app.py"]