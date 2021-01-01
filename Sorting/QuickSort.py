# First version of a quicksort algorithm.

def quicksort(data: list):
    for digi in data:
        print(digi, end=": ")
        print(id(digi), end=", ")
    print("")
    if len(data) == 1:
        return data
    pivot_point = data[-1]
    less_than = []
    more_than = []
    result = None
    res1 = []
    res2 = []

    # divide
    for i, e in enumerate(data):
        if e < pivot_point:
            less_than.append(data[i])
        if e > pivot_point:
            more_than.append(data[i])

    # re-call oneself
    if less_than:
        res1 = quicksort(less_than)
    if more_than:
        res2 = quicksort(more_than)
    result = res1 + [pivot_point] + res2
    return result


if __name__ == "__main__":
    rand_data = [3, 2, 63, 54, 78, 31, 5, 24, 56, 37, 3999]
    result = quicksort(rand_data)
    print(result)
    [print(id(d), end=", ") for d in result]
