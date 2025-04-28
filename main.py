from stats import count_num_words, count_chars

def main() -> None:
  book_path = 'books/frankenstein.txt'
  text = get_book_text(book_path)
  num_words = count_num_words(text)
  char_count_dict = count_chars(text)
  # print(text)
  print(f"{num_words} words found in the document", char_count_dict)

def get_book_text(filepath: str) -> str:
  with open(filepath) as f:
    return f.read()

main()
