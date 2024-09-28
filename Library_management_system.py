# Library Management System
books = ["Python for Everybody", "AI/ML Engineer", "Learn Boring Stuff", "The Catcher in the Rye", 
         "Moby-Dick", "Pride and Prejudice", "War and Peace"]
borrow_books = []

# Function to display available books
def display():
    print("\nThe list of books are as follows:")
    for index, book in enumerate(books, 1):  # Unpacking enumerate
        print(f"{index}. {book}")

# Function to borrow a book
def borrow():
    name_book = input("Enter the name of the book you want to borrow: ")
    if name_book in books:  # Check if the book is available
        books.remove(name_book)
        borrow_books.append(name_book)  # Add the book to borrowed books
        print(f"You borrowed '{name_book}'.")
    else:
        print("Sorry, that book is not available.")

# Function to return a book
def Return():
    book_name = input("Enter the name of the book you want to return: ")
    if book_name in borrow_books:
        books.append(book_name)  # Add the book back to available books
        borrow_books.remove(book_name)  # Remove it from borrowed books
        print(f"Thank you for returning '{book_name}'.")
    else:
        print(f"You haven't borrowed '{book_name}'.")

# Function to handle user's option (switch case)
def switch_case(option):
    match option:
        case 1:
            display()
        case 2:
            borrow()
        case 3:
            Return()
        case _:
            print("Invalid option. Please select 1, 2, or 3.")

# Main function to drive the program
def main():
    name = input("Enter your name: ")
    print(f"Hello, {name}. Welcome to MF Library!")

    while True:
        # Asking for user's option
        try:
            option = int(input("\nSelect an option:\n1. Display Books\n2. Borrow Books\n3. Return Books\n4. Exit\n"))
            if option == 4:
                print("Thank you for using the library system. Goodbye!")
                break  # Exit the loop and the program
            switch_case(option)  # Call the function to handle the user's choice
        except ValueError:
            print("Please enter a valid number.")

# Run the main program
main()

