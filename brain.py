def reply(message):
    text = message.lower().strip(" .,!?")

    memory = {}
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

    if text.startswith("my name is "):
        name = message.strip()[11:].strip(" .,!?")
        memory["name"] = name
        return f"Nice to meet you, {name}!" # name memory

    if replies:
        return " ".join(replies) # multi reply

    return f"You said: {message}" # echo fallback

if __name__ == "__main__":
    message = input("message: ")
    print("chatterbox:", reply(message))
