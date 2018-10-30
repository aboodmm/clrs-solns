""" 
Abdul Rashad - @aboodmm
Linear search 
The loop invariant for this procedure can be expressed as
'while current element is not search argument'
"""
a = [1, 2, 3, 4, 9001, 5]

def linear_search(arr, arg):
	for i in range(0, len(arr)):
		print("current item", arr[i])
		if arr[i] == arg:
			break

linear_search(a, 9001)
