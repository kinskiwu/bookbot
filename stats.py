def count_num_words(book_text: str) -> int:
  if not book_text:
    return 0
  temp = book_text.split()
  return len(temp)

def count_chars(book_text: str) -> dict:
  if not book_text:
    return {}

  char_count = {}

  for char in book_text:
    formatted_char = char.lower()
    if formatted_char not in char_count:
      char_count[formatted_char] = 1
    else:
      char_count[formatted_char] += 1

  return char_count


