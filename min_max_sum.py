def miniMaxSum(arr):
	min_sum = 0
	max_sum = 0
	n=len(arr)
	arr.sort()
	j=n-1
	for i in range(n-1):
		min_sum += arr[i]
		max_sum += arr[j]
		j-=1
	print(min_sum," ",max_sum)

arr=[1, 2, 3, 4, 5]

miniMaxSum(arr)