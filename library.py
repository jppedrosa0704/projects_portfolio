import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def register_books(books):
    
    while True:
        clear_screen()
        while True:
            title_input = input("Enter the book title: ").strip()
            if title_input == "":
                print("Cannot be empty.")
                continue
            else:
                break

        if title_input in books:
            print(f"⚠️  {title_input} is already in the catalog.")
        else:
            books[title_input] = {}
        
            while True:
                author = input("Enter the author: ").strip()
                if author.isdigit():
                    print("⚠️  Invalid author name.")
                    continue
                elif author == "":
                    print("Cannot be empty.")
                    continue
                else:
                    break

            while True:
                try:
                    year = int(input("Year: "))
                    
                    if year < 1000 or year > 10000:
                        print("⚠️  Year must have 4 digits.")
                        continue
                    else:
                        break
                except ValueError:
                    print("Enter a valid year")
                    continue
            
            status = 'available'
            data = {'author': author, 'year': year, 'status': status }
            books[title_input] = data

            print(f"Title: {title_input} successfully registered!")
            input("\nPress Enter to continue...")
            clear_screen()

            resp = input("Would you like to register another book? [Y/N] ").upper()
            if resp == 'N':
                break

def search_book_by_author_title(books):
    clear_screen()
    while True:
        search = input("Enter author name or title: ").lower()
        
        found = False
        print("---"*13)

        for k, v in books.items():
            if search == k.lower() or search == v['author'].lower():
                print(f"Title: {k:<60}")
                print(f"Author: {v['author']}")
                print(f"Year: {v['year']}")
                print(f"Status: {v['status']}")
                print("---"*13)
                found = True

        if not found:
            print(f"❌  {search} not found")

        resp = input("Do you want to continue searching? [Y/N] ").upper()
        if resp == 'N':
            break

def list_books(books):
    clear_screen()
    for k, v in sorted(books.items()):
        print("---"*13)
        print(f"Title: {k:<60}")
        print(f"Author: {v['author']}")
        print(f"Year: {v['year']}")
        print(f"Status: {v['status']}")
        
    print("---"*13)
    input("\nPress Enter to continue...")

def borrow_return_book(books):
    clear_screen()
    print("BORROW / RETURN MENU")
    print("[1] Borrow book")
    print("[2] Return book")
    print("[3] Exit")

    while True:
        try:
            option = int(input("Choose an option: "))
            if option < 1 or option > 3:
                print("Enter a valid option.")
                continue
            else: 
                break
        except ValueError:
            print("Enter a valid option.")

    match option:

        case 1:
            while True:
                borrow_book = input("Enter the book title or press ENTER to cancel: ").strip()
                if borrow_book == "":
                    break

                search = borrow_book.lower()
                real_title = None
                
                for title in books:
                    if search == title.lower():
                        real_title = title
                        break

                if not real_title:
                    print("❌  This book is not in our library")
                    continue

                if books[real_title]['status'] == 'available':
                    books[real_title]['status'] = 'borrowed'
                    print(f"📚 {real_title} borrowed successfully!")
                else:
                    print("⚠️  The book is already borrowed.")

                resp = input("\nBorrow another book? [Y/N]: ").upper()
                if resp != "Y":
                    break

        case 2:
            while True:
                return_book = input("Enter the book title: ")
                
                search = return_book.lower()
                real_title = None
                
                for title in books:
                    if search == title.lower():
                        real_title = title
                        break

                if not real_title:
                    print("❌  This book is not in our library")
                else:
                    if books[real_title]['status'] == 'borrowed':
                        books[real_title]['status'] = 'available'
                        print(f"{real_title} returned successfully!")
                    else:
                        print("⚠️  The book is already available")
                    
                    resp = input("\nContinue? [Y/N]: ").upper()
                    if resp != "Y":
                        break

        case 3:
            return

def remove_book(books):
    while True:
        remove = input("Which title do you want to delete or press ENTER to exit? ").strip()
        if remove == "":
            break

        if remove in books:
            del books[remove]
            print(f"{remove} successfully deleted.")
        else:
            print(f"{remove} is not in the library.")
        
        resp = input("Do you want to continue? [Y/N] ").upper()
        if resp != 'Y':
            break
        
def menu():
    print("-"*36)
    print(f"{'MENU':^34}")
    print("-"*36)
    print("[1] Register book")
    print("[2] List books")
    print("[3] Search by title or author")
    print("[4] Borrow/Return book")
    print("[5] Remove book")
    print("[6] Exit")

clear_screen()

books = {
    "The Little Prince": {
        "author": "Antoine de Saint-Exupéry",
        "year": 1943,
        "status": "available"
    },
    "1984": {
        "author": "George Orwell",
        "year": 1949,
        "status": "borrowed"
    },
    "Dom Casmurro": {
        "author": "Machado de Assis",
        "year": 1899,
        "status": "available"
    }
}

# MAIN PROGRAM
while True:
    clear_screen()
    menu()
    
    while True:
        try:
            option = int(input("Enter your choice: "))
            if option < 1 or option > 6:
                print("⚠️  Enter a valid option")
                continue
            else:
                break
        except ValueError:
            print("⚠️  Enter a valid option.")
            continue

    match option:
        case 1:
            register_books(books)
        case 2:
            list_books(books)
        case 3:
            search_book_by_author_title(books)
        case 4:
            borrow_return_book(books)
        case 5:
            remove_book(books)
        case 6:
            for i in range(3,0,-1):
                print(f"{i}",end="...")
                time.sleep(1)
            print("End.")
            print("❌  Program successfully terminated!")
            break