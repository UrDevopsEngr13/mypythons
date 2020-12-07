from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

def bidding():
  all_bids = []
  bidding_is_on = True
  while bidding_is_on:
    bids = {}
    bidder = input("Enter the bidder's name:  ")
    bid_price = float(input("Enter bid price: $"))
    bids["name"] = bidder
    bids["bid price"] = bid_price
    all_bids.append(bids)
    
    continue_bid = input("Are there any bidders? 'yes' or 'no' : ")
    clear()
    if continue_bid == 'no':
      highest_bid = 0
      highest_bidder =""
      for bid in all_bids:
        if bid["bid price"] > highest_bid:
          highest_bid = bid["bid price"]
          highest_bidder = bid["name"]
      print(f"Winning bidder is {highest_bidder} with a bid of ${highest_bid}")
      bidding_is_on = False

bidding()


