# First version of a quicksort algorithm.

import time

def sort(data: list):
    if len(data) == 1:
        return data
    pivot_point = data[-1]
    less_than = []
    more_than = []
    res1 = []
    res2 = []
    result = None

    # divide
    for i, e in enumerate(data):
        if e < pivot_point:
            less_than.append(data[i])
        if e > pivot_point:
            more_than.append(data[i])

    # re-call oneself
    if less_than:
        res1 = sort(less_than)
    if more_than:
        res2 = sort(more_than)
    result = res1 + [pivot_point] + res2
    return result

def divide(data: list, begin: int, end: int):
    '''partitions a list on a selected pivot value
       puts the pivot value to its correct place
    '''
    pivot = data[end]
    j = begin - 1
    for i in range(begin, end):
        print(i)
        if data[i] <= pivot:
            j += 1
            data[j], data[i] = data[i], data[j]

    data[j + 1], data[end] = data[end], data[j + 1]
    return j + 1

def sort_iterative(data: list, begin: int, end: int):
    #if end > len(data): end = len(data)
    stack = []
    stack.append(begin)
    stack.append(end)
    
    while end >= 0:
        print("data:  " + str(data))
        print("stack: " + str(stack))

        begin = stack.pop()
        end = stack.pop()
        pivot = divide(data, begin, end)
        
        if pivot - 1 > begin:
            stack.append(begin)
            stack.append(pivot - 1)

        if pivot + 1 < end:
            stack.append(pivot + 1)
            stack.append(end)
    
    return data


if __name__ == "__main__":
    rand_data = [3, 2, 63, 54, 78, 31, 5, 24, 56, 37, 7]
    print(rand_data)
    
    result = sort_iterative(rand_data, 0, len(rand_data) - 1)
    print(result)
