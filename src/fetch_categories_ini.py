import pandas as pd

def main():

    col_categories = ['全清1', '次清', '全濁1', '全清2', '全濁2', '次濁']

    df = pd.read_csv('categories/initials.tsv', sep='\t')
    
    df['母'] = df[col_categories].values.tolist()
    df2 = df[['母', '調', '組']]
    df2 = df2.explode('母', ignore_index=True)
    df2 = df2[~df2['母'].isna()]

    df3 = df[col_categories].transpose()
    df3['母'] = df3[df3.columns].values.tolist()
    df3 = df3.reset_index(names='音')
    df3['音'] = df3['音'].str[:2]
    df3 = df3[['母', '音']]
    df3 = df3.explode('母', ignore_index=True)
    df3 = df3[~df3['母'].isna()]

    df = df2.merge(df3, on='母', how='left')
    return df
