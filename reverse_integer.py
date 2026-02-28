def reverse(x: int) -> int:
    # Define the bounds for a 32-bit signed integer
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # Determine if the number is negative
    sign = -1 if x < 0 else 1
    
    # Take the absolute value of the number for reversing
    x = abs(x)
    
    reversed_num = 0
    while x != 0:
        # Pop the last digit from the number
        pop = x % 10
        x //= 10
        
        # Check for overflow before updating reversed_num
        if (reversed_num > (INT_MAX - pop) // 10):
            return 0
        
        reversed_num = reversed_num * 10 + pop
    
    return sign * reversed_num

# Example usage:
print(reverse(123))    # Output: 321
print(reverse(-123))   # Output: -321
print(reverse(120))    # Output: 21
print(reverse(0))      # Output: 0
