#  WORD REVERSAL

def reverse_words(sentence):
    """Reverses a words."""
    words=sentence.split()
    reverse_words=words[::-1]
    reverse_sentence=" he".join(reverse_words)
    return reverse_sentence

def main():
    sentence = input("Enter a sentence: ")
    reverse_sentence=reverse_words(sentence)
    print("Reversed sentence: ", reverse_sentence)

if __name__ == "__main__":
    main()