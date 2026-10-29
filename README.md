# Final Project – Emotion Detector

## Project Overview
The Emotion Detector is a Python-based application that analyzes text and identifies the emotions expressed by the user. It uses the IBM Watson Natural Language Processing (NLP) library to detect emotions and determine the dominant emotion in the given text.

## Features
- Detects five emotions: anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion in the input text.
- Formats the results into a structured Python dictionary.
- Provides a web interface using Flask.
- Handles blank inputs and unsuccessful API responses.
- Includes unit tests to validate emotion detection functionality.
- Supports static code analysis using Pylint.

## Technologies Used
- Python
- IBM Watson NLP
- Flask
- Requests
- Unittest
- Pylint
- HTML, CSS, and JavaScript

## Project Structure
```text
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai
   ```

2. Install the required dependencies:

   ```bash
   python3 -m pip install requests flask pylint
   ```

3. Run the unit tests:

   ```bash
   python3 -m unittest -v test_emotion_detection.py
   ```

4. Start the Flask application:

   ```bash
   python3 server.py
   ```

5. Open the application in your browser at:

   ```text
   http://127.0.0.1:5000/
   ```

## Example

**Input:**
```text
I am really mad about this.
```

**Expected output format:**
```python
{
    "anger": 0.0,
    "disgust": 0.0,
    "fear": 0.0,
    "joy": 0.0,
    "sadness": 0.0,
    "dominant_emotion": "anger"
}
```

*Note: The emotion scores above are placeholders illustrating the output format. Actual scores are returned by the Watson NLP service.*

## Error Handling
The application validates user input and handles unsuccessful service responses. When the input is blank or the service returns an error, the application displays an appropriate error message.

## Testing
Unit tests validate the detection of anger, disgust, fear, joy, and sadness. Pylint is used to assess code quality and maintainability.

## Project Objective
The objective of this project is to demonstrate the development, testing, packaging, and Flask deployment of an AI-based emotion detection application using natural language processing.

## Repository
This project is based on the IBM Developer Skills Network final project repository:

https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai
