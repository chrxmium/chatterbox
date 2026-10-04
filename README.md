hiya this is like my first code project ever that i've shipped so yay!

chatterbox is a small, rule-based discord chatbot for hack club's ysws crescent. it does not use an llm.

## features

- replies to greetings and introduction questions
- remembers each user's name
- remembers pet names by animal and user
- varying fallback replies when it doesn't recognize a message
- shows a typing indicator for a random 3–7 seconds
- only responds in the configured discord channel

## memory

memories are stored in per-user dictionaries while the bot is running. they are separated by discord user id, but they reset when the bot restarts. (no persistent database)

## how it works

chatterbox checks messages against simple text patterns and keywords. it saves matching names in memory and chooses a random fallback reply when no pattern matches.

## limitations

chatterbox only recognizes the phrases its rules cover. it may misunderstand messages or respond awkwardly.
