spam_phrases = ["make a lot of money", "buy now", "subscribe this", "click this"]
user_input = input("Enter your query: ").lower()  # Convert input to lowercase

# Check if any spam phrase is present in the user input
if any(phrase in user_input for phrase in spam_phrases):
    print("This is a spam message")
else:
    print("This is not a spam message")