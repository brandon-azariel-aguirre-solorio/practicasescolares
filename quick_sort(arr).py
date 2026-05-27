def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


numbers = [8, 3, 1, 7, 0, 10, 2]
sorted_numbers = quick_sort(numbers)

print(sorted_numbers)
