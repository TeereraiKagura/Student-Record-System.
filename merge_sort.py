def merge_sort(arr, key, reverse=False):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # Show the 'Divide' step
    print(f"DEBUG: Splitting list: {len(arr)} elements") 
    
    left = merge_sort(arr[:mid], key, reverse)
    right = merge_sort(arr[mid:], key, reverse)

    return merge(left, right, key, reverse)

def merge(left, right, key, reverse):
    result = []
    i = j = 0

    print(f"DEBUG: Merging {len(left)} items and {len(right)} items...")

    while i < len(left) and j < len(right):
        if reverse:
            condition = left[i][key] >= right[j][key]
        else:
            condition = left[i][key] <= right[j][key]

        if condition:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result