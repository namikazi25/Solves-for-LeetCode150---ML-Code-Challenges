def matrix_dot_vector(a , b):
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
        if len(a[0]) != len(b):
            return -1
        
        c = [0] * len(a)
        
        for i in range(len(a)):
            for j in range(len(b)):
                c[i] += a[i][j] * b[j]
        return c

print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))