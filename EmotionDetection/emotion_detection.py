"""Watson NLP emotion detection with formatted output and error handling."""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTION_KEYS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return the standard empty result used when analysis fails."""
    result = {emotion: None for emotion in EMOTION_KEYS}
    result["dominant_emotion"] = None
    return result


def emotion_detector(text_to_analyze):
    """Return five emotion scores and the dominant emotion.

    Empty text, unsuccessful HTTP responses, malformed responses, and
    request errors return None values rather than raising an exception.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            WATSON_URL,
            json=payload,
            headers=headers,
            timeout=30,
        )
        if response.status_code != 200:
            return _empty_result()

        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]
        scores = {emotion: emotions[emotion] for emotion in EMOTION_KEYS}
        scores["dominant_emotion"] = max(scores, key=scores.get)
        return scores
    except (
        requests.RequestException,
        ValueError,
        KeyError,
        IndexError,
        TypeError,
    ):
        return _empty_result()
