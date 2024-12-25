def is_anagram(string1, string2):
    # Remove spaces and convert to lowercase
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Check if sorted characters of both strings are equal
    return sorted(string1) == sorted(string2)

def main():
    print("Welcome to the Anagram Checker!")
    word1 = input("Enter the first word or phrase: ")
    word2 = input("Enter the second word or phrase: ")

    if is_anagram(word1, word2):
        print(f'"{word1}" and "{word2}" are anagrams.')
    else:
        print(f'"{word1}" and "{word2}" are not anagrams.')

if __name__ == "__main__":
    main()
