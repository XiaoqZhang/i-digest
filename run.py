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
        print("The video link is : %s" %video_link)
        if video_link is True:
            download(video_link)
            audio_path = "data/audio.mp4"
        video_text, summary, question = a2t(audio_path)
        st.text(f"Summary: \n {summary}")
        st.text(f"Questions: \n {question}")
        chem(video_text)


        # perhaps go via serialized file, 
        # then the context does not explode 
    """
        if "svg" in result:
            # find the the filepath that ends with .svg
            match = re.search(r"/\S+\.svg", result)
            svg_path = match.group()
            st.image(svg_path, use_column_width=True)
        else:
            st.text(result)
    """

# Run the main function
if __name__ == '__main__':
    main()