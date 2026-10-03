memory = {}

def reply(message):
    text = message.lower().strip(" .,!?")

    replies = []

    if any(word in text.split() for word in {"hi", "hello", "hey"}):
        replies.append("heya!") # greeting

    if any(phrase in text for phrase in {
        "who are you",
        "what are you",
        "what do you do",
        "tell me about yourself",
    }):
        replies.append(
            "i’m xilv's chatterbox, a rule-based chatbot for hack club's YSWS crescent." # introduction
        )

    name = None

    if "my name is " in text:
        name = message.strip()[11:].strip(" .,!?")
    elif "i'm " in text:
        name = message.strip()[4:].strip(" .,!?")

    if name:
        memory["name"] = name
        return f"nice to meet you, {name}!" # name memory

    if "what's my name" in text or "what is my name" in text:
        if "name" in memory:
            replies.append(f"your name is {memory['name']}!")
        else:
            replies.append("i don't know your name yet. what should I call you?")

    if replies:
        return " ".join(replies) # multi reply

    return f"You said: {message}" # echo fallback

if __name__ == "__main__":
    while True:
        message = input("message (or quit): ")
        if message.lower().strip() == "quit":
            break
        print("chatterbox:", reply(message))
