"""Emotion detection using IBM Watson NLP API."""

import json
import requests

def emotion_detection(text_to_analyse):
    """Sends input text to Watson NLP Emotion API and returns emotion scores and dominant emotion.

    Args:
        text_to_analyse (str): The text to analyze.

    Returns:
        dict or None: A dictionary with emotion scores and dominant emotion, or None on error.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    try:
        response = requests.post(url, json=myobj, headers=header, timeout=10)
    except requests.exceptions.RequestException:
        return None  # Handle network errors, timeouts, etc.

    if response.status_code == 200:
        data = json.loads(response.text)
        emotion_scores = data["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        result = emotion_scores.copy()
        result["dominant_emotion"] = dominant_emotion
    elif response.status_code == 400:
        result = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
    else:
        result = None

    return result
    