class Item:
    def __init__(self, title, creator):
        self.title = title
        self.creator = creator

    def display_info(self):
        raise NotImplementedError("Subclasses must implement this method")


class Book(Item):
    def __init__(self, title, creator, pages, genre):
        super().__init__(title, creator)

        if pages <= 0:
            raise ValueError("Pages must be greater than 0")

        if not isinstance(genre, str) or not genre.strip():
            raise ValueError("Genre must be a non-empty string")

        self.pages = pages
        self.genre = genre

    def display_info(self):
        return f"Title: {self.title}, Creator: {self.creator}, Pages: {self.pages}, Genre: {self.genre}"


class Magazine(Item):
    def __init__(self, title, creator, issue_number, month):
        super().__init__(title, creator)

        if issue_number <= 0:
            raise ValueError("Issue number must be greater than 0")

        self.issue_number = issue_number
        self.month = month

    def display_info(self):
        return f"Title: {self.title}, Creator: {self.creator}, Issue Number: {self.issue_number}, Month: {self.month}"


class Comic(Item):
    def __init__(self, title, creator, illustrator, volume):
        super().__init__(title, creator)

        if not isinstance(illustrator, str) or not illustrator.strip():
            raise ValueError("Illustrator must be a non-empty string")

        if not isinstance(volume, int) or volume <= 0:
            raise ValueError("Volume must be greater than 0")

        self.illustrator = illustrator
        self.volume = volume

    def display_info(self):
        return f"Title: {self.title}, Creator: {self.creator}, Illustrator: {self.illustrator}, Volume: {self.volume}"


class Shelf:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def add_item(self, item: Item):
        for existing_item in self.items:
            if existing_item.title.lower() == item.title.lower():
                print("Item already exists")
                return

        self.items.append(item)
        print("Item added successfully")

    def view_items(self):
        if not self.items:
            print("Shelf is empty")
            return

        for item in self.items:
            print(item.display_info())

    def search_by_attributes(self, attribute_name, value):
        for item in self.items:
            attr = getattr(item, attribute_name, None)

            if attr is not None and str(attr).lower() == str(value).lower():
                print(item.display_info())
                return

        print("Item not found")


book = Book("The Great Gatsby", "ABC", 200, "Classic")
magazine = Magazine("The New Yorker", "PQR", 1, "January")
comic = Comic("The Walking Dead", "XYZ", "Jason Bourne", 1)

shelf = Shelf()
shelf.add_item(book)
shelf.add_item(magazine)
shelf.add_item(comic)

print(f"Total items: {len(shelf)}")
shelf.view_items()

shelf.search_by_attributes("title", "The Great Gatsby")