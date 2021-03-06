'''
1. Remove Duplicates from Sorted Array

my_list = [1, 1, 2]

def removeDuplicates(list_):
    if len(list_) == 0:
        return 0
    else:
        i = 1
        for j in range(1, len(list_)):
            if list_[j] != list_[j-1]:
                list_[i] = list_[j]
                i+=1
        return i
       

print(removeDuplicates(my_list)) 
'''

'''
2. Best Time to Buy and Sell Stock II
'''

prices_list = [7,1,5,3,6,4]

def maxProfit(prices):
    if len(prices) == 1:
        return 0
    else:
        i = 0
        j = 1
        sum = 0
        while j < len(prices):
            if prices[i] > prices[j]:
                j+=1
            else:
                dif = prices[j] - prices[i]
                sum += dif
                j += 1