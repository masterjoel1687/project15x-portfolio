def contact_book():
    contacts = {}

    while True:
        n = input("\n1.Add a Contact\n2.Search Contacts\n3.Delete a Contact\n4.Exit\nChoose an option: ")
        if n == "1":
            input_contact = input("Enter a Contact Book Entry (Name:Phone Number): ")
            if ":" in input_contact:
                name, phone = input_contact.split(":", 1)
                name, phone = name.strip(), int(phone.strip())
                if name and phone:
                    contacts[name] = phone
                    print(f"Contact '{name}' added successfully.\n")
                else:
                    print("Invalid entry. Both name and phone number must be non-empty.\n")
            else:
                print("Invalid format. Please use Name:Phone Number.\n")
        elif n == "2":
            search_name = input("Enter the name to search: ")
            if search_name in contacts:
                print(f"{search_name}: {contacts[search_name]}\n")
            else:
                print(f"Contact '{search_name}' not found.\n")
        elif n == "3":
            delete_name = input("Enter the name to delete: ")
            if delete_name in contacts:
                del contacts[delete_name]
                print(f"Contact '{delete_name}' deleted successfully.\n")
            else:
                print(f"Contact '{delete_name}' not found.\n")
        elif n == "4":
            print("Exiting the contact book.\n")
            break
        else:
            print("Invalid option. Please try again.\n")

contact_book()