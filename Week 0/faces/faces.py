# Set up the question
def main():
    chat = input("Are you Happy or Sad? ")
    chat = convert(chat)
    print(chat)

# Convert the answer and return with emojis if given
def convert(response):
    response = response.replace(":)", "🙂").replace(":(", "🙁")
    return response

main()
