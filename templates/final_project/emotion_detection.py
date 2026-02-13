import requests
import json

def emotion_detector(text_to_analyse):
    # Return None if text is empty
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # API endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Prepare the payload
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}

    # Send the request
    response = requests.post(url, json=payload, headers=headers)

    # Parse JSON
    result = response.json()

    # Extract emotions
    emotions = result["emotionPredictions"][0]["emotion"]

    # Find dominant emotion
    dominant_emotion = max(
        emotions,
        key=emotions.get
    )

    # Prepare output
    return {
        "anger": emotions.get("anger"),
        "disgust": emotions.get("disgust"),
        "fear": emotions.get("fear"),
        "joy": emotions.get("joy"),
        "sadness": emotions.get("sadness"),
        "dominant_emotion": dominant_emotion
    }
