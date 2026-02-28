"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). It is not allowed to load weight more than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:

Input: weights = [2,4,6,1,3,10], days = 4

Output: 10

Explanation:
1st day: [2]
2nd day: [4,6]
3rd day: [1,3]
4th day: [10]

Hint - Will use minimum number of ships
"""

def ShipPackage(weights, days):
    l,r = max(weights), sum(weights)
    res = r
    
    def canShip(cap):
        currCap = cap
        ships = 1
        for w in weights:
            if w - currCap < 0:
                ships += 1
                if ships > days:
                    return False
                currCap = cap
            currCap -= w
        return True
    while l<=r:
        cap = (l+r)//2
        if canShip:
            res = min(res, cap)
            r = cap - 1
        else:
            l = cap + 1
    return res    