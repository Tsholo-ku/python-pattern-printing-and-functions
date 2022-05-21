#Excercise 1: printing a star

def star(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


star(5)


#Exercise 2: After 180 degree rotation

def star2(n):
	
	# number of spaces
	k = 2*n - 2

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 2
	
		# inner loop to handle number of columns
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

star2(5)

#Execise 3: Printing a triangle

def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

triangle(5)

#Exercise 4: Printing a number pattern

def numpat(n):
	
	# initialising starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# re assigning num
		num = 1
	
		# inner loop to handle number of columns
		for j in range(0, i+1):
		
				# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\r")


numpat(5)

#Exercise 5: Printing number pattern without reassigning

def contnum(n):
	
	# initializing starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# not re assigning num
		# num = 1
	
		# inner loop to handle number of columns
		for j in range(0, i+1):
		
			# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\r")


contnum(5)



