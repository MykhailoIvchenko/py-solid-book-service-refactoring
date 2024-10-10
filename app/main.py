from app.book import Book
from app.book_managers import BookViewer, BookPrinter, BookSerializer
from app.method_validators import (
    DisplayMethodValidator,
    PrinterMethodValidator,
    SerializerMethodValidator
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            validator = DisplayMethodValidator()
            validator.validate_method(method_type)
            viewer = BookViewer(book.title, book.content)
            if method_type == "console":
                viewer.display_console()
            else:
                viewer.display_reverse()
        elif cmd == "print":
            validator = PrinterMethodValidator()
            validator.validate_method(method_type)
            printer = BookPrinter(book.title, book.content)
            if method_type == "console":
                printer.print_console()
            else:
                printer.print_reverse()
        elif cmd == "serialize":
            validator = SerializerMethodValidator()
            validator.validate_method(method_type)
            serializer = BookSerializer(book.title, book.content)
            if method_type == "json":
                return serializer.serialize_to_json()
            else:
                return serializer.serialize_to_xml()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
