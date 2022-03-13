# **Data Science and Machine Learning Tool-Kit**
Important python for Data Science and Machine Learning scripts and functions:
- [Feature Engineering](#FE)
  - [Feature Interactions with pandas - GroupBy](#feature-interactions-groupby)
- [Other](#other)
  - [Plot subplots with a for loop](#subplots-forloop)
  - [Reduce dataframe memory usage](#reduce-df-mem-usage)
  - [Save submission files with submission time as filename](#subfiles-time)

<a name="FE"></a>
## **Feature Engineering**

<a name="feature-interactions-groupby"></a>
### **[Feature Interactions with pandas - GroupBy](feature_interactions_groupby.py)**
[##]::
<details><summary>Click to view code</summary>
<p>

```python
def feature_interactions(df, continuous_features=[], categorical_features=[]):
    
    assert len(continuous_features) > 0 and len(categorical_features) > 0,\
    "Please specify continuous and/or categorical variables"
    #if len(continuous_features) < 1:
        #print("Please specify continuous variables to be used.")
        
    for cat_feat in categorical_features:
        for cont_feat in continuous_features:
            df[f'{cat_feat}_interact_{cont_feat}_mean'] = df[cat_feat].map(df.groupby(cat_feat)[cont_feat].mean().to_dict())
            df[f'{cat_feat}_interact_{cont_feat}_count'] = df[cat_feat].map(df.groupby(cat_feat)[cont_feat].count().to_dict())
            df[f'{cat_feat}_interact_{cont_feat}_median'] = df[cat_feat].map(df.groupby(cat_feat)[cont_feat].median().to_dict())
            df[f'{cat_feat}_interact_{cont_feat}_sum'] = df[cat_feat].map(df.groupby(cat_feat)[cont_feat].sum().to_dict())
            df[f'{cat_feat}_interact_{cont_feat}_max'] = df[cat_feat].map(df.groupby(cat_feat)[cont_feat].max().to_dict())
            df[f'{cat_feat}_interact_{cont_feat}_min'] = df[cat_feat].map(df.groupby(cat_feat)[cont_feat].min().to_dict())
            df[f'{cat_feat}_interact_{cont_feat}_std'] = df[cat_feat].map(df.groupby(cat_feat)[cont_feat].std().to_dict())
            df[f'{cat_feat}_interact_{cont_feat}_var'] = df[cat_feat].map(df.groupby(cat_feat)[cont_feat].var().to_dict())
            df[f'{cat_feat}_interact_{cont_feat}_skew'] = df[cat_feat].map(df.groupby(cat_feat)[cont_feat].skew().to_dict())
            
    return df
```
</p>
</details>


<a name="other"></a>
## **Other**

<a name="subplots-forloop"></a>
### **Plot subplots with a for loop**
[##]::
<details><summary>Click to view code</summary>
<p>

```python
cols, rows = 3, 2

fig, axes = plt.subplots(rows, cols, figsize=(16,12))

columns = ['CreditLimit', 'CreditUsed', 'AmountRepaid', 'Balance', 'Fees', 'DaysOverdue']


for index, col in enumerate(columns):
    # new subplot with (i + 1)-th index laying on a grid
    plt.subplot(rows, cols, index + 1) 
    # drawing the plot
    sns.boxplot(x='cleared_cat', y=col, data=data)
    plt.title(f"{col}")

fig.suptitle("Numerical columns in relation to Cleared status")
plt.show()
```
</p>
</details>


<a name="reduce-df-mem-usage"></a>
### **Reduce dataframe memory usage**
[##]::
<details><summary>Click to view code</summary>
<p>

```python
def reduce_mem_usage(df, verbose=True):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    start_mem = df.memory_usage().sum() / 1024**2    
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)    
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose: print('Mem. usage decreased from {:5.2f} Mb to {:5.2f} Mb ({:.1f}% reduction)'.format(start_mem, end_mem, 100 * (start_mem - end_mem) / start_mem))
    return df
```
</p>
</details>


<a name="subfiles-time"></a>
### **Save submission files with submission time as filename**
[##]::
<details><summary>Click to view code</summary>
<p>

```python
from time import strftime

def get_current_timestamp():
    return strftime('%Y%m%d_%H%M%S')

submission_fname = 'submissions/stacking_%s.csv' % get_current_timestamp()
print(submission_fname)

submission_df.to_csv(submission_fname, index=False)
```
</p>
</details>