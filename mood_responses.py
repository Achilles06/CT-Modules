# mood_responses.py

def mood_response(mood):
    mood = mood.lower()
    responses = {
        'happy': "That's great to hear! Keep smiling!",
        'sad': "I'm sorry you're feeling sad. Things will get better.",
        'excited': "That's awesome! Enjoy the excitement!",
        'angry': "Take a deep breath. It's okay to feel angry sometimes.",
        'bored': "Maybe try something new to spice things up!",
        'tired': "Get some rest. You deserve it.",
        'anxious': "Take it one step at a time. You're doing great.",
    }

    return responses.get(mood, "I don't know that mood, but I hope you have a good day!")
