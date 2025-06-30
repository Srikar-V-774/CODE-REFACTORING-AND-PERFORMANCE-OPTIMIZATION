from collections import Counter
def load_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()
def count_words(text):
    words = text.split()
    return words, len(words)
def count_characters(words):
    return sum(len(word) for word in words)
def count_sentences(text):
    return len([s for s in text.split('.') if s.strip()])
def most_common_word(words):
    counter = Counter(words)
    return counter.most_common(1)[0]
def average_word_length(total_chars, total_words):
    return round(total_chars / total_words, 2)
def analyze(file_path):
    text = load_text(file_path)
    words, word_count = count_words(text)
    char_count = count_characters(words)
    sentence_count = count_sentences(text)
    common_word, freq = most_common_word(words)
    avg_length = average_word_length(char_count, word_count)
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")
    print(f"Sentences: {sentence_count}")
    print(f"Most Common Word: '{common_word}' ({freq} times)")
    print(f"Average Word Length: {avg_length}")
if __name__ == "__main__":
    analyze("sample.txt")
