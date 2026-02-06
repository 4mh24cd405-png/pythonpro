def add_book():
    with open("library.txt", "a") as file:
        book_id = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        author = input("Enter Author: ")
        qty = input("Enter Quantity: ")
        file.write(f"{book_id},{name},{author},{qty}\n")
    print("Book added successfully!")