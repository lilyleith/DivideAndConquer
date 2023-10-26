#!/usr/bin/env python
# coding: utf-8

# In[8]:


def MergeSort(p, q):
    if len(p) <= 1:
        return p, q

    mid = len(p) // 2

    left, left2= MergeSort(p[:mid], q[:mid])
    right, right2 = MergeSort(p[mid:], q[mid:])
    p_sort, q_sort = Merge(left, right, left2, right2)

    return p_sort, q_sort

def Merge(left, right, left2, right2):
    i = j = 0
    merged = []
    resort = []
    while len(left) > i and len(right) > j:
        if int(left[i]) <= int(right[j]):
            merged.append(left[i])
            resort.append(left2[i])
            i += 1
        else:
            merged.append(right[j])
            resort.append(right2[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    resort += left2[i:]
    resort += right2[j:]

    return merged, resort

def MergeInversions(left, right):
    num_inversions = 0
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1            
        else:
            result.append(right[j])
            j += 1
            num_inversions += (len(left) - i)

    if j == len(right) and i < len(left):
        result += left[i:]
    if i == len(left) and j < len(right):
        result += right[j:]
    return result, num_inversions

def InversionCount(arr):

    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inversions = InversionCount(arr[:mid])
    right, right_inversions = InversionCount(arr[mid:])
    merged, merged_inversions = MergeInversions(left, right)
    total_inversions = left_inversions + right_inversions + merged_inversions
    return merged, total_inversions


t = int(input())
tcount = 0
results = [None] * t
while tcount < t:
    n = int(input())
    ncount = 0
    q = []
    p = []
    while ncount < n:
        q.append(int(input()))
        ncount += 1
    ncount = 0
    while ncount < n:
        p.append(int(input()))
        ncount += 1
    anw1, anw2 = MergeSort(p,q)
    trash, result = InversionCount(anw2)
    results[tcount] = result
    tcount += 1
for i in range(t):
    print(results[i])


# In[ ]:




