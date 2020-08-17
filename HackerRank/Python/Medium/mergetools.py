def merge_the_tools(string, k):
    # your code goes here
    res = []
    for i in range(len(string)):
        if string[i] not in res:
            res.append(string[i])
        if (i+1)%k == 0:
            print(''.join(res))
            res = []


if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)