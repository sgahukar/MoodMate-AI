# utils/response_generator.py
import random

def generate_response(emotion):
    responses = {
        "Happy": [
            "That's wonderful! 😊 Keep that positive energy flowing!",
            "I'm so glad to hear you're happy today! 🌞"
        ],
        "Sad": [
            "I'm really sorry to hear that 💙. Want me to cheer you up with something?",
            "It’s okay to feel sad sometimes — I’m here for you 🤗."
        ],
        "Angry": [
            "I understand how you feel 😤. Maybe take a few deep breaths — it might help.",
            "That sounds frustrating. Do you want to talk about what made you angry?"
        ],
        "Fear": [
            "It’s natural to feel afraid sometimes 😔. You're not alone in this.",
            "Take a deep breath — facing fears starts small, but you're stronger than you think 💪."
        ],
        "Surprise": [
            "Oh wow! 😲 That must have been unexpected!",
            "That sounds surprising — tell me what happened!"
        ],
        "Disgust": [
            "Yikes 😣 that must have been unpleasant.",
            "Ugh, that doesn’t sound nice. Want to vent about it?"
        ],
        "Confused": [
            "Hmm 🤔 sounds confusing. Maybe I can help you think it through?",
            "It’s okay to be unsure — clarity will come soon!"
        ],
        "Relaxed": [
            "That’s great 🌿! Peace of mind is so valuable.",
            "Love to hear that you’re feeling calm and relaxed 😌."
        ],
        "Love": [
            "Aww 💖 that's beautiful! Love truly makes everything brighter.",
            "How sweet! Cherish those feelings of love and connection 💞."
        ],
        "Hopeful": [
            "That’s the spirit 🌈 — stay hopeful and great things will happen!",
            "Optimism looks great on you ✨ keep believing in better days."
        ],
        "Lonely": [
            "I'm sorry you're feeling lonely 💔. Remember, you're never really alone.",
            "That sounds tough. Talking helps — I'm right here with you 🤍."
        ],
        "Guilty": [
            "Guilt can be heavy 😞, but remember — we all make mistakes.",
            "Try forgiving yourself — growth comes from learning, not perfection 🌱."
        ],
        "Proud": [
            "You should be proud! 🎉 Celebrate your wins, big or small.",
            "That’s amazing 👏 — keep believing in your potential!"
        ],
        "Jealous": [
            "It’s okay to feel jealous sometimes — it just means you care.",
            "Try turning that envy into motivation 💪 — you’ve got this!"
        ],
        "Bored": [
            "Feeling bored? Let’s find something fun to spark your interest 🎨.",
            "Boredom can be an invitation to try something new — what do you like doing?"
        ],
        "Embarrassed": [
            "It’s okay, we all have embarrassing moments 😅.",
            "Don’t worry — everyone’s been there! Time heals awkwardness quickly 😄."
        ],
        "Grateful": [
            "That’s wonderful 🙏. Gratitude brings more peace and positivity 🌸.",
            "Feeling grateful makes the heart lighter and happier 💫."
        ],
        "Curious": [
            "Curiosity is the first step to discovery 🧠 — keep exploring!",
            "That’s great! Let’s dive into what you’re curious about 🔍."
        ],
        "Tired": [
            "You sound exhausted 😴. Rest is not a reward, it’s a necessity.",
            "Maybe take a short break or nap — you deserve some recharge time 🌙."
        ],
        "Neutral": [
            "Got it. 😊 Tell me more — how was your day?",
            "Okay. Let’s talk about something that interests you today!"
        ]
    }

    default = ["I'm here to listen. Tell me more about how you're feeling 💬."]
    return random.choice(responses.get(emotion, default))
