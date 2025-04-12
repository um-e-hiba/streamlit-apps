# Function to add books
def add_book(fileName,title,author,published_year,genre,is_read):
    status = "Yes" if is_read == "yes" else "No"
    # Chunk
    chunk = (
        "=== Book Entry ===\n"
        f"Title : {title}\n"
        f"Author : {author}\n"
        f"Publication Year : {published_year}\n"
        f"Genre : {genre}\n"
        f"Status : {status}\n"
        "==================\n"
    )
    try:
            # file handling
        with open(fileName, "a") as file:
            file.write(chunk)
        return "✔ Book Entry Added Successfully.", True
    except Exception as e:
        return "❌ Failed to Add Book : {e}.!", False
        
# Function to delete book
def remove_book(fileName, title):
        # file handling
    with open(fileName, "r") as file:
        content = file.read()
    
    # Split content into chunks
    chunks = content.split("=== Book Entry ===")
    updated_chunks = []

    found = False
    for chunk in chunks:
        if chunk.strip() == "":
            continue # Skip Empty Blocks
        if f"Title : {title}" not in chunk:
            updated_chunks.append("=== Book Entry ===" + chunk)
        else :
            found = True

    if not found:
        return f"⚠ no entry found with title '{title}'." , False
    
    with open(fileName, "w") as file:
        file.writelines(updated_chunks)

    return f"✔ Entry with title '{title}' has been deleted.", True

# Functions to search books by title or by author “
def search_book_by_title(fileName, title=None):
    with open(fileName, "r") as file:
        content = file.read()

    # Split Content into Chunks
    chunks = content.split("=== Book Entry ===")

    for chunk in chunks:
        if f"Title : {title}" in chunk:
            print("✔ Book Found:")
            print("=== Book Entry ===" + chunk)
            return True

    return "✖ Book not Found.", False

def search_book_by_author(fileName, author=None):
    with open(fileName, "r") as file:
        content = file.read()

    # Split Content into Chunks
    chunks = content.split("=== Book Entry ===")

    for chunk in chunks:
        if f"Author : {author}" in chunk:
            print("✔ Book Found:")
            print("=== Book Entry ===" + chunk)
            return True 

    return "✖ Book not Found.", False
#       ”
# Function to display all books
def display_all_books(fileName):
    with open(fileName, "r") as file:
        content = file.read()

    print(content)
    return True

# Function to get book statistics
def get_book_statistics(fileName):
    try:
        with open(fileName, "r") as file:
            content = file.read()

        chunks = [chunk for chunk in content.split("=== Book Entry ===") if chunk.strip()]
        total_books = len(chunks)
        read_count = sum(1 for chunk in chunks if "Status : Yes" in chunk)
        unread_count = total_books - read_count

        if total_books == 0:
            print("⚠ No book found.!")
            return
        
        read_percentage = (read_count/ total_books) * 100
        unread_percentage = 100 - read_percentage

        print("=== Library Statistics ===")
        print(f"📚 Total Books : {total_books}")
        print(f"📖 Read : {read_count} ({read_percentage:.2f}%)")
        print(f"📔Unread : {unread_count} ({unread_percentage:.2f}%)")

    except Exception as e:
        print("✖ File not found.!")

fileName = "library.txt"

# LOOP
while True:
    print("""\nWelcome to your Personal Library Manager!
        1. Add a Book
        2. Remove a Book
        3. Search for a Book
        4. Display all Books
        5. Display Statistics
        6. Exit""")
    user_choice = input("Enter Your Choice : ")
    print("\n")

    # conditional Statement
    if user_choice.lower() == "":
        print("You didn't enter anything.")

    elif user_choice.lower() == "add a book":
        
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        published_year = input("Publication Year: ")
        genre = input("Book Genre: ")
        read_status = input("Read Status (Yes/No): ").strip().lower()

        is_read = bool(read_status)

        new_book, success = add_book(fileName, title, author, published_year, genre, is_read)

        if success:
            print(new_book)
        else:
            print(new_book)

    elif user_choice.lower() == "remove a book":
        title = input("Enter the title of the book to remove : ")
        book_to_remove, success = remove_book(fileName, title)

        if success:
            print(book_to_remove)
        else:
            print("Could not remove this book at the moment.")

    elif user_choice.lower() == "search for a book":
        print("""Search by :
            1. Title
            2. Author """)
        searched_option = input("Enter your choice (1/2): ")
                            # string manipulation
        if searched_option == "1" and searched_option != "":
            title = input("Enter the title : ")
            print(search_book_by_title(fileName, title))
                              # string manipulation
        elif searched_option == "2" and searched_option != "":
            author = input("Enter the Author : ")
            print(search_book_by_author(fileName, author))
        else: 
            print("Something went wrong try later.!")

    elif user_choice.lower() == "display all books":
        display_all_books(fileName)

    elif user_choice.lower() == "display statistics":
        get_book_statistics(fileName)

    elif user_choice.lower() == "exit": 
        print("Hope You Enjoyed your time here. Goodbye!")
        break
        
    else: 
        print("❌ Invalid option selected.")
