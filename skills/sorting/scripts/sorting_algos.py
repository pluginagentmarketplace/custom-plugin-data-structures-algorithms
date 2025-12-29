#!/usr/bin/env python3
def quicksort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr)//2]
    return quicksort([x for x in arr if x < pivot]) + [x for x in arr if x == pivot] + quicksort([x for x in arr if x > pivot])

def mergesort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr)//2
    return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))

def merge(l, r):
    result = []
    while l and r: result.append((l if l[0] < r[0] else r).pop(0))
    return result + l + r
