import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from clipdigest.load_video import download
from clipdigest.audio2text import a2t
from clipdigest.get_compound import chem
import langchain
from langchain.cache import InMemoryCache
langchain.llm_cache = InMemoryCache()


# Define the main Streamlit app
def main():
    # Set the page title
    st.title('Clip Digest')
    st.image("img/logo.png", use_column_width=True)

    # Add a text input widget
    video_link = st.text_input('Video link', '')
    audio_path = st.text_input('Path to audio', '')

    # Add a button widget
    if st.button('Go'):
        # Get the input arguments
        if video_link != '':
            download(video_link)
            audio_path = "data/audio.mp4"
        video_text, summary, question = a2t(audio_path)
        st.markdown(f"Summary: \n {summary}")
        st.text(f"Questions: \n {question}")
        chem(video_text)


# Run the main function
if __name__ == '__main__':
    main()