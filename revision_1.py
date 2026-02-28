from itertools import combinations

def wordSearch(board:list[list[int]], word: str):
    rows, cols = len(board[0]), len(board)
    path = set()
    def dfs(r,c,i):
        if i == len(word):
            return True
        if (r<0 or c<0 or r>rows or c>cols or word[i] != board[r][c] or (r,c) not in path):
            return False
        path.add(r,c)
        
        res= (dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i-1) or dfs(r,c-1,i-1))
        
        path.remove(r,c)
        
        return res
        
    for r in range(rows):
        for c in range(cols):
            if dfs(r,c,0):
                return True
    return False
    




def wordOperation(s):
    wordMap = {'zero':'0','one': '1'....}
    res = []
    i = 0
    while i <= len(s):
        for word in wordMap:
            if word.startswith(word,i):
                res.append(str(wordMap[word]))
                i+=len(word)
                break
            else:
                if word.startswith('plus'):
                    res.append('+')
                    i+=4
                if word.startswith('minus'):
                    res.append('-')
                    i+=5
                else:
                    i+=1
    return "".join(res)

def solve(input_str):
    expression = wordOperation(input_str)
    return eval(expression)

def totalVisistslessthantarget(visits, target):
    if sum(visits)!= target:
        return -1
    valid_combinations = 0
    
    for r in range(1, len(visits) + 1):
        for comb in combinations(visits,r):
            if sum(comb) < target:
                valid_combinations += 1
    return valid_combinations

class TreeNode:
    def __init__(self, left = None, right = None):
        