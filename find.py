
import argparse

page_dict = []

def load_pagedict():
    f = open("papers_index.txt")
    for line in f:
        minrow, maxrow, conference = line.strip().split()
        page_dict.append([int(minrow), int(maxrow), conference])

def search(keyword):
    print("query: ", keyword)
    keys = keyword.strip().split("_")
    f = open("papers.txt")
    cnt = 1
    res_cnt = 0
    for line in f:
        line = line.strip().lower()
        exist = True
        for k in keys:
            if k.lower() not in line:
                exist = False
                break
        if exist:
            for pc in page_dict:
                if cnt >= pc[0] and cnt <= pc[1]:
                    print("-------------------------------")
                    print(pc[2] + "("+ str(cnt) +")"+ ":" + line)
                    # print("-------------------------------")
                    res_cnt += 1
        cnt += 1

    print("have got %d results." % (res_cnt))

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='paper search')
    parser.add_argument('-q',type=str,help='query, delimated by _', default='dialogue generation')
    args = parser.parse_args()

    load_pagedict()

    search(args.q)
