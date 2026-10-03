def reply(message):
    text = message.lower().strip(" .,!?")

    if text in {"hi", "hello", "hey"}:
        return "heya!" # greeting

    if any(phrase in text for phrase in {
        "who are you",
        "what are you",
        "what do you do",
        "tell me about yourself",
    }):
        return "i’m xilv's chatterbox, a rule-based chatbot for hack club's YSWS crescent."

    return f"You said: {message}" # echo fallback

if __name__ == "__main__":
    message = input("message: ")
    print("chatterbox:", reply(message))
