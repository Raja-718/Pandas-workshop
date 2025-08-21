#Different Methods of Creation of Series 
# Method 1: Using a list 
import pandas as pd
import numpy as np

a = pd.Series(['Raja','Rajesh','Radha',100])
print(a)


# Method 2: Using a Dictionary
b = pd.Series({'a':'Raja','b':'Ranjan'})
print(b)
# Method 3: Using a a NumPy array 
c = pd.Series(np.array([1,2,3,4,5,6,7,8,9]))
print(c)
# Method 4: Using Random Function
d = pd.Series(np.random.randn(5))
print(d)
# Method 5: Using a Scalar value
e = pd.Series(5,index=['a','b','c','d','e'])
print(e)