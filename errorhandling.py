import json
import os

FILENAME =  "data.json"

def load_notes():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME,'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error reading")
        return []


def save_notes(notes):
    try:
        with open(FILENAME,'w') as file:
            json.dump(notes, file, indent=4)
    except Exception as e:
        print("Error saving", e)

def add_note():
    note = input("Enter your Note:")
    if note.strip():
        notes = load_notes()
        notes.append(note)
        save_notes(notes)
        print("Note Added")
    else:
        print("Note cannot be empty")


def view_notes():
    notes = load_notes()
    if notes:
        print("\n Your Notes:")
        for i , note in enumerate(notes,1):
            print(f"{i}. {note}")
    else:
        print("No Note found")  


def delete_notes():
    notes = load_notes()

    if not notes:
        print("Notes not found")
        return 
    print("select Note to delete")
    for i , note in enumerate(notes,1):
            print(f"{i}. {note}")

    try:
        choice = int(input("Enter a note number to delete"))
        if 1<=choice<=len(notes):
            removed = notes.pop(choice - 1)
            save_notes(notes)
            print(f"Delete: {removed}")
        else:
            print("Invalid note number")
    except ValueError:
        print("please enter a valid number")                      

# def delete_notes():
#     notes = load_notes()
    
#     if not notes:
#         print("Notes not found")
#         return
    
#     view_notes()  # Show the notes that help the user to choose the notes that he/she wants to delete

#     note_to_delete = input("Enter the note you want to delete form the added notes: ").strip()

#     if note_to_delete in notes:
#         notes.remove(note_to_delete) 
#         save_notes(notes)
#         print(f"Deleted not{note_to_delete}")
#     else:
#         print("Note not found,Please enter the correct note from the given notes")        



def main():
    while True:
        print("\n Simple note app")
        print("1. Add Note")
        print("2. View Note")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("choose option 1 -4")

        if choice =="1":
            add_note()
        elif choice =="2":
            view_notes()
        elif choice =="3":
            delete_notes()
        elif choice=="4":
            print("BYe")
            break
        else:
            print("! Invalid option")

if __name__ == "__main__":
    main()












# try:
#     result = 10/0
#     test = input("enter your name") #6
#     test.striifgkdf
# except (ZeroDivisionError,TypeError) as e :
#         print("Mesage", e)
# else:
#       print("Yur message") 
# finally:
#       print("Garbage collection")             