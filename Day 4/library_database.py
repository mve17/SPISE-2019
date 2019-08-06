class Book():
    def __init__(self,title,author,available='in library'):
        self.title=title
        self.author=author
        self.available=available
    def print_info(self):
        print('\n')
        print(self.title)
        print(self.author)
        print(self.available)

class Library():
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def get_book_by_title(self,title):
        for book in self.books:
            if book.title==title:
              return book
        return None
    def print_info_by_title(self,title):
        book=self.get_book_by_title(title)
        if book:
          book.print_info()
        else:
          print('No book of this title in library.')
    def check_out_book(self,title):
        book=self.get_book_by_title(title)
        if book:
          if book.available=='in library':
            book.available='checked out'
          else:
            print('Book already checked out')
        else:
          print('No book of this title in library.')
    def check_in_book(self,title):
        book=self.get_book_by_title(title)
        if book:
          if book.available=='checked out':
            book.available='in library'
          else:
            print('Book already in library')
        else:
            print('No book of this title in library.')
    def print_catalog(self):
        if len(self.books)==0:
          print('Library Empty. Add books!')
        for book in self.books:
          book.print_info()
library=Library()
print('Welcome to the Library Database!')
while True:
    command=input('\nPlease Enter a Command: ')
    if command=='add book':
      title=input('Enter Title: ')
      author=input('Enter Author: ')
      new_book=Book(title,author)
      library.add_book(new_book)
    elif command=='check in':
      title=input('Enter title: ')
      library.check_in_book(title)
    elif command=='check out':
      title=input('Enter title: ')
      library.check_out_book(title)
    elif command=='get book info':
      title=input('Enter title: ')
      library.print_info_by_title(title)
    elif command=='print catalog':
      library.print_catalog()
    else:
      print("Unknown command. Try 'add book', 'check in', 'check out', 'get book info', or 'print catalog'.")
