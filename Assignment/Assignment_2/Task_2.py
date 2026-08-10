
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

# Task 2 Soln,

# x=[]
# y=[]
# for book in books:
#    x.append(book[2]) 
#    x=sorted(x)
# for i in x:
#    for book in books:
      
#          if i == book[2]:
#             y.append(book)

# print(y)

x=[book[2] for book in books ]
sort_book= lambda x:sorted(x)
x= sort_book(x)
y=[book for year in x for book in books if year == book[2] ]
print(y)