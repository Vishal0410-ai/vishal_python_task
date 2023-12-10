#!/usr/bin/env python
# coding: utf-8

# ### Question 1 

# In[1]:


import pandas as pd
import numpy as np

def generate_car_matrix(df):
    result_df = df.pivot(index='id_1', columns='id_2', values='car')
    np.fill_diagonal(result_df.values, 0)
    
    return result_df

df = pd.read_csv('dataset-1.csv')
new_df = generate_car_matrix(df)


# In[2]:


new_df


# ### Question 2
# 

# In[3]:


def get_type_count(df):
    
    def categorize_car_value(value):
        if value <= 15:
            return 'low'
        elif 15 < value <= 25:
            return 'medium'
        else:
            return 'high'

    df['car_type'] = df['car'].apply(categorize_car_value)
    type_count = df['car_type'].value_counts().to_dict()
    type_count = dict(sorted(type_count.items()))
    
    return type_count

type_count = get_type_count(df)
type_count


# ### Question 3

# In[4]:


def get_bus_indexes(df):
    threshold = 2 * df['bus'].mean()
    bus_indexes = df[df['bus'] > threshold].index.tolist()
    bus_indexes.sort()
    
    return bus_indexes

bus_indexes = get_bus_indexes(df)
bus_indexes


# ### Question 4

# In[5]:


def filter_routes(df):
    grouped_df = df.groupby('route')['truck'].mean()
    filtered_routes = grouped_df[grouped_df > 7].index.tolist()
    filtered_routes.sort()
    
    return filtered_routes
filtered_routes = filter_routes(df)
filtered_routes


# ### Question 5

# In[8]:


def multiply_matrix(df):
    def modify_value(value):
        if value > 20:
            return round(value * 0.75, 1)
        else:
            return round(value * 1.25, 1)
    df = df.applymap(modify_value)
    return df
modified_df = multiply_matrix(new_df)


# In[9]:


modified_df


# ### Question 6

# In[11]:


df2 = pd.read_csv('dataset-2.csv')


# In[12]:


def check_timestamp_completeness(df1):
    # Convert startDay and endDay to datetime format
    df['startDay'] = pd.to_datetime(df['startDay'], errors='coerce')
    df['endDay'] = pd.to_datetime(df['endDay'], errors='coerce')

    # Create a boolean series indicating if each (id, id_2) pair has incorrect timestamps
    result = df.groupby(['id', 'id_2']).apply(lambda group: not (
        group['startDay'].dt.dayofweek.min() == 0 and  # Monday
        group['endDay'].dt.dayofweek.max() == 6 and  # Sunday
        group['startTime'].min() == '00:00:00' and
        group['endTime'].max() == '23:59:59'
    ))

    return result
result = check_timestamp_completeness(df2)
result


# In[ ]:




