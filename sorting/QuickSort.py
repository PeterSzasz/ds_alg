import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from core.stack import stack

def sort(data: list):
    '''Simple recursive version of a quicksort algorithm.'''
    if len(data) == 1:
        return data
    pivot_point = data[-1]
    less_than = []
    more_than = []
    res1 = []
    res2 = []
    result = None

    for i, e in enumerate(data):    # divide
        if e < pivot_point:
            less_than.append(data[i])
        if e > pivot_point:
            more_than.append(data[i])

    if less_than:                   # re-call oneself
        res1 = sort(less_than)
    if more_than:
        res2 = sort(more_than)
    result = res1 + [pivot_point] + res2
    return result

def divide(data: list, begin: int, end: int):
    '''Partitions a list on a selected pivot value,
       puts the pivot value to its correct place.
    '''
    pivot = data[end]
    j = begin - 1
    for i in range(begin, end):
        if data[i] <= pivot:
            j += 1
            data[j], data[i] = data[i], data[j]

    data[j + 1], data[end] = data[end], data[j + 1]
    return j + 1

def sort_iterative(data: list, begin: int, end: int):
    '''Iterative version of quicksort using a stack.'''
    s = stack()
    s.push(begin)
    s.push(end)
    print(f"init: {s}")

    while end > 1:
        print(f"data:  {str(data)}")
        print(f"stack: {s}")

        end = s.pop()
        begin = s.pop()
        pivot = divide(data, begin, end)
        print(f"pivot: {pivot}, begin: {begin}, end: {end}")
        
        if pivot - 1 > begin:
            s.push(begin)
            s.push(pivot - 1)
        
        if pivot + 1 < end:
            s.push(pivot + 1)
            s.push(end)
            
    return data


if __name__ == "__main__":
    rand_data = [3, 2, 63, 54, 78, 31, 5, 24, 56, 37, 7]
    print(rand_data)
    
    result = sort_iterative(rand_data, 0, len(rand_data) - 1)
    print(result)
