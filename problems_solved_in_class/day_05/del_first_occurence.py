def first_occ(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            for j in range(i, len(arr) - 1):
                arr[j] = arr[j + 1]
            return arr[:len(arr) - 1]
    else:
        return arr