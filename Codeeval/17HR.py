t, c ,v = map(int, raw_input().split())
a = []
for i in xrange(t):
    a.append([int(i) for i in raw_input().split()])
for i in xrange(t):
    for j in xrange(1, c):
        a[i][j] += a[i][j-1]

for j in xrange(c):
    for i in xrange(1, t):
        a[i][j] += a[i-1][j]
    		
for _ in xrange(v):
    x1, y1, x2, y2 = map(lambda x:x - 1, map(int, raw_input().split()))
    if (x1, y1) > (x2, y2):
        (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
    if (x1, y1) == (0, 0):
        sol = a[x2][y2]
    elif x1 == 0:
        sol = a[x2][y2] - a[x2][max(0, y1-1)]
    elif y1 == 0:
        sol = a[x2][y2] - a[max(0, x1-1)][y2]
    else:
        sol = a[max(0, x1-1)][max(0, y1-1)] + a[x2][y2] - a[max(0, x1-1)][y2] - a[x2][max(0, y1-1)]
    print sol
