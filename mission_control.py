missions = []
mission_details = {}

def add_mission(missions, mission_details, name, details):
    # TODO: Implement this function
    # pass
    
    # Add the mission's name to the LIST
    missions.append(name)
    
    # Use the mission's name as the KEY in the dictionary
    # and store its details as the VALUE
    mission_details[name] = details
    
    print(f"\n Mission '{name}' added successfully.")

def update_mission(mission_details, name, key, value):
    # TODO: Implement this function
    # pass
    print("UPDATE FUNCTION IS RUNNING")
    
    # Check if mission exist before updating
    if name in mission_details:
        
        #Update mission details
        mission_details[name][key] = value
        
        print(f"\n Mission '{name}' updated successfully.")
    else:
        print(f"\n Mission '{name}' not found.")

def display_missions(missions, mission_details):
    # TODO: Implement this function
    # pass
    if not missions:
        print("\n No missions found.")
        return
    
    #Loop through each mission's name
    for name in missions:
        print(f"\n Mission Name: {name}")
        
        print(f" Destination: {mission_details[name].get('Destination', 'N/A')}")
        
        print(f" Launch Date: {mission_details[name]['Launch Date']}")
        
        print(f" Crew Members: {mission_details[name]['Crew']}")

def list_astronauts(mission_details):
    # TODO: Implement this function
    pass

# Main menu loop
while True:
    print("\nSpace Mission Management System")
    print("1. Add Mission")
    print("2. Update Mission")
    print("3. Display Missions")
    print("4. List Astronauts")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        name = input("Enter mission name: ")
        destination = input("Enter destination: ")
        launch_date = input("Enter launch date: ")
        crew = input("Enter crew members (comma-separated): ")
        details = {
            "Destination": destination,
            "Launch Date": launch_date,
            "Crew": crew
        }
        add_mission(missions, mission_details, name, details)

    elif choice == '2':
        name = input("Enter mission name to update: ")
        key = input("Enter detail to update (Destination/Launch Date/Crew): ")
        value = input(f"Enter new value for {key}: ")
        update_mission(mission_details, name, key, value)

    elif choice == '3':
        display_missions(missions, mission_details)

    elif choice == '4':
        astronauts = list_astronauts(mission_details)
        print("\nAll Astronauts:")
        for astronaut in astronauts:
            print(f"- {astronaut}")

    elif choice == '5':
        print("Exiting Space Mission Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
