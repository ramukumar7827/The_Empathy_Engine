from flask import Flask, render_template, jsonify, request
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from huggingface_hub import InferenceClient
import os
# import pyttsx3
from gtts import gTTS
from pydub import AudioSegment
import uuid
load_dotenv()
app = Flask(__name__)
import os
from huggingface_hub import InferenceClient


def get_emotion(text):
    client = InferenceClient(
        provider="hf-inference",
        api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
    )

    result = client.text_classification(
        text,
        model="ProsusAI/finbert",
    )
    print(result)
    top_emotion=max(result, key=lambda x: x['score'])
    emotion=top_emotion['label']
    print(emotion)
    intensity=top_emotion['score']
    return emotion


AUDIO_FOLDER = "static/audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

def speak_with_emotion(text, sentiment):
    voice_params = {
        'rate':1.0,
        'volume':0
    }

    if sentiment=="positive":
        voice_params['rate']=1.2
        voice_params['volume']= +4

    elif sentiment=="negative":
        voice_params['rate']=0.9
        voice_params['volume']=1

    else:
        voice_params['rate']=1.0
        voice_params['volume']= 0

    base_path = os.path.join(
        AUDIO_FOLDER,
        f"{uuid.uuid4()}_base.mp3"
    )
    gTTS(text=text, lang="en").save(base_path)

    audio=AudioSegment.from_mp3(base_path)

    audio=audio+voice_params['volume']
    if voice_params['rate'] != 1.0:
        audio = audio.speedup(
            playback_speed=voice_params['rate']
        )

    final_path = os.path.join(
        AUDIO_FOLDER,
        f"{uuid.uuid4()}.mp3"
    )
    audio.export(final_path, format="mp3")

    return final_path



@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/generate", methods=["POST"])
def generate():
    text = request.form.get("text")
    emotion=get_emotion(text)

    audio_path = speak_with_emotion(text, emotion)

    return jsonify({
        "emotion": emotion,
        "audio_url": audio_path
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)