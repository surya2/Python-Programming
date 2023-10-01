import copy
import math


def merge(arr_list, start, middle, end):
    left_list = copy.deepcopy(arr_list)
    right_list = copy.deepcopy(arr_list)
    left_ptr = start
    right_ptr = middle + 1
    list_ptr = start
    while left_ptr <= middle and right_ptr <= end:
        if left_list[left_ptr] <= right_list[right_ptr]:
            arr_list[list_ptr] = left_list[left_ptr]
            left_ptr += 1
        else:
            arr_list[list_ptr] = right_list[right_ptr]
            right_ptr += 1
        list_ptr += 1

    while left_ptr <= middle:
        arr_list[list_ptr] = left_list[left_ptr]
        left_ptr+=1

    while right_ptr <= end:
        arr_list[list_ptr] = right_list[right_ptr]
        right_ptr+=1


def mergeSort(arr_list, start, end):
    if (end - start) == 1:
        if arr_list[end] < arr_list[start]:
            temp = arr_list[end]
            arr_list[end] = arr_list[start]
            arr_list[start] = temp
        return

    if start == end:
        return

    middle = int((start + end) / 2)
    mergeSort(arr_list, start, middle)
    mergeSort(arr_list, middle + 1, end)

    merge(arr_list, start, middle, end)


arr = [34, 89, 100, 345, 2, 1, 784, 92, 78, 101, 389, 3, 67]
mergeSort(arr, 0, len(arr) - 1)
print(arr)
