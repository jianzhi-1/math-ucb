arr = [(0, 0, -6), (0.1, 0.1, -5.89483),  (0.3, 0.3, -5.65014), (0.6, 0.6, -5.17788), (1, 1, -4.28172), (1.1, 1.1, -3.99583)]
while len(arr) > 0:
    newarr = []
    for i in range(len(arr) - 1):
        newarr.append((arr[i][0], arr[i + 1][1], (arr[i + 1][2] - arr[i][2])/(arr[i + 1][1] - arr[i][0])))
    arr = newarr
    print(arr)
