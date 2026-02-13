def format_emotion_output(response):
    dominant = response.get("dominant_emotion")

    if dominant is None:
        return "Invalid text! Please try again."

    return f"The dominant emotion is: {dominant}"
