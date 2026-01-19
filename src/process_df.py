import configs.configs as conf
import json

def expand_with_categories(df):

    import src.utils_fanqie

    dfcs, cols = src.utils_fanqie._dfc_col()
    for dfc, col in zip(dfcs, cols):
        df = df.merge(dfc, how='left', on=col)
    df = df.drop(columns='韻合')
    df.drop(columns='Unnamed: 3')
    return df

def transliterate_segments(df, fp_maps):

    with open(fp_maps, 'r', encoding='utf-8') as f:
        maps_data = json.load(f)

    cats_segms = [k.split() for k in maps_data.keys()]

    for segm, cat in cats_segms:
        df[cat] = df[cat] + cat
        df[segm] = df[cat].map(maps_data[f'{segm} {cat}'])

    return df