# simple heap sort

def heapify(data, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and data[largest] < data[l]:
        largest = l
    if r < n and data[largest] < data[r]:
        largest = r
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest) 
 
def sort(data):
    n = len(data)
    for i in range(n//2 - 1, -1, -1):
        heapify(data, n, i)
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
    return data


if __name__ == "__main__":
    rand_data = [3, 2, 63, 54, 78, 31, 5, 24, 56, 37, 3999]
    result = sort(rand_data)
    print(result)