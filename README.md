# Final Project – Emotion Detector

## Overview
A Python web application that analyzes customer feedback with the Watson NLP EmotionPredict service and reports five emotion scores: anger, disgust, fear, joy, and sadness, along with the dominant emotion.

## Features
- Watson NLP emotion detection
- Consistent dictionary output with five scores and `dominant_emotion`
- Python package named `EmotionDetection`
- Flask web interface
- Blank-input and unsuccessful-service-response handling
- Unit tests using mocked Watson responses
- Pylint configuration and commands

## Project structure
```text
oaqjp-final-project-emb-ai/
├── 2a_emotion_detection/
│   └── emotion_detection.py
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   ├── style.css
│   └── mywebscript.js
├── templates/
│   └── index.html
├── test_emotion_detection.py
├── server.py
├── requirements.txt
└── README.md
```

## Setup
Python 3.9+ is recommended.

```bash
python3 -m pip install -r requirements.txt
```

## Run tests
```bash
python3 -m unittest -v test_emotion_detection.py
```

The unit tests mock the remote Watson response, so they do not require network access. To test the live service, run the app and submit text in the browser.

## Run the Flask application
```bash
python3 server.py
```
Then open <http://127.0.0.1:5000/>.

## Test the package
```bash
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
```

## Static analysis
```bash
python3 -m pylint server.py
```

## Coursera submission notes
The assignment requires real terminal output and two screenshots. Run the commands in the Coursera lab and paste the actual terminal output into the corresponding assessment fields. Capture:
- `6b_deployment_test.png`: the running interface with submitted text and visible results.
- `7c_error_handling_interface.png`: the interface showing the blank-input validation message.

Do not submit example or fabricated terminal output as if it were captured from a real run.

## Original starter repository
https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai
