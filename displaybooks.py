def display_books():
    with open("library.txt", "r") as file:
        for line in file:
            book = line.strip().split(",")
            print("ID:", book[0], "Name:", book[1], "Author:", book[2], "Qty:", book[3])