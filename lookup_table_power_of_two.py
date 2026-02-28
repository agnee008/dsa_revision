def power_of_two(x):
    powers_of_2 = [2 ** i for i in range(31)]
    return x in powers_of_2

def solution(numbers):
    count = 0
    n = len(numbers)
    
    for i in range(n):
        for j in range(i,n):
            if power_of_two(numbers[i] + numbers[j]):
                count += 1
    return count
    