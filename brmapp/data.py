import csv
from brmapp.models import Book
path = "C:/Users/ajygn/OneDrive/Desktop/Github_Todolist/Book/book-record-management-yt/Data.csv"
with open(path, mode = 'r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        name = lines[0]
        author = lines[1]
        price = lines[2]
        p = Book(title = name, author = author, price = price)
        p.save()