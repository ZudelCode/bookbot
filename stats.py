content = """

The Project Gutenberg eBook of Frankenstein; Or, The Modern Prometheus
    
This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,
you will have to check the laws of the country where you are located
before using this eBook.

"""
def count_words(content):
    sum_of_words = content.split()
    return len(sum_of_words)

def count_characters(content):
    words_dictionary = {}
    words = content.lower().split()
    for word in words:
        for chars in word:
            if chars in words_dictionary:
                words_dictionary[chars] += 1
            else:
                words_dictionary[chars] = 1
    return words_dictionary

def make_sorted_list(diction):
    listing = []
    for k in diction:
        listing.append({"name": k, "count": diction[k]})
    listing.sort(reverse=True, key=sort_on)
    return listing

def sort_on(d):
    return d["count"]
