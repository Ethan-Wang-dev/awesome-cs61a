def g(lst):
    max_num = lst[0]

    for num in lst:
        max_num = max(max_num, num)

    return max_num
    
g([1,4,3,2])

# To see the space complexity of running the above
# see https://tinyurl.com/y6sh4ekr



def g(lst):
    if len(lst) == 1: 
        return lst[0]

    return max(lst[0], g(lst[1:]))
    
    
g([1,4,3,2])

# To see the space complexity of running the above
# see https://tinyurl.com/mr6rpwb2