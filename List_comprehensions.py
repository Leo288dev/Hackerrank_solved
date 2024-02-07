if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    res = []
for k in range(0, x+1):
    for l in range(0, y+1):
        for m in range(0, z+1):
            if k + l + m != n:
                res.append([k, l, m])
res = [[k, l, m] for k in range(0, x+1) for l in range(0, y+1) for m in range(0, z+1) if k + l + m != n]
print(res)
