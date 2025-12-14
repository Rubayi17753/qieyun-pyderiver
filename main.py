import src.parse_fanqie as parse_fanqie

def main():

    monochars_fp = 'data/monochars.tsv'
    df = parse_fanqie.main(monochars_fp)
    print(df)
    exit()

if __name__ == '__main__':
    main()