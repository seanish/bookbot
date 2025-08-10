from stats import count_words, create_final_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        word_count = count_words(sys.argv[1])
        character_count = create_final_count(sys.argv[1])
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at books {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        i = 0
        while i < len(character_count) - 1:
            i += 1
            if character_count[i]["char"].isalpha() != True:
                continue
            else:
                print(f"{character_count[i]['char']}" ": " f"{character_count[i]['num']}")

        print("============= END ===============")

main()
