# Online Auction System

This is a simple command-line interface (CLI) based Online Auction System built using Python. The system allows users to register as either bidders or auctioneers, create auctions, place bids, and view ongoing auctions. This project uses in-memory data structures, so it doesn't require a database.

## Features

- **User Registration & Login**: Users can register and log in as bidders or auctioneers.
- **Auction Creation**: Auctioneers can create auctions by specifying item details, starting bid, and auction end time.
- **Bidding**: Bidders can place bids on active auctions.
- **View Auctions**: Users can view all ongoing auctions and see the current highest bid.
- **View Bids**: Users can view all bids placed on a specific auction.

## File Structure
```
/online_auction_system
│
├── main.py # The main entry point for running the CLI application
│
└── auction_system/
├── init.py # Makes the folder a Python package
├── models.py # Contains the data structures (User, Auction, Bid)
├── auction.py # Functions related to auction creation, viewing, and bidding
└── user.py # Functions related to user registration and login
```
###1)Register:
  -Run the program and select the "Register" option to create a new user account.
  -You can register as an auctioneer if you want to create auctions.
###2)Login:
  -After registering, log in to access the system.
  -Create Auction (Auctioneers only):
  -After logging in as an auctioneer, choose the "Create Auction" option.
  -Provide the item name, description, starting bid, and end time.

###3)Place Bid:
  -After logging in, choose the "Place Bid" option.
  -Enter the auction ID and the amount you wish to bid.

###4)View Auctions:
  -Choose the "View Auctions" option to see a list of all ongoing auctions.

###5)View Bids:
  -To see all bids for a specific auction, choose the "View Bids" option and enter the auction ID.

###6)Exit:
  -Choose the "Exit" option to quit the application.
