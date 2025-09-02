# Parent class
class Item:
    def __init__(self, title):
        self.title = title   

    def info(self):   
        return f"Item: {self.title}"

# Child class 
class Book(Item):
    def __init__(self, title, author, pages):
        super().__init__(title)   
        self.author = author
        self.__pages = pages  

    def read(self):   
        return f"Reading '{self.title}' by {self.author}..."

    def get_pages(self):   
        return f"Total pages: {self.__pages}"

# Example usage
book1 = Book("Nuggets of Destiny", "John K. William", 375)
print(book1.info())     
print(book1.read())       
print(book1.get_pages()) 
