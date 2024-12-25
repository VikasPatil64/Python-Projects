def word_counter(sentence):
    word_counts = {}
    words = sentence.split()
    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def main():
    sentence = input("Enter a sentence to count word occurrences: ")  # Corrected "sentecnce" to "sentence"
    word_counts = word_counter(sentence)
    
    print("\nWord Occurrences:")  # Removed extra space in the output
    for word, count in word_counts.items():
        print(f"{word}: {count}")
        
if __name__ == "__main__":
    main()
