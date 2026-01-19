import pandas as pd

def main(monochars_fp):
    df = pd.read_csv(monochars_fp, sep='\t')
    df = parse_fanqie(df)

    return df

def parse_fanqie(df):
    df = df[['fanqie']].drop_duplicates()
    
    df = df.assign(
        initial=df['fanqie'].str[0], 
        rime=df['fanqie'].str.slice(1, -1), 
        tone=df['fanqie'].str[-1]
    )

    col_names = ['rounding', 'niu']
    varlists = (('合', '開'), ('A', 'B'))
    
    df[col_names] = None

    for col_name, varlist in zip(col_names, varlists):
        x = df['rime'].str[0]
        mask = x.isin(varlist)

        df[mask] = df[mask].assign(
            **{
                col_name: df['rime'][mask].str[0],
                'rime': df['rime'][mask].str.slice(1),
            }
        )

    # Tidy df up
    cols_en = ['fanqie', 'initial', 'rounding', 'niu', 'rime', 'tone']
    cols_zh = ['切', '母', '呼', '紐', '韻', '聲']
    df = df[cols_en]
    df.columns = cols_zh

    return df