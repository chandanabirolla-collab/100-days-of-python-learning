import random
import string

# Ask user whether they want to Code (1) or Decode (2)
choice = input("Type 1 to Code or 2 to Decode: ")
message = input("Enter your message: ")

words = message.split(" ")  # Split sentence into words

# ---------------- CODING ----------------
if choice == "1":
    coded_words = []
    for word in words:
        if len(word) >= 3:
            # 1. Take 3 random letters for start and end
            r1 = "abc"
            r2 = "xyz"
            # 2. Move first letter to the end, then add random letters
            new_word = r1 + word[1:] + word[0] + r2
            coded_words.append(new_word)
        else:
            # If word is less than 3 letters, just reverse it
            coded_words.append(word[::-1])

    print("Secret Code:", " ".join(coded_words))

# ---------------- DECODING ----------------
elif choice == "2":
    decoded_words = []
    for word in words:
        if len(word) >= 3:
            # 1. Remove 3 letters from start and 3 from end
            core = word[3:-3]
            # 2. Move the last letter back to the front
            original = core[-1] + core[:-1]
            decoded_words.append(original)
        else:
            # If word is less than 3 letters, reverse it back
            decoded_words.append(word[::-1])

    print("Decoded Message:", " ".join(decoded_words))