# def word_to_num(s):

#     word_map = {'zero' : 0, 'one' : 1, 'two' : 2}
#     i=0
#     output = []
#     n = len(s)
#     while i<n:
#         for word in word_map:
#             if s.startswith(word,i):
#                 output.append(str(word_map[word]))
#                 i+=len(word)
#                 break
#             else:
#                 if s.startswith('plus', i):
#                     output.append('+')
#                     i+=4
#                 if s.startswith('minus', i):
#                     output.append('-')
#                     i+=5
#                 else:
#                     i+=1
                    
#     return ''.join(output)

# def solve(input_str):
#     expression = word_to_num(input_str)
#     return eval(expression)



def wordMap(s):
    word_map = {'zero': 0, 'one' : 1}
    i = 0
    n = len(s)
    output = []
    while i<n:
        for word in word_map:
            if word.startswith(word,i):
                output.append(str(word_map[word]))
                i+=len(word)
                break
            else:
                if word.startswith('plus',i):
                    output.append('+')
                    i+=4
                if word.startswith('minus',i):
                    output.append('-')
                    i+=5
                else:
                    i+=1
    return ''.join(output)


def solve(input_str):
    expression = wordMap(input_str)
    return eval(expression)



