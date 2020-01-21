def max_3(a,b,c):
    if a<b:
        if b>c:
            return b
        else:
            return c
    else:
        if a>c:
            return a
        else:
            return c



if __name__ == '__main__':
    one = int(input())
    two = int(input())
    three = int(input())

    print(max_3(one, two, three))

