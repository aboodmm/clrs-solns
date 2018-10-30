""" 
Abdul Rashad - @aboodmm
Insertion sort procedure
Sorts randomly generated list in non-increasing order
"""

import os
import random

a = []

for i in range(0, 5):
	a.append(random.randint(1, 10))

def insertion_sort_reverse(a):
	for j in range(1, len(a)):
		key = a[j]
		i = j - 1
		while i > -1 and a[i] < key:
			a[i + 1] = a[i]
			i = i - 1
		a[i + 1] = key
	return a

print("Input list", a)

print("Sort decreasing", insertion_sort_reverse(a))


