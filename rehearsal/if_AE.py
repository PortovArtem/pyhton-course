def if_AE(a, b, c):
    if a < c:
        if c < b:
            maximum = b
            two = c
            three = a
            return f'{three} {two} {maximum}'
        if c > b and b >= a:
            maximum = c
            two = b
            three = a
            return f'{three} {two} {maximum}'
        elif c > b and b < a:
            maximum = c
            two = a
            three = b
            return f'{three} {two} {maximum}'
    if a > c:
        if a < b:
            maximum = b
            two = a
            three = c
            return f'{three} {two} {maximum}'
        if a > b and b >= c:
            maximum = a
            two = b
            three = c
            return f'{three} {two} {maximum}'
        elif a > b and b < c:
            maximum = a
            two = c
            three = b
            return f'{three} {two} {maximum}'


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    print(if_AE(a, b, c))
