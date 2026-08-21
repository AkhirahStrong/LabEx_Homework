# This function adds a new contact to the contacts dictionary.
# It receives:
# contacts = the dictionary holding all contacts
# name = the person's name
# phone = the person's phone number
# email = the person's email address
def add_contact(contacts, name, phone, email):

    contacts[name] = {"phone": phone, "email": email}

    # Confirm that the contact was added.
    print(f"Contact {name} added successfully.")


# This function removes a contact from the contacts dictionary.
def remove_contact(contacts, name):

    # Check whether the name exists as a key in the contacts dictionary.
    if name in contacts:

        # 'del' removes the key AND its associated value from the dictionary.
        del contacts[name]

        print(f"Contact {name} removed successfully.")

    # If the name is not found in the dictionary, run this instead.
    else:
        print(f"Contact {name} not found.")


# This function displays all contacts currently stored.
def display_contacts(contacts):

    # An empty dictionary is considered False.
    # A dictionary containing data is considered True.
    #
    # So this means:
    # "If there are contacts in the dictionary..."
    if contacts:

        print("\nContact List:")

        # .items() gives us BOTH the key and value from the dictionary.
        #
        # name = dictionary key
        # info = dictionary value
        #
        # Example:
        # name = "John"
        # info = {"phone": "555-1234", "email": "john@email.com"}
        for name, info in contacts.items():

            # Access the phone and email from the inner dictionary.
            #
            # info["phone"] gets the phone number
            # info["email"] gets the email address
            print(
                f"Name: {name}, "
                f"Phone: {info['phone']}, "
                f"Email: {info['email']}"
            )

    # If the contacts dictionary is empty, display this message.
    else:
        print("Contact list is empty.")


# main() controls the overall program.
def main():

    # Create an empty dictionary to store contacts.
    #
    # Eventually it could look like:
    #
    # {
    #     "John": {
    #         "phone": "555-1234",
    #         "email": "john@email.com"
    #     }
    # }
    contacts = {}

    # Create an empty SET for favorite contacts.
    #
    # A set only stores unique values.
    # This prevents the same person from appearing multiple times.
    favorite_contacts = set()


    # Keep the program running until the user chooses Exit.
    while True:

        # Display the menu.
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Add to Favorites")
        print("5. Display Favorites")
        print("6. Exit")

        # Get the user's menu choice.
        # input() returns a string, which is why we compare
        # choice to "1", "2", etc. instead of integers.
        choice = input("Enter your choice (1-6): ")


        # OPTION 1: Add a contact
        if choice == "1":

            # Ask the user for the contact information.
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")

            # Send that information to our add_contact() function.
            add_contact(contacts, name, phone, email)


        # OPTION 2: Remove a contact
        elif choice == "2":

            # Ask which contact should be removed.
            name = input("Enter name to remove: ")

            # Call the remove_contact() function.
            remove_contact(contacts, name)


        # OPTION 3: Display all contacts
        elif choice == "3":

            # Pass the contacts dictionary to the display function.
            display_contacts(contacts)


        # OPTION 4: Add a contact to favorites
        elif choice == "4":

            # Ask which contact should become a favorite.
            name = input("Enter name to add to favorites: ")

            # First make sure the person actually exists
            # in the contacts dictionary.
            if name in contacts:

                # .add() adds an item to a SET.
                #
                # Because favorite_contacts is a set,
                # adding the same name twice will NOT create duplicates.
                favorite_contacts.add(name)

                print(f"{name} added to favorites.")

            else:
                print(f"Contact {name} not found.")


        # OPTION 5: Display favorite contacts
        elif choice == "5":

            print("\nFavorite Contacts:")

            # Loop through every name stored in the set.
            for name in favorite_contacts:
                print(name)


        # OPTION 6: Exit the program
        elif choice == "6":

            print("Thank you for using Contact Manager. Goodbye!")

            # break exits the while True loop.
            # This ends the program.
            break


        # If the user enters anything other than 1-6,
        # this section runs.
        else:
            print("Invalid choice. Please try again.")


# Python automatically creates the special variable __name__.
#
# When this file is run directly:
# __name__ == "__main__"
#
# This prevents main() from automatically running if this
# Python file is imported into another Python program.
if __name__ == "__main__":

    # Start the program.
    main()