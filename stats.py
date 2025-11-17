def get_num_words(book):
    return len(book.split())

def get_char_count(book):
    book = book.lower()
    # compiles list of characters used in book
    characters = []
    for n in book:
        if n not in characters:
            characters.append(n)
    
    char_dict = {}
    for c in characters:
        result = 0

        for n in book:
            if n == c:
                result += 1

        char_dict[c] = result

    return char_dict

def sort_on(d):
    return d["num"]

def sort_dictionary(dictionary):
    sorted_list = []
    for ch in dictionary:
        sorted_list.append({"char": ch, "num": dictionary[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
