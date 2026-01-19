monochars = 'data/raw/monochars.tsv'
json_template = 'schemes/maps.json'
cat_inv = 'data/category_inventory.tsv'
fanqie_translit = 'data/fanqie_translit.tsv'

def scheme_dfs(current_scheme):
    maps = f'schemes/{current_scheme}/maps.json'

    return maps