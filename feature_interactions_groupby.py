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
