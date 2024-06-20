import os
import datetime

def write_entry():
    clear_screen()
    print("---Welcome to Your Personal Diary---\n")
    entry_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry_content = input("Write your entry:\n")
    entry = f"Date: {entry_date}\n\n{entry_content}\n\n"
    save_entry(entry)

def save_entry(entry):
    filename = "diary.txt"
    with open(filename, "a") as file:
        file.write(entry)
    print("\nEntry saved successfully!")

def read_entries():
    clear_screen()
    print("**** Your Personal Diary ****\n")
    try:
        with open("diary.txt", "r") as file:
            entries = file.read()
            print(entries)
    except FileNotFoundError:
        print("No entries found.")

def edit_entry():
    clear_screen()
    print("**** Edit Entry ****\n")
    try:
        with open("diary.txt", "r") as file:
            entries = file.readlines()

        if not entries:
            print("No entries found.")
            return

        print("Entries:")
        for i, entry in enumerate(entries):
            print(f"{i+1}. {entry.strip()}")

        entry_num = int(input("\nEnter the number of the entry you want to edit: ")) - 1

        if entry_num < 0 or entry_num >= len(entries):
            print("Invalid entry number.")
            return

        print(f"\nEditing entry {entry_num + 1}:")
        new_content = input("Enter new content:\n")

        entries[entry_num] = new_content + "\n"

        with open("diary.txt", "w") as file:
            file.writelines(entries)

        print("\nEntry edited successfully!")
    except FileNotFoundError:
        print("No entries found.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        print("\n1. Write an entry")
        print("2. Read entries")
        print("3. Edit an entry")
        print("4. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            edit_entry()
        elif choice == "4":
            print("Thank you for using Your Personal Diary. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
