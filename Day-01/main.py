# Day 1 - Report Repair
# https://adventofcode.com/2020/day/1
# ===================================

# Part 1
def twoNumberSumProduct(array, num):
    array.sort()
    i = 0
    j = len(array) - 1

    results = 0
    while i < j:
        if array[i] + array[j] == num:
            results = array[i] * array[j]
            break
        elif array[i] < array[j] == num:
            i += 1
        else:
            j -= 1
    return results

# Part 2
def threeNumberSumProduct(array, targetSum):
    array.sort()
    i = 0 
    results = 0
    while i < len(array) - 2:
        j = i + 1
        while j < len(array) - 1:
            k = j + 1
            while k < len(array):
                if array[i] + array[j] + array[k] == targetSum:
                    results = array[i] * array[j] * array[k]
                k += 1
            j+=1
        i+=1
    return results

# I/O
def fileRead(fname):
    content_array = []
    with open(fname) as f:
        for line in f:
                content_array.append(int(line))
    return content_array

# main
data = fileRead('input.txt')

results = twoNumberSumProduct(data, 2020)
print("The product of the two entries that sum to 2020:")
print(results)

results = threeNumberSumProduct(data, 2020) 
print("The product of the three entries that sum to 2020:")
print(results)