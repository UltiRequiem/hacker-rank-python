"""
You are given three integers x,y and z representing the dimensions
of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i,j,k)
on a 3D grid where the sum of i+j+k  is not equal to n.
Here, 0 < i < x; 0 < j < y; 0 < k < z.
"""


def represent_dimension_cuboid(x, y, z, n) -> list:
    return [
        [a, b, c]
        for a in range(x + 1)
        for b in range(y + 1)
        for c in range(z + 1)
        if a + b + c != n
    ]


if __name__ == "__main__":
    x, y, z, n = (int(input()) for _ in range(4))
    print(represent_dimension_cuboid(x, y, z, n))
