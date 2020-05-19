if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg=0
    i=0
    for i in range(3):
        avg=avg+student_marks[query_name][i]
    print("{0:.2f}".format(avg/3))
