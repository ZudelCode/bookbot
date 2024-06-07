def main():
    book = "books/frankenstein.txt"
    text = the_text(book)
    words_count = get_words(text)
    chars = count_characters(text)
    sorted = sort(chars)


    print(f"There are {words_count} words in this book")
    for item in sorted:
        if item["char"].isalpha():
            print(f"{item['char']} character is {item['n']} times in this book")
        else:
            continue


def get_words(text):
    words_count = text.split()
    words_count = len(words_count)
    return words_count

def count_characters(text):
    chars = {}
    char = text
    low_char = char.lower()
    for item in low_char:
        if item in chars:
            chars[item] += 1
        else:
            chars[item] = 1
    return chars

def sort_on(dic):
    return dic["n"]

def sort(chars):
    sorted = []
    for item in chars:
        sorted.append({"char": item, "n": chars[item]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted


def the_text(book):
    with open(book) as f:
        text = f.read()
    return text


main()
