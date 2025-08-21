
# Method 1: using a single tuple 
import pandas as pd
a = pd.DataFrame(('raja','Rajesh',100))
print(a)

# Method 2: using a single list 
b = pd.DataFrame(['Rajnish','Ramesh','Bipesh'])
print(b)
# Method 3: using a list of list 
c = pd.DataFrame([['Raja',25],['Rajnish',23],['Rajesh',25]], columns=['Name','Age'])
print(c)
 
# Method 4: using dictionary of lists 
d = pd.DataFrame({ 'Name': ['John', 'Mark', 'Joseph'], 
                   'Age': [29, 24, 28, ], 
                   'City': ['Sydney', 'Paris', 'New York']}) 
print(d) 
# Method 5: using Numpy arrays 
import numpy as np
e = pd.DataFrame({ 
                'name':['Jane','John','Ashley','Mike'], 
                'category':['A','D','C','D'], 
                'val1':np.random.random(4).round(2), 
                'val2':np.random.randint(1,10, size=4), 
                'val3':np.array(['Aditya','Emily',40,50])}) 
print(e) 
 
#Method 6: using Series 

g = pd.DataFrame(pd.Series(['Jit', 'Purn', 'Arp', 'Jot'])) 
print(g) 
