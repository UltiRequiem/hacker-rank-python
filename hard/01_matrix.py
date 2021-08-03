from re import sub


n, m = map(int, input().split())

a, b = [input() for _ in range(n)], ""

for z in zip(*a):
    b += "".join(z)

print(sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))
