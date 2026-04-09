
"""
Here, each one of element in the result array b is the sum of its neighboring elements plus itself:
"""
def solution(a):
    b = [0] * len(a)
    
    for i in range(len(a)):
        prev = a[i-1] if i-1 >=0 else 0
        curr =a[i]
        next = a[i+1] if i+1 < len(a) else 0 
        b[i] = prev+curr+next
    return b


if __name__ == "__main__":
    print(solution([1,3,4,6]))


