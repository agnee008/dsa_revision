class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x
        while l<=r:
            mid = (l+r)//2
            mid_sqaured = mid * mid
            if mid_sqaured == x:
                return mid
            elif mid_sqaured< x:
                l = mid + 1
            else:
                r= mid -1
        return r

# Example usage:
solution = Solution()
print(solution.sqrt(16))  # Output should be 4
print(solution.sqrt(12))  # Output should be 3
print(solution.sqrt(0))   # Output should be 0
