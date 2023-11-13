from openai import OpenAI
import streamlit as st



with st.sidebar:
    your_openai_key = st.text_input('Enter API Key', type="password")

client = OpenAI(api_key=your_openai_key)

my_text = st.text_input('Enter text')
download_name = st.text_input('Enter the file name to be downloaded')

option = st.sidebar.selectbox(
   "Choose voice:",
   ("alloy", "echo", "fable", "onyx", "nova", "shimmer"),
   index=5,


)

if(your_openai_key):
    if(my_text and download_name):
        
        response = client.audio.speech.create(
            model="tts-1",
            voice=option,
            input=my_text,
        )

        response.stream_to_file("speech_yay1.mp3")
        st.audio("speech_yay1.mp3")

        with open("speech_yay1.mp3", "rb") as f:
            data = f.read()

        st.download_button(label="Download now",data=data, file_name=download_name + ".mp3")

else:
    st.info("Enter API Key")
