# Day 23 - Notes File App (CRUD in .txt)

# This is constant which is holding file name where our notes will be stored.
NOTES_FILE = "notes.txt"

# This function is used to display the menu to the user, which represents what what operations can be performed on file.
def show_menu():
    print("\n🗂️ Notes File App")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")

# This function first asks the user to enter the content to add then adds the note by opening the file in append mode and writes into 
# the file, and then displays an user friendly msg that the note is successfully added. And if notes file didn't founds creates it.
def add_note():
    note = input("📝 Enter your note: ")
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    print("✅ Note added.")

# This function tries to open the file in read mode and reads all lines into notes list, If the file founds empty thn displays a msg that
# the file not found else displays the contents of file with index number by removing extra spaces by .strip(). So, if the file isn't founds
# then displays a user friendly msg that file isn't found. 
def view_notes():
    try:
        with open(NOTES_FILE, "r") as f:
            notes = f.readlines()
            if not notes:
                print("📭 No notes found.")
            else:
                print("\n📖 Your Notes:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("🚫 No notes file found.")

# This function updates the existing notes in the file, First it displays all contents/notes in file by calling the view_notes() function
# allowing the user to choose the content of note to update by index. It reads all notes into a list in read-mode. And asks the user for 
# index number of the content to update and asks to enter and updates that specific note in write-mode and then displays user friendly msg
# that note has updated. If the entered index didn't found then alerts user with an alert msg, if file not found alerts user with alert msg.
def update_note():
    view_notes()
    try:
        with open(NOTES_FILE, "r") as f:
            notes = f.readlines()
        idx = int(input("🔁 Enter note number to update: ")) - 1
        if 0 <= idx < len(notes):
            new_note = input("✏️ Enter updated note: ")
            notes[idx] = new_note + "\n"
            with open(NOTES_FILE, "w") as f:
                f.writelines(notes)
            print("✅ Note updated.")
        else:
            print("⚠️ Invalid note number.")
    except (ValueError, IndexError):
        print("⚠️ Please enter a valid number.")
    except FileNotFoundError:
        print("🚫 Notes file not found.")

# This function is used to delete the note from the notes file. First it displays the contents of the file by calling view_notes(). Then
# tries to open file in read-mode and reads all contents and stores in a list and asks the user for the index of the note to be removed, 
# And then deletes the note and displays the note which was deleted and updates the notes after deleting the deleted content. If user enters
# the invalid index number then displays the alert msg index not found, if file isn't found alerts the user with an alert msg.
def delete_note():
    view_notes()
    try:
        with open(NOTES_FILE, "r") as f:
            notes = f.readlines()
        idx = int(input("❌ Enter note number to delete: ")) - 1
        if 0 <= idx < len(notes):
            deleted = notes.pop(idx)
            with open(NOTES_FILE, "w") as f:
                f.writelines(notes)
            print(f"✅ Deleted: {deleted.strip()}")
        else:
            print("⚠️ Invalid note number.")
    except (ValueError, IndexError):
        print("⚠️ Please enter a valid number.")
    except FileNotFoundError:
        print("🚫 Notes file not found.")

# main
def main():
    # This loop runs until user chooses exit button by breaking the loop.
    while True:
        # displays the available menu options to the user to perform operations on the file
        show_menu()
        # asks the user to choose the meniu option to perform the file operations the file. 
        choice = input("👉 Enter choice: ")
        # If user chooses option 1 then it calls add_note()
        if choice == '1':
            add_note()
        # If user chooses option 2 then it calls view_notes() 
        elif choice == '2':
            view_notes()
        # If user chooses option 3 then it calls update_note()
        elif choice == '3':
            update_note()
        # If user chooses option 4 then calls delete_note()
        elif choice == '4':
            delete_note()
        # If user chooses option 5 then exits the loop by breaking and displaying an exit msg to user.
        elif choice == '5':
            print("👋 Exiting Note File App...")
            break
        # If the choosen option is invalid this msg will be displayed 
        else:
            print("⚠️ Invalid choice. Try again.")

# calling main() to starting execution of program
if __name__ == "__main__":
    main()
