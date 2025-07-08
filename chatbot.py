import streamlit as st
import pandas as pd
from google import genai

api_key = st.secrets["gemini"]["google_api_key"]
client = genai.Client(api_key=api_key)

# response = client.models.generate_content(
#     model='gemini-2.0-flash-001', contents='Why is the sky blue?'
# )
# print(response.text)

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
    # response = client.chat.completions.create(model = "gpt-3.5-turbo",
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=f"Act like this {role} and i want you to  answer this {question}")

    # print(response.text)
    st.write(response.text)

    
    # messages = [
    #     {"role":"system","content":f"you are {character}. Answer with their personality"},
    #     {"role":"user","content":question}
    # # ]
    # )
    # print(response)
    # st.write(response.choices[0].message.content)

#  def callOpenai():
#     print()


    # ChatCompletion(id='chatcmpl-BpOCyxKXPAsQL9KxCPAbiYGPMuhde', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="Oooh ooh, hello! I'm excited to chat with you, let's have some fun!", refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1751587484, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=22, prompt_tokens=22, total_tokens=44, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))