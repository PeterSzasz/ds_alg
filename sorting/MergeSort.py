# Most basic version of a Merges sort.

def sort(data):
    if len(data) > 1:
        # split input
        mid = len(data)//2
        left_half = data[:mid]
        right_half = data[mid:] 
        sort(left_half)
        sort(right_half) 
        i = 0
        j = 0
        k = 0
        # merging together
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1
        # checking if any element was left
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
 
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
    return data


if __name__ == "__main__":
    rand_data = [3, 2, 63, 54, 78, 31, 5, 24, 56, 37, 3999]
    result = sort(rand_data)
    print(result)
