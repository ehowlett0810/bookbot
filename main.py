import sys
from stats import word_count, unique_char_count, sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: pythong3 main.py <path_to_books>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = word_count(text)

    char_counts = unique_char_count(text)
    
    sorted_chars = sort_char_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    # Print character count section
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["character"]
        count = char_dict["count"]

        if char.isalpha():
             print(f"{char}: {count}")

    print("============= END ===============")

main()

