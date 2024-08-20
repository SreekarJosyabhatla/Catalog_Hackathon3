from auction_system.user import register_user, login_user
from auction_system.auction import create_auction, place_bid, view_auctions, view_bids

def main():
    current_user = None

    while True:
        print("\n1. Register\n2. Login\n3. Create Auction\n4. Place Bid\n5. View Auctions\n6. View Bids\n7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            current_user = login_user()
        elif choice == '3' and current_user:
            create_auction(current_user)
        elif choice == '4' and current_user:
            place_bid(current_user)
        elif choice == '5':
            view_auctions()
        elif choice == '6':
            auction_id = int(input("Enter auction ID to view bids: "))
            view_bids(auction_id)
        elif choice == '7':
            break
        else:
            print("Invalid choice or not logged in. Please try again.")

if __name__ == "__main__":
    main()
