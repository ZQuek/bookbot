def get_num_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_char(text):
    char = {}
    words = text.split()
    for word in words:
        for character in word:
            character = character.lower()
            if character not in char:
                char[character] = 0
            if character in char:
                char[character] += 1
    return char