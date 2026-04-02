"""
Your task is to implement simplified inventory tracking
system for a large retail store.
You are given a transaction log, where each log item corresponds to one of three transaction types: supply, sell or return. Log items are provided in the following format

* [“supply”, “<item_name>”, ”<count>”, ”<price>”] - the store receives <count> units of <item name>, and each item costs <prices>.
* [“sell”, “<item name>”, ”<count>”]  - the store sells <count units of <item name>. If the specified item is available at different prices, 
the cheapest ones should be sold first. It is guaranteed that the store will always have enough items to satisfy all sell transactions
* [“return”, “<item name>”, “<count>”, “<sell price>”, “<new price>”] - the store takes back <count> units of <item name>. 
It is guaranteed that the store has sold at least <count> units of <item_name> previously at price = <sell price> which are not returned yet. 
The returned items can be added back to inventory and sold later at price = <new price>


The tracking system should return the revenue from all sell transactions after processing the entire transaction log. 
Specifically, return an array representing the amount of money the store received from each sell transaction.

"""


import heapq

class InventoryTrackingSystem:
    def __init__(self):
        # Inventory will store item names with their prices as a min-heap
        self.inventory = {}
        # To track revenue from each sell transaction
        self.revenue = []

    def process_transaction(self, transaction):
        transaction_type = transaction[0]
        
        if transaction_type == "supply":
            item_name = transaction[1]
            count = int(transaction[2])
            price = float(transaction[3])
            if item_name not in self.inventory:
                self.inventory[item_name] = []
            for _ in range(count):
                heapq.heappush(self.inventory[item_name], price)
        
        elif transaction_type == "sell":
            item_name = transaction[1]
            count = int(transaction[2])
            total_revenue = 0.0
            for _ in range(count):
                price = heapq.heappop(self.inventory[item_name])
                total_revenue += price
            self.revenue.append(total_revenue)
        
        elif transaction_type == "return":
            item_name = transaction[1]
            count = int(transaction[2])
            new_price = float(transaction[3])
            if item_name not in self.inventory:
                self.inventory[item_name] = []
            for _ in range(count):
                heapq.heappush(self.inventory[item_name], new_price)

    def get_revenue(self):
        return self.revenue

def solution(logs):
    system = InventoryTrackingSystem()
    for transaction in logs:
        system.process_transaction(transaction)
    return system.get_revenue()

# Example log input
log = [
    ["supply", "item1", 10, 5],
    ["supply", "item1", 5, 6],
    ["sell", "item1", 8],
    ["return", "item1", 3, 4],
    ["sell", "item1", 7]
]

# Call the function with the example log input
print(solution(log))