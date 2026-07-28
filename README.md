# Korean Service Phrase Coach

A Streamlit app for practicing polite Korean phrases for restaurants, spas, payments, and general service interactions.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The app uses the browser's Korean speech synthesis voice for pronunciation playback. Voice recording uses Streamlit's built-in audio input, so the browser may ask for microphone permission.
