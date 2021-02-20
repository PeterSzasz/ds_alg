
def sort(data):
    '''Simple cocktail sort.'''
    swapped = True
    while swapped:
        swapped = False
        n = len(data)
        for i in range(n-1):
            if data[i] > data[i+1]:
                tmp = data[i]
                data[i] = data[i+1]
                data[i+1] = tmp
                swapped = True
                print(data)
            j = n - i - 1
            if i != j and data[j] < data[j - 1]:
                tmp = data[j]
                data[j] = data[j - 1]
                data[j - 1] = tmp
                swapped = True
                print(data)
    return data


if __name__ == "__main__":
    rand_data = [3, 2, 63, 54, 78, 31, 5, 24, 56, 37, 3999]
    print(rand_data)
    print(sort(rand_data))
