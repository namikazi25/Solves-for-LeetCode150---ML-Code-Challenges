import numpy as np

# Example:
# y = [0, 1, 1, 1, 0]
# print(gini_impurity(y))

# # Expected Output:
# # 0.48

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	unique, counts = np.unique(y, return_counts=True)
	gini_impurity = 1 - np.sum(np.square(counts / len(y)))
	
	return f"{gini_impurity:.3f}" # Return formatted to three decimal places


# gini_impurity = gini_impurity([0, 1, 1, 1, 0])
# print(gini_impurity)
