def reply(message):
    text = message.lower().strip(" .,!?")

    replies = []

    if any(word in text.split() for word in {"hi", "hello", "hey"}):
        replies.append("heya!")

    if any(phrase in text for phrase in {
        "who are you",
        "what are you",
        "what do you do",
        "tell me about yourself",
    }):
        replies.append(
            "i’m xilv's chatterbox, a rule-based chatbot for hack club's YSWS crescent."
        )

    if replies:
        return " ".join(replies)

    return f"You said: {message}" # echo fallback

if __name__ == "__main__":
    message = input("message: ")
    print("chatterbox:", reply(message))
