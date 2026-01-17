import pandas as pd

def _dfc_col():

    from src.fetch_categories_ini import main as categories_ini

    dfcs = [categories_ini(),
            pd.read_csv('categories/finals.tsv', sep='\t'),  
            pd.read_csv('categories/tones.tsv', sep='\t'),   
        ]   
    cols = ['母', '韻', '聲']

    return dfcs, cols    

def expand_with_categories(df):

    dfcs, cols = _dfc_col()

    for dfc, col in zip(dfcs, cols):
        df = df.merge(dfc, how='left', on=col)
    df = df.drop(columns='韻合')

    return df

def _category_inventory(df):

    df = df.drop(columns='切')

    df2 = pd.DataFrame()
    df2['col'] = df.columns
    df2['val'] = [df[col].unique().tolist() for col in df.columns]
    df2 = df2.explode('val', ignore_index=True)

    print(df2)
    exit()

    return df2

def generate_json_template(df):

    df = _category_inventory(df)
    return df

def category_inventory(df):

    df = _category_inventory(df)
    df3 = df.groupby('val')['col'].agg(list).reset_index()
    return df3



