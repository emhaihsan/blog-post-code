import gradio as gr
import assemblyai as aai
from translate import Translator
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import uuid
from pathlib import Path
from dotenv import dotenv_values

config = dotenv_values(".env")

ELEVENLABS_API_KEY = config["ELEVENLABS_API_KEY"]
ASSEMBLYAI_API_KEY = config["ASSEMBLYAI_API_KEY"]


def voice_to_voice(audio_file):
    transcription_response = audio_transcription(audio_file)

    if transcription_response.status == aai.TranscriptStatus.error:
        raise gr.Error(transcription_response.error)
    else:
        text =  transcription_response.text

    es_translation, ar_translation, ja_translation  = text_translation(text)

    es_audio_path = text_to_speech(es_translation)
    ar_audio_path = text_to_speech(ar_translation)
    ja_audio_path = text_to_speech(ja_translation)

    es_path = Path(es_audio_path)
    ar_path = Path(ar_audio_path)
    ja_path = Path(ja_audio_path)

    return es_path, ar_path, ja_path

def audio_transcription(audio_file):
    
    aai.settings.api_key = ASSEMBLYAI_API_KEY

    transcriber = aai.Transcriber()
    transcription = transcriber.transcribe(audio_file)

    return transcription

def text_translation(text):
    translator_es = Translator(from_lang="en", to_lang="es")
    es_text = translator_es.translate(text)

    translator_ar = Translator(from_lang="en", to_lang="ar")
    ar_text = translator_ar.translate(text)

    translator_ja = Translator(from_lang="en", to_lang="ja")
    ja_text = translator_ja.translate(text)

    return es_text, ar_text, ja_text

def text_to_speech(text: str) -> str:
    client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
    )
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2", # use the turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.5,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = f"{uuid.uuid4()}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path

audio_input = gr.Audio(
    sources=["microphone"],
    type="filepath"
)

demo = gr.Interface(
    fn=voice_to_voice,
    inputs=audio_input,
    outputs=[gr.Audio(label="Spanish"), gr.Audio(label="Arabic"), gr.Audio(label="Japanese")],
    title="Voice-to-Voice Translator",
    description="Voice-to-Voice",
)

if __name__ == "__main__":
    demo.launch()