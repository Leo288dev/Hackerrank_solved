if __name__ == '__main__':
    s = 0
    name = ''
    n = int(input(''))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        s = float(sum(scores))
        average = s / len(scores)
        student_marks[name] = scores
        student_marks[name + '_avg'] = average

    query_name = input(str('')).strip()
    for i in student_marks.keys():
        if query_name == i:
            print(f"{student_marks[query_name + '_avg']:<.2f}")


