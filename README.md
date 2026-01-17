# Emotion-Aware Text-to-Speech Web Application

This web application that detects the emotional sentiment of user-provided text using the Hugging Face API for sentiment analysis and generates emotion-aware speech output. The speech characteristics such as speed and volume are adjusted dynamically based on the detected emotion.





## Features
- Emotion detection using Hugging Face Inference API
- Sentiment classification using the ProsusAI/finbert model
- Emotion-aware audio generation
- Dynamic speech rate and volume control
- REST API for text-to-speech generation
- Web interface by flask

---

## Architecture

1. User submits text through the web interface
2. Text is sent to the Hugging Face Inference API
3. Sentiment is classified into positive, negative, or neutral
4. Highest-confidence emotion is selected
5. Audio is generated using gTTS
6. Audio properties are modified using pydub
7. Final audio file is returned to the client

##  Setup & Installation
  ### 1.Clone the Repository
  ### 2.Install Dependencies
  ### 3.pip install -r requirements.txt
  ###4.API Key Configuration
      Create a .env file in the root directory:
      HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
  ###5.Run the Application
       python app.py

---

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/df89f178-487b-4ab3-8ec0-60c15bd10520" />

