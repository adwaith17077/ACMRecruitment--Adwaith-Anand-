Program: Find the second largest number in a list

	def second_largest(arr):
	    
			largest = second = -9999999
	    for num in arr:
	        if num > largest:
	            second = largest
	            largest = num
	        elif num > second:
	            second = num
	    return second
	n = int(input("Enter number of elements: "))
	arr = list(map(int, input("Enter numbers: ").split()))
	
	print("Second largest:", second_largest(arr))
in the given code i have found an error in the elif statement which when the given list has 2 or more same largest element, the variable second will take the the vaalue of largest value
hence we rewrite the statetment as 'elif num>second and num!=0:' and i also dont there is a need to have a variable 'n' as u can input the no of elemennts as you like in the next statement using map function
so the corrected code according to me will be:

	def second_largest(arr):
	    
			largest = second = -9999999
	    for num in arr:
	        if num > largest:
	            second = largest
	            largest = num
	        elif num > second and num!=0:
	            second = num
	    return second
	arr = list(map(int, input("Enter numbers: ").split()))
	
	print("Second largest:", second_largest(arr))
