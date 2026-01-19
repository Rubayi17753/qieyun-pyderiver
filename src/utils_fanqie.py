import pandas as pd

def _dfc_col():

    from src.fetch_categories_ini import main as categories_ini

    dfcs = [categories_ini(),
            pd.read_csv('categories/rimes.tsv', sep='\t'),  
            pd.read_csv('categories/tones.tsv', sep='\t'),   
        ]   
    cols = ['母', '韻', '聲']

    return dfcs, cols    

def _category_inventory():

    dfcs, cols = _dfc_col()
 
    df_out = pd.DataFrame()
    data_out = list()
    
    for dfc, col in zip(dfcs, cols):
        for col2 in dfc.columns:
            data_out.append({'col' : col2, 'val' : dfc[col2].unique().tolist()})

    df_out = pd.DataFrame.from_dict(data_out)
    df_out = df_out.explode('val').reset_index()
    return df_out

def _generate_json_template_whole():

    dfcs, cols = _dfc_col()
    data_out = dict()
    
    for dfc, col in zip(dfcs, cols):
        for col2 in dfc.columns:
            x = dfc[col2].unique().tolist()

            if 'nan' in x:
                x.remove('nan')

            data_out[col2] = x

    return data_out

def generate_json_template():

    import configs.configs as conf

    cats = conf.categories
    segms = conf.segments

    template_whole = _generate_json_template_whole()
    
    def _func1(v, k):
        return [f'{v2}{k}' for v2 in v]
        
    template_part = {k : _func1(v, k)
                    for k, v in template_whole.items() 
                    if k in cats}

    template_part = {f'{segm} {cat}' : dict.fromkeys(v, '') 
                    for segm, cat, v in zip(segms, cats, template_part.values())}

    return template_part

def category_inventory(df):

    df = _category_inventory()
    df3 = df.groupby('val')['col'].agg(list).reset_index()
    return df3



