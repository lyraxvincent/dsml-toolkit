def feature_combinations(df: pd.DataFrame, features: list):
    for i in tqdm(range(len(features))):
        if i < len(features) - 1:
            df[f'{features[i]}_X_{features[i+1]}'] = df[features[i]].astype(str) + '_X_' + df[features[i+1]].astype(str)
            
            for feat in set(features).difference({features[i]}):
                if '_X_' not in feat:
                    df[f'{features[i]}_X_{feat}'] = df[features[i]].astype(str) + '_X_' + df[feat].astype(str)
                    
    # and now for all features
    df['master_combination_X_'] = df[features].agg(sum, axis=1)

    return df

