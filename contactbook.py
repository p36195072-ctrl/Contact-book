import json

try:
    with open("contactbook.json", "r") as file:
        contactbook = json.load(file)
except FileNotFoundError:
    contactbook = {}

def save_data():
    with open("contactbook.json", "w") as file:
        json.dump(contactbook, file, indent=4)

def add_contact():
    contact = input("Enter the name of the contact: ")
    if contact == "":
        print("Contact can't be empty")
        return

    phone_no = int(input("Enter the phone number: "))
    if phone_no == "":
        print("Phone number can't be empty")
        return

    gender = input("Enter the gender (male/female): ")
    if gender == "":
        print("Gender can't be empty")
        return

    city = input("Enter the city: ")
    if city == "":
        print("City can't be empty")
        return

    # Save contact details
    contactbook[contact] = {
        "phone_no": phone_no,
        "gender": gender,
        "city": city
    }

    save_data()
    print("Contact saved successfully!")



def search_contact():
    search = input("Enter the contact you want to search: ")

    if search == "":
        print("Search can't be empty")
        return

    if search in contactbook:
        print("\nContact Found!")
        print("Name:", search)
        print("Phone No:", contactbook[search]["phone_no"])
        print("Gender:", contactbook[search]["gender"])
        print("City:", contactbook[search]["city"])
    else:
        print("Contact not found!")

def view_contacts():
    if len(contactbook) == 0:
        print("No contacts found")
        return

    for name in contactbook:
        print("\nName:", name)
        print("Phone:", contactbook[name]["phone_no"])
        print("Gender:", contactbook[name]["gender"])
        print("City:", contactbook[name]["city"])

def exit_programe():
    print("Exiting...")
    save_data()
    


while True:

    print("\n===== STUDENT MANAGER =====")
    print("1. add contacts")
    print("2. Search contacts")
    print("3. View contacts")
    print("4. Exit")

    choice = input("Enter the number:").strip()
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()

    elif choice == "3":
        view_contacts()

    elif choice == "4":
        exit_programe()
        break
