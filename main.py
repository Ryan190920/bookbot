import sys
from stats import get_num_words, get_num_characters, sort_the_dictionary

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

def get_book_text(filepath):
    """Read and return the contents of a text file."""
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    """Main function that analyzes book text and prints statistics."""
    book_text = get_book_text(path_to_book)

    words = get_num_words(book_text)
    characters = get_num_characters(book_text)

    sorted_dictionary = sort_the_dictionary(characters)
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found' {words} 'total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_dictionary:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")

main()