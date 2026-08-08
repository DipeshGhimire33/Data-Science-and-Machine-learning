# A list of tuples, where each tuple contains information about a book: (title, genre, year_published, times_borrowed).

books = [
    ("The Alchemist", "Fiction", 1988, 250),
    ("The Da Vinci Code", "Mystery", 2003, 300),
    ("A Brief History of Time", "Science", 1988, 150),
    ("The Theory of Everything", "Science", 2002, 100),
    ("Pride and Prejudice", "Fiction", 1813, 200),
    ("To Kill a Mockingbird", "Fiction", 1960, 180),
    ("The Catcher in the Rye", "Fiction", 1991, 220),
    ("Angels & Demons", "Mystery", 2000, 210),
    ("The Grand Design", "Science", 2010, 90),
    ("1984", "Fiction", 1949, 190)
]

# x= []
def filter_book(genre: str, year: int):
    # for book in books:
    #     if book[1] == genre and book[2] >= year:
    #         x.append(book[0])
    # print(x)

    y=[book[0] for book in books if book[1] == genre and book[2] >= year ]
    print(y)
filter_book("Fiction",1988)



# .append has a return type of none thus 
# y=[y.append(book[0]) for book in books if book[1] == genre and book[2] >= year ] throws error
# instead used book[0]