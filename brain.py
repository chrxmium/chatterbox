def reply(message):
    text = message.lower().strip(" .,!?")

    if text in {"hi", "hello", "hey"}:
        return "heya!"

    return f"You said: {message}"

if __name__ == "__main__":
    message = input("message: ")
    print("chatterbox:", reply(message))
