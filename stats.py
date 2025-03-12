def get_num_words(text):
    words = text.split()
    total_words = (len(words),"words found in the document")
    return total_words

def get_num_characters(text):
    letter_dict = {}

    for letter in text.lower():
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1

    return(letter_dict)

def generate_report(text,path):
    print("============ Bookbot ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count -----------")
    word_count, message = get_num_words(text)
    print(f"Found {word_count} total words")

    print("----------- Character Count -----------")
    character_counts = get_num_characters(text)
    sorted_counts = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_counts:
        print(f"{char}: {count}")
              
    print("============ END ============")
