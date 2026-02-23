def vector_add(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]

def vector_subtract(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]

def dot_product(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))

def scalar_multiply(scalar, v):
    return [scalar * x for x in v]


v1 = [1, 2, 3]
v2 = [4, 5, 6]

print("Addition:", vector_add(v1, v2))
print("Dot Product:", dot_product(v1, v2))