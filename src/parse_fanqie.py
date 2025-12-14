import pandas as pd

def main(monochars_fp):
    df = pd.read_csv(monochars_fp, sep='\t')
    df = parse_fanqie(df)

    return df

def parse_fanqie(df):
    df = df[['fanqie']].drop_duplicates()
    
    df = df.assign(
        initial=df['fanqie'].str[0], 
        final=df['fanqie'].str.slice(1, -1), 
        tone=df['fanqie'].str[-1]
    )

    for col_name, varlist in (('rounding', ('合', '開')), ('niu', ('A', 'B'))):
        x = df['final'].str[0]
        mask = x.isin(varlist)

        df[mask] = df[mask].assign(
            **{
                col_name: df['final'][mask].str[0],
                'final': df['final'][mask].str.slice(1),
            }
        )

    return df
