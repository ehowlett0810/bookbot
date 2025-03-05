def word_count(text):
    words = text.split()
    total_words = len(words)
    return total_words

def unique_char_count(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_char_count(char_counts):
    sorted_chars = []
    for char, count in char_counts.items():
        sorted_chars.append({'character': char, 'count': count})
    
    sorted_chars.sort(reverse=True, key=lambda x: x['count'])
    return sorted_chars