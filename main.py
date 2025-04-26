def main() -> None:
  book_path = 'books/frankenstein.txt'
  text = get_book_text(book_path)
  print(text)

def get_book_text(filepath: str) -> str:
  with open(filepath) as f:
    return f.read()

main()
