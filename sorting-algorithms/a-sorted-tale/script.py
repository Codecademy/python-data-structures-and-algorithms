import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

print("Bubble sort, title ascending:")
for book in sort_1:
  print(book['title'])
  
def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

bookshelf_v1 = bookshelf.copy()
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

print("Bubble sort, author ascending:")
for book in sort_2:
  print(book['author'])

bookshelf_v2 = bookshelf.copy()
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

print("Quicksort, author ascending:")
for book in bookshelf_v2:
  print(book['author'])

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

long_bookshelf_1 = utils.load_books('books_large.csv')

# sorts.bubble_sort(long_bookshelf_1, by_total_length)
sorts.quicksort(long_bookshelf_1, 0, len(long_bookshelf_1) - 1, by_total_length)
