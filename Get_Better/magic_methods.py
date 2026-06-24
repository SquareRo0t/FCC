# Magic methods = Dunder methods (double underscore) __init__, __Str__, __eq__
#                 They are automatically called by many of python's build-in operations.
#                 They allow developers to define or customize the behavior of objects

# class Student:

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa

#     def __str__(self):
#         return f"name: {self.name} gpa {self.gpa}"
    
#     def __eq__(self, other):
#         return self.name == other.name
    
#     def __gt__(self, other):
#         return self.gpa > other.gpa
    
# student1 = Student("BOB", 2.0)
# student2 = Student("ROB", 3.0)


class Book:

    def __init__(self, titel, author, num_pages):
        self.title = titel
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f" '{self.title}' '{self.author}'"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key =="author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("Fantasy", "M.I.K", 100)
book2 = Book("Fantasy2", "M.I.K.2", 200)
book3 = Book("Fantasy3", "M.I.K.3", 300)

# print(book1)
# print(book1 == book2)
# print(book2 < book3)
# print(book2 > book3)
# print(book2 + book3)

print(book1["num_pages"])