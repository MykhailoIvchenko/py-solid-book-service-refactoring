from app.book import Book
import json
import xml.etree.ElementTree as Et


class BookPrinter(Book):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def print_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])


class BookViewer(Book):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def display_console(self) -> None:
        print(self.content)

    def display_reverse(self) -> None:
        print(self.content[::-1])


class BookSerializer(Book):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def serialize_to_json(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})

    def serialize_to_xml(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.title
        content = Et.SubElement(root, "content")
        content.text = self.content

        return Et.tostring(root, encoding="unicode")
