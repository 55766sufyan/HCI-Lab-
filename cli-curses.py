import curses

books = []

def add_book(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.addstr("Enter book title: ")
    title = stdscr.getstr().decode()
    stdscr.addstr("Enter author name: ")
    author = stdscr.getstr().decode()
    stdscr.addstr("Enter ISBN: ")
    isbn = stdscr.getstr().decode()
    books.append({'title': title, 'author': author, 'isbn': isbn})
    stdscr.addstr("\nBook added successfully! Press any key to return to menu.")
    stdscr.getch()

def search_book(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.addstr("Search by title or author: ")
    keyword = stdscr.getstr().decode().lower()
    found = False
    stdscr.addstr("\nResults:\n")
    for book in books:
        if keyword in book['title'].lower() or keyword in book['author'].lower():
            stdscr.addstr(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}\n")
            found = True
    if not found:
        stdscr.addstr("No matching books found.\n")
    stdscr.addstr("\nPress any key to return to menu.")
    stdscr.getch()

def main(stdscr):
    curses.curs_set(0)
    while True:
        stdscr.clear()
        stdscr.addstr("Library Menu\n")
        stdscr.addstr("1. Add Book\n")
        stdscr.addstr("2. Search Book\n")
        stdscr.addstr("3. Exit\n")
        stdscr.addstr("Choose an option: ")
        choice = stdscr.getch()
        if choice == ord('1'):
            add_book(stdscr)
        elif choice == ord('2'):
            search_book(stdscr)
        elif choice == ord('3'):
            break

curses.wrapper(main)
