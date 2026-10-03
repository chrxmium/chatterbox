import random
import re

memories = {}
pets_by_user = {}

def reply(message, user_id="local"):
    text = message.lower().strip(" .,!?")
    memory = memories.setdefault(user_id, {})
    pets = pets_by_user.setdefault(user_id, {})
    replies = []

    if any(word in text.split() for word in {"hi", "hello", "hey"}):
        replies.append("oh, hi. took you long enough.") # greeting

    if any(phrase in text for phrase in {
        "who are you",
        "what are you",
        "what do you do",
        "tell me about yourself",
    }):
        replies.append(
            "ugh. i’m xilv's chatterbox, a rule-based chatbot for hack club's YSWS crescent. is that it?" # introduction
        )

    name = None

    if "my name is " in text:
        start = text.index("my name is ") + len("my name is ")
        name = message[start:].strip(" .,!?")
    elif "i'm " in text:
        start = text.index("i'm ") + len("i'm ")
        name = message[start:].strip(" .,!?")

    if name:
        memory["name"] = name
        replies.append(f"fine. nice to meet you, {name}, i guess.") # name memory

    if "what's my name" in text or "what is my name" in text:
        if "name" in memory:
            replies.append(f"shouldn't you know your own name? your name is {memory['name']}.")
        else:
            replies.append("why would i know your name? stupid question.") # name inquiry

    petname = None

    match = re.search(r"my (.+?)'s name is (.+)", message, re.IGNORECASE)
    if match:
        animal = match.group(1).strip().lower()
        petname = match.group(2).strip(" .,!?")
        pets[animal] = petname
        replies.append(f"oh, your {animal} is called {petname}. cute, i guess.")

    match = re.search(r"my (.+?) is called (.+)", message, re.IGNORECASE)
    if match:
        animal = match.group(1).strip().lower()
        petname = match.group(2).strip(" .,!?")
        pets[animal] = petname
        replies.append(f"oh, your {animal} is called {petname}. cute, i guess.")

    if petname:
        replies.append(f"okay. cool. {petname}.") # pet name memory

    pet_question = re.search(
        r"what(?:'|’)s my (.+?)(?:'|’)s name|what is my (.+?)(?:'|’)s name",
        text,
    )
    if pet_question:
        animal = (pet_question.group(1) or pet_question.group(2)).strip().lower()
        if animal in pets:
            replies.append(f"your {animal}'s name is {pets[animal]}.")
        else:
            replies.append("why would i know your pet's name? stupid question.") # pet name inquiry

    if replies:
        return " ".join(replies) # multi reply

    return random.choice([
        "i guess, bro.",
        "okay? and what am i meant to do with that?",
        "fascinating. absolutely life-changing.",
        "sure, if you say so.",
    ]) # fallback response

if __name__ == "__main__":
    while True:
        message = input("message (or quit): ")
        if message.lower().strip() == "quit":
            break
        print("chatterbox:", reply(message))
