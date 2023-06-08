class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):

        adding_book = Book(name, year, author)
        self.books.append(adding_book)
        self.authors.append(author)
        Author.add_book(author, adding_book)

    def group_by_author(self, author):
        flag = False
        for book in self.books:
            if book.author == author:
                flag = True
                print(f'{author.name} wrote a book: {book.name}')

        if not flag:
            print(f'Not found books of {author} author')

    def group_by_year(self, year):
        flag = False
        for book in self.books:
            if book.year == year:
                flag = True
                print(f'Book name: {book.name} was written in {year} by {book.author.name}')

        if not flag:
            print(f'Not found books of {year} year')

    def __str__(self):
        return f'Library "{self.name}"'

    def __repr__(self):
        return f'Library "{self.name}"'

    def show_books(self):
        if len(self.books) == 0:
            print('Library store is empty')
        else:
            for book in self.books:
                print(book)


class Book:
    count_of_books = 0

    def __init__(self, name, year, autor):
        self.name = name
        self.year = year
        self.author = autor
        Book.count_of_books += 1

    def __str__(self):
        return f'Book: {self.name}, year: {self.year}, author: {self.author}'

    def __repr__(self):
        return f'Book: {self.name}, year: {self.year}, author: {self.author}'


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f'Author: {self.name}, country: {self.country}, birthday: {self.birthday}'

    def __repr__(self):
        return f'Author: {self.name}, country: {self.country}, birthday: {self.birthday}'

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        flag = False
        for book in self.books:
            flag = True
            print('"' + book.name + '"')
        if not flag:
            print(f'Not found books of {self.name} author')

print('-' * 20)
# adding authors
author1 = Author('Taras Shevchenko', 'Ukraine', '1814-03-09')
author2 = Author('Ivan Nechuy-Levytsky', 'Ukraine', '1838-07-15')
author3 = Author('Ivan Kotlyarevsky', 'Ukraine', '1769-09-09')


# list of books of author1 is empty for now
print("Showing list of author`s 1 books")
author1.show_books()


# creating library
print('-' * 20)
print('Printing name of library through str methods')
libr1 = Library('National Library')
print(libr1)


print('-' * 20)
print(f'Showing all books in library "{libr1.name}"')
libr1.show_books()

print('-' * 20)

# adding books to the libraries
libr1.new_book('Kobzar', 1840, author1)
libr1.new_book('Kaydasheva simya', 1879, author2)
libr1.new_book('Eneida', 1798, author3)
libr1.new_book('Kavkaz', 1859, author1)

print(f'We added 4 books to the library and now we can see books of {author1.name} in stock of "{libr1.name}"')
author1.show_books()

print('-' * 20)
print(f'For now we are going to iterate through books of {author1.name} and show them')
libr1.group_by_author(author1)

print('-' * 20)
print(f'For now we are going to iterate through years of writing books and show them')
libr1.group_by_year(1798)

print('-' * 20)
print(f'Show all books in library "{libr1.name}"')
libr1.show_books()








