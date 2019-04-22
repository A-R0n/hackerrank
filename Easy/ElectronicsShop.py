# I need to purchase 2 goods, 1 of each, for the maximum
# amount of money in summation without going over budget.
def getMoneySpent(keyboards, drives, b):
    import itertools 
    # the below product is technically o(n*m) but thanks to our
    # sort it should never reach that. 
    choices = list(itertools.product(keyboards, drives))
    sorted_choices_by_sum = sorted(choices, reverse=True, key=lambda x: x[0]+x[1])
    for val in sorted_choices_by_sum : # O(c) where c is num of actual tuples tried. 
        tot = val[0]+val[1]
        if tot <= b:
            return tot
    return -1