import streamlit as st
import pandas as pd
# from google import genai
# from google.genai import types
import google.generativeai as genai
from elevenlabs.client import ElevenLabs
from elevenlabs import play


elevenlabs_api_key = st.secrets["elevenlabs_api_key"]
elevenlabs = ElevenLabs(
  api_key = elevenlabs_api_key
)
api_key = st.secrets["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # or gemini-1.5-pro

# audio_stream = elevenlabs.text_to_speech.stream(
#     text="This is a test",
#     voice_id="JBFqnCBsd6RMkjVDRZzb",
#     model_id="eleven_multilingual_v2"
# )
# audio_bytes = b"".join(audio_stream)
# st.audio(audio_bytes,format="audio/mpeg")

st.write("""
# MLB Chatbot 
""")


st.write("""
### Welcome to MLB Chatbot
""")

role = st.text_input("Who do you want your bot to be like")
question = st.text_area("Enter text to chat")

if question:
    st.write("Thanks for asking the question!")
    system_instructions=f"You are {role}"
    prompt = f"Act like this {role} and i want you to  answer this {question}"
    response = model.generate_content(prompt)
    st.write(response.text)
    audio_stream = elevenlabs.text_to_speech.stream(
        text=response.text,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2"
    )
    audio_bytes = b"".join(audio_stream)
    st.audio(audio_bytes,format="audio/mpeg")
    
    # ChatCompletion(id='chatcmpl-BpOCyxKXPAsQL9KxCPAbiYGPMuhde', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="Oooh ooh, hello! I'm excited to chat with you, let's have some fun!", refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1751587484, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=22, prompt_tokens=22, total_tokens=44, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))