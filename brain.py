def reply(message):
    return f"You said: {message}"

if __name__ == "__main__":
    message = input("message: ")
    print("chatterbox:", reply(message))