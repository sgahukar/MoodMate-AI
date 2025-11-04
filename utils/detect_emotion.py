# utils/detect_emotion.py
import re

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower().strip()

def predict_emotion(text):
    text = clean_text(text)

    emotion_keywords = {
        "Happy": ["happy", "joy", "delighted", "cheerful", "glad", "great", "awesome", "good", "excited"],
        "Sad": ["sad", "unhappy", "depressed", "down", "cry", "lonely", "miserable", "heartbroken"],
        "Angry": ["angry", "mad", "furious", "irritated", "annoyed", "rage", "frustrated"],
        "Fear": ["afraid", "scared", "fear", "terrified", "anxious", "nervous", "worried"],
        "Surprise": ["surprised", "shocked", "amazed", "astonished", "startled"],
        "Disgust": ["disgusted", "gross", "nauseous", "sick", "repulsed"],
        "Confused": ["confused", "uncertain", "unsure", "puzzled", "lost"],
        "Relaxed": ["calm", "peaceful", "relaxed", "comfortable", "chill", "content"],
        "Love": ["love", "affection", "caring", "fond", "adore", "romantic", "sweetheart"],
        "Hopeful": ["hope", "optimistic", "positive", "looking forward", "expecting", "inspired"],
        "Lonely": ["lonely", "alone", "isolated", "abandoned", "forsaken"],
        "Guilty": ["guilty", "regret", "remorse", "sorry", "ashamed"],
        "Proud": ["proud", "accomplished", "successful", "achieved", "victorious"],
        "Jealous": ["jealous", "envious", "envy", "covet", "resentful"],
        "Bored": ["bored", "uninterested", "dull", "monotonous", "tired"],
        "Embarrassed": ["embarrassed", "awkward", "ashamed", "self-conscious", "cringe"],
        "Grateful": ["grateful", "thankful", "appreciative", "blessed"],
        "Curious": ["curious", "interested", "wondering", "inquiring", "intrigued"],
        "Tired": ["tired", "exhausted", "sleepy", "fatigued", "weary"],
        "Neutral": ["okay", "fine", "normal", "alright", "neutral"]
        
    }

    for emotion, keywords in emotion_keywords.items():
        if any(word in text for word in keywords):
            return emotion

    return "Neutral"
