from auction_system.models import auctions, bids, Auction, Bid
import datetime

def create_auction(user):
    if not user.is_auctioneer:
        print("Only auctioneers can create auctions.")
        return

    item_name = input("Enter item name: ")
    description = input("Enter item description: ")
    starting_bid = float(input("Enter starting bid: "))
    end_time = datetime.datetime.strptime(input("Enter end time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")

    auction_id = len(auctions) + 1
    auctions[auction_id] = Auction(user.username, item_name, description, starting_bid, end_time)
    print(f"Auction created successfully with ID {auction_id}")

def place_bid(user):
    auction_id = int(input("Enter auction ID: "))
    if auction_id not in auctions:
        print("Auction not found.")
        return

    auction = auctions[auction_id]
    if datetime.datetime.now() > auction.end_time:
        print("Auction has already ended.")
        return

    bid_amount = float(input("Enter your bid amount: "))
    if auction.current_highest_bid and bid_amount <= auction.current_highest_bid.bid_amount:
        print("Bid must be higher than the current highest bid.")
        return

    bid = Bid(user.username, bid_amount, datetime.datetime.now())
    bids[auction_id] = bids.get(auction_id, []) + [bid]
    auction.current_highest_bid = bid
    print(f"Bid placed successfully by {user.username} for {bid_amount}!")

def view_auctions():
    for auction_id, auction in auctions.items():
        print(f"Auction ID: {auction_id}, Item: {auction.item_name}, Current Highest Bid: {auction.current_highest_bid.bid_amount if auction.current_highest_bid else 'No bids yet'}")

def view_bids(auction_id):
    if auction_id in bids:
        for bid in bids[auction_id]:
            print(f"Bidder: {bid.bidder}, Amount: {bid.bid_amount}, Time: {bid.bid_time}")
    else:
        print("No bids for this auction.")
