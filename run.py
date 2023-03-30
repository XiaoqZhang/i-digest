import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from clipdigest.audio2text import a2t
from clipdigest.get_compound import chem
import langchain
from langchain.cache import InMemoryCache
langchain.llm_cache = InMemoryCache()


# Define the main Streamlit app
def main():
    # Set the page title
    st.title('Clip Digest')

    # Add a text input widget
    audio_path = st.text_input('Path to audio', '')

    # Add a button widget
    if st.button('Go'):
        # Convert the user input to a float
        video_text = a2t(audio_path)
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