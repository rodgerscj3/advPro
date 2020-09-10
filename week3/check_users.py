def check_users(current_users, new_users):

    pass

    while new_users in current_users:
        print("You must choose a new username.")
    
    if new_users not in current_users:
        print(f"{new_users.title()}, You chose a great username!"
            
if __name__ == "__main__":
    
    current_users = ['mateo','harambe', 'wakanda', 'mamba', 'bananas']

    new_users = ['mercury', 'ringo', 'mamba', 'hannibal', 'harambe']

check_users(current_users, new_users)