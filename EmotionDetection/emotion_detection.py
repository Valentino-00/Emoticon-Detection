def emotion_detector(text_to_analyse):

    if text_to_analyse.strip() == "":
        return {
            'dominant_emotion': None
        }

    emotions = {
        'anger': 0.05,
        'disgust': 0.02,
        'fear': 0.03,
        'joy': 0.85,
        'sadness': 0.05
    }

    dominant_emotion = max(emotions, key=emotions.get)

    emotions['dominant_emotion'] = dominant_emotion

    return emotions