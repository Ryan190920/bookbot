def get_num_words(book_text):
    count_of_words = book_text.split()
    words = len(count_of_words)
    return words

def get_num_characters(book_text):
    characters = {}
    
    for character in book_text:
        lowercase_character = character.lower()
        if lowercase_character in characters:
            characters[lowercase_character] += 1
        else:
            characters[lowercase_character] = 1
    
    return characters

def sort_the_dictionary(characters):
    char_list = []
    
    for char, count in characters.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(key = lambda x: x["num"], reverse = True)

    return char_list