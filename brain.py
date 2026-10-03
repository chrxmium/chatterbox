import random

memory = {}

def reply(message):
    text = message.lower().strip(" .,!?")

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

    if replies:
        return " ".join(replies) # multi reply

    petname = None

    if "my pet's name is " in text:
        start = text.index("my pet's name is ") + len("my pet's name is ")
        petname = message[start:].strip(" .,!?")

    if petname:
        memory["petname"] = petname
        replies.append(f"okay. what am i meant to do with that? {petname}.") # pet name memory

    if "what's my pet's name" in text or "what is my pet's name" in text:
        if "petname" in memory:
            replies.append(f"you forgot your pet's name? you're a horrible owner. it's {memory['petname']}.")
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
