import sys
from stats import count_words, count_characters, make_sorted_list
import sys


if len(sys.argv) < 2:
    print("""No book to analyze! 
to use this script properly, add relative or absolute path to book
Usage: python3 main.py <path_to_book>""")
    sys.exit(1)

filepath = sys.argv[1]
def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():
    content = get_book_text(filepath)
    the_dict = count_characters(content)
    sorted_list = make_sorted_list(the_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(content)} total words")
    print("--------- Character Count -------")
    for character in sorted_list:
        if character["name"].isalpha():
            print(f"{character["name"]}: {character["count"]}")
    print("============= END ===============")
if __name__ == "__main__":
    main()
