#!/usr/bin/env python
# coding: utf-8

# # Life Expectancy By Country

# Over the course of the past few centuries, technological and medical advancements have helped increase the life expectancy of humans. However, as of now, the average life expectancy of humans varies depending on what country you live in.
# 
# In this project, we will investigate a dataset containing information about the average life expectancy in 158 different countries. We will specifically look at how a country's economic success might impact the life expectancy in that area.

# ## Access the Data

# 1. We've imported a dataset containing the life expectancy in different countries. The data can be found in the variable named `data`.
# 
#    To begin, let's get a sense of what this data looks like. Print `data.head()` to see the first 5 rows of the dataset.
#    
#    Look at the names of the columns. What other pieces of information does this dataset contain?
#    

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")


# 2. Let's isolate the column that contains the life expectancy and store it in a variable named `life_expectancy`.


# In[6]:


life_expentancy = data["Life Expectancy"]


# ## Find the Quantiles

# 3. We can now use NumPy functions on that column! Let's use the `np.quantile()` function to find the quartiles of `life_expectancy`. Store the result in a variable named `life_expectancy_quartiles` and print the results.

# In[7]:


life_expectancy_quartiles = np.quantile(life_expentancy, [0.25,0.5,0.75])
print (life_expectancy_quartiles)


# 4. it seems like some of the data is fairly close together a quarter of the data is between `72.5` years and `75.4` years.
# 
#   
#    Plot the histogram by using the following two lines of code. Does it look how you expected?
#    
#  
#    ```

# In[8]:


plt.hist(life_expentancy)
plt.show()


# 5. Let's take a moment to think about the meaning of these quartiles. If your country has a life expectancy of `70` years, does that fall in the first, second, third, or final quarter of the data?
# 

# ## Splitting the Data by GDP

# 6. GDP is a measure of a country's wealth. Let's now use the GDP data to see if life expectancy is affected by this value.
# 
#    Let's split the data into two groups based on GDP. If we find the median GDP, we can create two datasets for "low GDP countries" and "high GDP countries".
#    
#    To start, let's isolate the GDP column and store it in a variable named `gdp`. This should be similar to how we
#    isolated the life expectancy column.

# In[9]:


gdp = data["GDP"]


# 7. We now want to find the median GDP. You can use NumPy's `np.median()` function, but since the median is also a quantile, we can call `np.quantile()` using `0.5` as the second parameter.
# 
#    Store the median in a variable named `median_gdp`. Print that variable to see the median.

# In[11]:


median_gdp = np.quantile(gdp,0.5)
print (median_gdp)


# 8. Let's now grab all of the rows from our original dataset that have a GDP less than or equal to the median. The following code will do that for you:
# 
#    Do the same for all of the rows that have a GDP higher than the median. Store those rows in a variable named `high_gdp`.
#    
#    The line of code should look almost identical to the one above, but you should change the `<=` to `>`.
#    

# In[12]:


low_gdp = data[data['GDP']<=median_gdp]
high_gdp = data[data ['GDP']>= median_gdp]


# 9. Now that we've split the data based on the GDP, let's see how the life expectancy of each group compares to each other.
# 
#  

# In[20]:


low_gdp_quartiles = np.quantile(low_gdp["Life Expectancy"], [0.25, 0.5, 0.75])
print (low_gdp_quartiles)


# 10. Find the quartiles of the high GDP countries. This should look very similar to the last line of code you wrote. Print the results.

# In[21]:


high_gdp_quartiles = np.quantile(high_gdp["Life Expectancy"], [0.25,0.5,0.75])
print (high_gdp_quartiles)


# ## Histogram and Conclusions

# 11. By looking at the quantiles, you should get a sense of the spread and central tendency of these two datasets. But let's plot a histogram of each dataset to really compare them.
# 

# In[19]:


plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label ="High GDP", color = "green")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP", color = "Pink")
plt.legend()
plt.show()


# 12. We can now truly see the impact GDP has on life expectancy.
# 
#     Once again, consider a country that has a life expectancy of `70` years. means that the country is in low gdp group that belong to first fourth quarter

# In[ ]:




