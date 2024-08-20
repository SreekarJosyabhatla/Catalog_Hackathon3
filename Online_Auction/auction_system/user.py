from auction_system.models import users, User

def register_user():
    username = input("Enter username: ")
    is_auctioneer = input("Are you an auctioneer? (yes/no): ").strip().lower() == 'yes'
    if username not in users:
        users[username] = User(username, is_auctioneer)
        print(f"User {username} registered successfully!")
    else:
        print(f"User {username} already exists!")

def login_user():
    username = input("Enter username: ")
    if username in users:
        print(f"Welcome back, {username}!")
        return users[username]
    else:
        print("User not found. Please register first.")
        return None
