while True:
    print("\n1.Add Book\n2.Display Books\n3.Search Book\n4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
