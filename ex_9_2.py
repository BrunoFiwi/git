books = []

def add_book(title, author, year):
    books.append({
        "title": title,
        "author": author,
        "year": year
    })

def list_books():
    if not books:
        print("No books in the library.")
    for b in books:
        print(f"{b['title']} by {b['author']} ({b['year']})")

def search_book(keyword):
    found = [b for b in books if keyword.lower() in b['title'].lower()]
    for b in found:
        print(f"{b['title']} by {b['author']}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            t = input("Title: ")
            a = input("Author: ")
            y = input("Year: ")
            add_book(t, a, y)
        elif choice == "2":
            list_books()
        elif choice == "3":
            k = input("Search keyword: ")
            search_book(k)
        elif choice == "4":
            break
