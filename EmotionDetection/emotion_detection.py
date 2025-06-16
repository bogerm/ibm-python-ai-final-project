import requests
import json

def emotion_detection(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 200:
        data = json.loads(response.text)
        emotion_scores = data["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        result = emotion_scores.copy()
        result["dominant_emotion"] = dominant_emotion
    else
        result = 'Error'
    return result