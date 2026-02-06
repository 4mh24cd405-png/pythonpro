def search_book():
    search_id = input("Enter Book ID to search: ")
    found = False
    with open("library.txt", "r") as file:
        for line in file:
            book = line.strip().split(",")
            if book[0] == search_id:
                print("Book Found:", book)
                found = True
                break
    if not found:
        print("Book not found")
