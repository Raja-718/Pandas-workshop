
#Creating a Sample DataFrame 
import pandas as pd 
df = { 
       "Name":["Ram","Sam","Scott","Ann","John"], 
       "Mathematics" :[80,90,85,70,95], 
       "Science" :[85,95,80,90,75], 
       "English" :[90,85,80,70,95] 
              } 
index_labels=['r1','r2','r3','r4','r5'] 
df = pd.DataFrame(df ,index=index_labels) 
 
print(df) 
 
 
#Perform statistical operations 
#1) sum() 
# Add new column Sum  
df['Sum'] = df['Mathematics'] + df['Science'] + df['English'] 
print(df) 
 
# Select 1 to 3 columns to sum 
df['Sum']=df.iloc[:,1:3].sum(axis=1) 
print(df) 
 
# Sum columns Fee and Discount for row from r2 to r3 
df['Sum'] = df.loc['r2':'r4',['Mathematics','Science']].sum(axis = 1) 
print(df) 
 
print(df['Sum'].mean()) 
 
print(df['Sum'].median()) 
 
print(df['Sum'].mode()) 
 
print(df['Sum'].count()) 
 
print(df['Sum'].std()) 
 
print(df['Sum'].max()) 
 
print(df['Sum'].min()) 
 
 
 
#Descriptive Statistics 
print(df.describe()) 
 
# summary statistics of character column 
print(df.describe(include=['object'])) 
 
# summary statistics of all the column 
print(df.describe(include='all'))