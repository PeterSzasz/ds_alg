# Simple Bubble sort. First try.

import time

def sort(data: list):
    swapped = True
    while swapped:
        swapped = False
        print(data)
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                tmp = data[i]
                data[i] = data[i+1]
                data[i+1] = tmp
                swapped = True
    return data


if __name__ == "__main__":
    rand_data = [3, 2, 63, 54, 78, 31, 5, 24, 56, 37, 3999]
    start = time.time()
    result = sort(rand_data)
    stop = time.time()
    print(stop - start)
    print(result)
