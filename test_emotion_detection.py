"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import (
    EMOTION_KEYS,
    WATSON_URL,
    emotion_detector,
)


def make_response(scores, status_code=200):
    """Build a mock Watson API response."""
    response = Mock()
    response.status_code = status_code
    response.json.return_value = {
        "emotionPredictions": [{"emotion": scores}]
    }
    return response


class TestEmotionDetector(unittest.TestCase):
    """Test output format, dominant emotion, and error handling."""

    def test_anger_is_dominant(self):
        scores = {
            "anger": 0.8, "disgust": 0.1, "fear": 0.05,
            "joy": 0.02, "sadness": 0.03,
        }
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=make_response(scores),
        ):
            result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_joy_is_dominant(self):
        scores = {
            "anger": 0.02, "disgust": 0.01, "fear": 0.03,
            "joy": 0.9, "sadness": 0.04,
        }
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=make_response(scores),
        ):
            result = emotion_detector("I am delighted")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_all_five_scores_are_returned(self):
        scores = {
            "anger": 0.1, "disgust": 0.2, "fear": 0.3,
            "joy": 0.25, "sadness": 0.15,
        }
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=make_response(scores),
        ):
            result = emotion_detector("Test sentence")
        self.assertEqual(set(EMOTION_KEYS), set(scores))
        self.assertEqual(set(EMOTION_KEYS) | {"dominant_emotion"}, set(result))

    def test_blank_input_returns_empty_result_without_request(self):
        with patch(
            "EmotionDetection.emotion_detection.requests.post"
        ) as post:
            result = emotion_detector("   ")
        post.assert_not_called()
        self.assertIsNone(result["dominant_emotion"])
        self.assertTrue(all(result[key] is None for key in EMOTION_KEYS))

    def test_http_400_returns_empty_result(self):
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=make_response({}, status_code=400),
        ) as post:
            result = emotion_detector("invalid request")
        post.assert_called_once()
        self.assertEqual(post.call_args.args[0], WATSON_URL)
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
