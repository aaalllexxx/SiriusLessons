s1 = set(map(lambda x: int(x), input().split()))
s2 = set(map(lambda x: int(x), input().split()))

print(s1.union(s2))
print(s1.intersection(s2))
