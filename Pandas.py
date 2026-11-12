# In[1]:
#creating a series from list
import pandas as pd
a = [1,7,2]
myvar=pd.Series(a)
print(myvar)

# In[2]:
#creating labels
import pandas as pd
a = [1,7,2]
myvar=pd.Series(a, index=["x","y","z"])
print(myvar)

# In[6]:
#creating series
import pandas as pd
a = [12,20,30]
myvar=pd.Series(a , index = ["a","b","c"], name = "example series")
print(myvar)

# In[11]:
##creating a series from dictionary
import pandas as pd
s1= pd.Series({"x":1,"y":2,"z":3})
print(s1)
print()
calories = {"day1":240 ,"day2":380 ,"day3":390}
myvar = pd.Series(calories)
print(myvar)

# In[14]:
#DataFrames
import pandas as pd
data ={
    "calories":[420,380,290],
    "duration":[50,40,45]
}
df=pd.DataFrame(data)
print(df.loc[0])
print()
print(df.loc[[0,1]])

# In[21]:
#Named Index
import pandas as pd
data = {
    "calories":[600,300,480],
    "duration":[50,60,20]
}
df = pd.DataFrame(data , index=["day1","day2","day3"])
print(df)

# In[25]:
#Data cleaning
data={
    "A":[1,2,3,None,5],
    "B":[None,2,3,4,5],
    "c":[1,2,None,4,5]
}

df=pd.DataFrame(data)
print("Original Data:\n",df)
print()
df_cleaned=df.dropna()
print("Cleaned data:\n",df_cleaned)

# In[26]:
#fill missing data
data={
    "A":[1,2,3,None,5],
    "B":[None,2,3,4,5],
    "c":[1,2,None,4,5]
}

df=pd.DataFrame(data)
print("Original Data:\n",df)
df_cleaned=df.fillna(0, inplace=True)
print("Cleaned data:\n",df_cleaned)

# In[29]:
#use aggregate[mean,some]
data={
    "A":[1,2,3,None,5],
    "B":[None,2,3,4,5],
    "c":[1,2,None,4,5]
}

df=pd.DataFrame(data)
print("Original Data:\n",df)
df_mean=df.fillna(df.mean(), inplace=True)
print(df_mean)
