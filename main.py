import sys
from stats import get_num_words
from stats import get_num_characters
from stats import generate_report


def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    return file_contents
      
def main():
   if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

   path = sys.argv[1]
   book_text = get_book_text(path)

   word_count = get_num_words(book_text)
   chars_dict = get_num_characters(book_text)
   generate_report(book_text, path)

if __name__ == '__main__':
    main()