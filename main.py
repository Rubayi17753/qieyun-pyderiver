import src.parse_fanqie as parse_fanqie
import src.utils_fanqie as utils_fanqie

def main():

    def main1():

        monochars_fp = 'data/raw/monochars.tsv'

        json_template_fp = 'schemes/template.json'
        cat_inv_fp = 'data/category_inventory.tsv'

        df = parse_fanqie.main(monochars_fp)
        df = utils_fanqie.expand_with_categories(df)

        df3 = utils_fanqie.generate_json_template(df)
        df3.to_csv(cat_inv_fp, encoding='utf-8', sep='\t', index=False)

        df5 = utils_fanqie.category_inventory(df)
        df5.to_csv(cat_inv_fp, encoding='utf-8', sep='\t', index=False)



    main1()

if __name__ == '__main__':
    main()