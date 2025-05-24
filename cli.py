books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    books.append({'title': title, 'author': author, 'isbn': isbn})
    print("Book added successfully!\n")

def search_book():
    keyword = input("Search by title or author: ").lower()
    found = False
    print("\nSearch Results:")
    for book in books:
        if keyword in book['title'].lower() or keyword in book['author'].lower():
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
            found = True
    if not found:
        print("No matching books found.")
    print()

def main():
    while True:
        print("Library Menu")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            break
        else:
            print("Invalid choice!\n")

main()
