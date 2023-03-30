How to run this code

1. Configure Python environment, we suggest you use Python3.8

2. Install openai and set the openai key in the terminal
```
export OPENAI_API_KEY=<your_api_key>
```
You can find your openai api key following [this link](https://elephas.app/blog/how-to-create-openai-api-keys-cl5c4f21d281431po7k8fgyol0).

3. Install whisper following [this](https://github.com/openai/whisper)

4. Install the packages required: loguru, pytube, pubchempy, pandas, streamlit, langchain in your local python environment

5. Install chemdataextractor by 
```
pip install chemdataextractor
cde data download
```

6. Install this repo
```
pip install -e .
```

7. Run the program by `streamlit run run.py` 
