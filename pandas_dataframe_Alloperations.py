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
 
#(1) Extract the first 3 records 
print(df.head(3)) 
 
#(2) Extract the last 3 records 
print(df.tail(3)) 
 
#(3) Find the Shape of the DataFrame 
print(df.shape) 
#(4) Get the index Details 
print(df.index) 
 
#(5) Get the columns Details 
print(df.columns) 
 
#(6) Select rows and columns using loc[] 
print(df.loc['r1':'r4', 'Name':'English']) 
 
#(7) Select rows and columns using iloc[] 
print(df.iloc[1:4, 1:4]) 
 
#(8) Delete the rows 
print(df.drop(index=['r1','r2'])) 
 
#(9) Delete the column 
print(df.drop(columns=['English'], axis = 1)) 
 
#(10) Sort By Rows 
print(df.sort_index(axis = 0)) 
 
#(11) Sort By Columns 
print(df.sort_values(by = ["Name","Science"], inplace = False, na_position ='last')) 
 
#(l2) Apply any ranking method 
df["Rank"] =df["Science"].rank(method ='average') 
 
#(13) Filtering records based on conditions 
 
print(df.where((df.Mathematics>=90) & (df.Science>=90) & (df.English>=70), other='NA')) 
 
#(14) Add new column to the existing DataFrame 
 
df['Total'] = df[['Mathematics','Science','English']].sum(axis=1) 
 
print(df) 
 
#(15) Rename a Column 
print(df.rename(columns = {'Total':'Result'}))