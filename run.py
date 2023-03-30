import streamlit as st
from clipdigest.load_video import download
from clipdigest.audio2text import a2t
from clipdigest.get_compound import chem
import langchain
from langchain.cache import InMemoryCache
import mols2grid
import streamlit.components.v1 as components
langchain.llm_cache = InMemoryCache()



# Define the main Streamlit app
def main():
    # Set the page title
    st.title('ClipDigest')
    st.image("img/logo.png", width=400, use_column_width=False)

    # Add a text input widget
    video_link = st.text_input('Video link', '')
    audio_path = st.text_input('Path to audio', '')

    # Add a button widget
    if st.button('Go'):
        # Get the input arguments
        if video_link != '':
            download(video_link)
            audio_path = "data/audio.mp4"
        video_text, summary, question, refer = a2t(audio_path)
        st.markdown(f"Summary:")
        st.markdown(summary)
        st.markdown(f"Questions: \n {question}")
        st.markdown(f"References: \n {refer}")
        df = chem(video_text)
        ay = []
        for i in df['label']:
            url = df.loc[df['label'] == i]['link'].values[0]
            ay.append(f"[{i}]({url})")
            
            #st.text(df.loc[df['label'] == i]['iupac'].values[0])
            #st.text(df.loc[df['label'] == i]['SMILES'].values[0])
        if ay:
            st.markdown('Chemical compounds:')
        string = ', '.join(ay)
        st.markdown(string)
        raw_html = mols2grid.display(df, mapping={"smiles":"SMILES"})._repr_html_()
        components.html(raw_html, width=900, height=900, scrolling=True)

# Run the main function
if __name__ == '__main__':
    main()
