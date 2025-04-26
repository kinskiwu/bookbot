def main() -> None:
  book_path = 'books/frankenstein.txt'
  text = get_book_text(book_path)
  num_words = count_num_words(text)
  # print(text)
  print(f"{num_words} words found in the document")

def get_book_text(filepath: str) -> str:
  with open(filepath) as f:
    return f.read()

def count_num_words(book_text: str) -> int:
  temp = book_text.split()
  return len(temp)

main()
