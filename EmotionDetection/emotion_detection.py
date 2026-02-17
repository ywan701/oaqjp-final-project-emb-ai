import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url=url, json=payload, headers=headers)
    formatted_response = response.json()

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    predictions = formatted_response.get("emotionPredictions", [])
    emotions = predictions[0].get("emotion", {})

    anger_score = emotions.get("anger")
    disgust_score = emotions.get("disgust")
    fear_score = emotions.get("fear")
    joy_score = emotions.get("joy")
    sadness_score = emotions.get("sadness")

    dominant_emotion = max(emotions, key=emotions.get) if emotions else None

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }
