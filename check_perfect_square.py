def checkPerfectSquare(n:int):
    l,r = 0, n
    
    while l<=r:
        mid = (l+r) // 2
        mid_square = mid * mid
        if mid_square == n:
            return True
        if mid_square < n:
            l = mid + 1
        else:
            r = mid -1
    return False