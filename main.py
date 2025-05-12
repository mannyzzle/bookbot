from stats import get_char_count, get_num_words, report
import sys

if len(sys.argv) < 2 or len(sys.argv) > 2 :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    file = sys.argv[1]
    num_words = get_num_words(file)
    report1 = report(file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in report1.items():
        if key.isalpha():
            print(f"{key}: {value}")
        else:
            continue
    print("============= END ===============")



main()
