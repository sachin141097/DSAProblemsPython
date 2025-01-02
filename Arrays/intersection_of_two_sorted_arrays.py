def find_intersection(arr1, arr2):
    intersection_arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if not intersection_arr or intersection_arr[-1] != arr1[i]:
                intersection_arr.append(arr1[i])
            i += 1
            j += 1
        elif arr2[j] > arr1[i]:
            i += 1
        else:
            j += 1
    return intersection_arr


if __name__ == "__main__":
    arr1 = list(
        map(int, input(f"Enter the elements for array1 space separated: ").split())
    )
    arr2 = list(
        map(int, input(f"Enter the elements for array2 space separated: ").split())
    )
    ans = find_intersection(arr1, arr2)
    print(f"Intersection of array1 and array2 is {ans}")
