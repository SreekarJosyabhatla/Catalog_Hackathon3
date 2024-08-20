import datetime

users = {}
auctions = {}
bids = {}

class User:
    def __init__(self, username, is_auctioneer=False):
        self.username = username
        self.is_auctioneer = is_auctioneer

class Auction:
    def __init__(self, auctioneer, item_name, description, starting_bid, end_time):
        self.auctioneer = auctioneer
        self.item_name = item_name
        self.description = description
        self.starting_bid = starting_bid
        self.end_time = end_time
        self.current_highest_bid = None

class Bid:
    def __init__(self, bidder, bid_amount, bid_time):
        self.bidder = bidder
        self.bid_amount = bid_amount
        self.bid_time = bid_time
