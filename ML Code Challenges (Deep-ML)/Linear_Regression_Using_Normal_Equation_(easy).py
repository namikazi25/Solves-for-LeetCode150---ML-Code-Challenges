import numpy as np
import numpy.linalg as linalg

# Write a Python function that performs linear regression using the normal equation.
# The function should take a matrix X (features) and a vector y (target) 
# as input, and return the coefficients of the linear regression model. 
# Round your answer to four decimal places,
# -0.0 is a valid result for rounding a very small number.

# Example:
# input: X = [[1, 1], [1, 2], [1, 3]], y = [1, 2, 3]
# output: [0.0, 1.0]
# reasoning: The linear model is y = 0.0 + 1.0*x, perfectly fitting the input data.



def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
    X = np.array(X)
    y = np.array(y)
    X_t = X.T
    XX_t = np.dot(X,X_t)
    XX_t_inv = np.linalg.pinv(XX_t)
    XX_t_inv_X_T = np.dot(X_t, XX_t_inv)
    theta = np.dot(XX_t_inv_X_T,y)
    theta = np.round(theta, 4).flatten().tolist()
    return theta
   
    # print(XX_t_inv)
    # theta = np.dot(XX_inv_minus_1,X_t_y)
    # print(round(theta))

def linear_regression_normal_equation_test():
    X = [[1, 1], [1, 2], [1, 3]]
    y = [1, 2, 3]
    theta = linear_regression_normal_equation(X, y)
    print(theta)

linear_regression_normal_equation_test()
