import json
import configs.filepaths as fp
import src.parse_fanqie as parse_fanqie
import src.utils_fanqie as utils_fanqie
import src.process_df as process_df

def main():

    current_scheme = 'sample_scheme'
    maps_fp = fp.scheme_dfs(current_scheme)

    def main1():

        df = parse_fanqie.main(fp.monochars)
        
        df = process_df.expand_with_categories(df)
        df = process_df.transliterate_segments(df, maps_fp)
        # stage2
        # collate
        df.to_csv(fp.fanqie_translit, encoding='utf-8', sep='\t', index=False)

        df5 = utils_fanqie.category_inventory(df)
        df5.to_csv(fp.cat_inv, encoding='utf-8', sep='\t', index=False)

    main1()

if __name__ == '__main__':
    main()