categories = ['母', '呼', '紐', '韻', '聲', 
    '調', '組', '音', 
    '等', '水', '攝', '轉', '尾', 
    '舒', '仄',]

def generate_map_template():

    import json
    import configs.filepaths as fp
    import src.utils_fanqie as utils_fanqie

    json_template = utils_fanqie.generate_json_template()
    with open(fp.json_template, 'w', encoding='utf-8') as f:
        json.dump(json_template, f, indent='    ', ensure_ascii=False)