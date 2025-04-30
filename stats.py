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

def find_count(input_dict: dict) -> bool:
    return input_dict['num']

def sort_chars_list(char_count_dict: dict) -> list:
  sorted_by_count = []

  for char, count in char_count_dict.items():
    if char.isalpha():
      current_dict = {}
      current_dict['char'] = char
      current_dict['num'] = count
      sorted_by_count.append(current_dict)

  sorted_by_count.sort(key=find_count, reverse=True)

  return sorted_by_count
