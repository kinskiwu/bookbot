from stats import count_num_words, count_chars, sort_chars_list

def main() -> None:
  book_path = 'books/frankenstein.txt'
  text = get_book_text(book_path)
  num_words = count_num_words(text)
  char_count_dict = count_chars(text)
  sorted_chars_list = sort_chars_list(char_count_dict)
  print_report(book_path, num_words, sorted_chars_list)

def get_book_text(filepath: str) -> str:
  with open(filepath) as f:
    return f.read()

def print_report(book_path, num_words, sorted_chars_list) -> None:
    print("============ BOOKBOT ============\n\n",f"Analyzing book found at {book_path}\n\n","----------- Word Count ----------\n\n", f"Found {num_words} total words\n\n", "--------- Character Count -------\n\n")

    for dic in sorted_chars_list:
      if not dic['char'].isalpha():
        continue
      print(f"{dic['char']}: {dic['num']}")

main()
