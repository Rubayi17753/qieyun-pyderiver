class Hanzi():

    def __init__(self, initial, rounding, niu, final, tone):

        self.data = dict()

        self.data['母'] = initial

        self.data['韻'] = final

        self.data['呼'] = rounding
        self.data['紐'] = niu

        self.data['聲'] = tone
        self.data['舒'] = True if tone in '平上去' else False
        self.data['仄'] = True if tone in '上去入' else False

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