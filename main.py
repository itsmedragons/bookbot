from stats import get_num_words
from stats import get_num_characters
from stats import generate_report


def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    return file_contents
      
def main():
   return(get_book_text('books/frankenstein.txt'))

if __name__ == '__main__':
    main()

get_num_words(main()) 
get_num_characters(main())
generate_report(main())
