'''
Random Experiment
'''

from random import choice

'''
RE of a single coin flip
'''

def coin_flip():
    # return choice('HT') # equivalent alternative
    return choice(['H', 'T'])

# print(coin_flip())


'''
RE: the count of heads in 20 flips
'''
def twenty_flips():
    flips = []

    for _ in range(20):
        flips.append(coin_flip())

    return flips

# print(twenty_flips())


'''
How many heads would you "Expect" in 20 flips?
0.5 * 20 = 10
'''



'''
Union
'''
list1
list2
list3