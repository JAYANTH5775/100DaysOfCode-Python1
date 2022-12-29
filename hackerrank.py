list = []
n = int(input())
for i in range(n):
    list.append(input().split)

t = tuple(list)
print(hash(t))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

average = []
average = student_marks[query_name]
for i in range(average.len()):
    sum += average[i]

r = sum / average.len()

print(r)