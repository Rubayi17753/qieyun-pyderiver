categories = ['母', '呼', '紐', '韻', '聲', 
    '調', '組', '音', 
    '等', '水', '攝', '轉', '尾', 
    '舒', '仄',]

def parse_query(s, query_delim=' '):

    def compute_truth(segm):

        if segm in ('舒聲', '仄聲'):
            segm = segm[0]

        if len(segm) > 1:
            value, category = segm[-1:], segm[-1]
            out = True if Hanzi.data[category] == value else False
        else:
            category = segm
            out = Hanzi.data[category]
        
        return out

    out = all(tuple(compute_truth(segm) for segm in s.split(query_delim)))
    return out