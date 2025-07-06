import string
from collections import Counter

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words), words

def count_characters(text):
    return len(text)

def count_sentences(text):
    sentences = text.split('.')
    return len([s for s in sentences if s.strip() != ''])

def count_paragraphs(text):
    paragraphs = text.split('\n\n')
    return len([p for p in paragraphs if p.strip() != ''])

def most_common_words(words, n=5):
    cleaned_words = [word.strip(string.punctuation).lower() for word in words]
    counter = Counter(cleaned_words)
    return counter.most_common(n)

def longest_and_shortest_words(words):
    cleaned_words = [word.strip(string.punctuation) for word in words if word]
    longest = max(cleaned_words, key=len)
    shortest = min(cleaned_words, key=len)
    return longest, shortest

def main():
    filepath = input("Enter path to text file: ").strip()
    try:
        text = read_file(filepath)
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return

    word_count, words = count_words(text)
    char_count = count_characters(text)
    sentence_count = count_sentences(text)
    paragraph_count = count_paragraphs(text)
    common_words = most_common_words(words)
    longest, shortest = longest_and_shortest_words(words)

    print("\n--- Text File Analysis ---")
    print(f"Total Characters: {char_count}")
    print(f"Total Words: {word_count}")
    print(f"Total Sentences: {sentence_count}")
    print(f"Total Paragraphs: {paragraph_count}")
    print(f"Most Common Words: {common_words}")
    print(f"Longest Word: {longest}")
    print(f"Shortest Word: {shortest}")

if __name__ == "__main__":
    main()
