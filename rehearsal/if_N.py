def if_N(a,b):
    if a==0 and b==0:
        return 'INF'
    elif a==0:
        return 'NO'
    else:
        x=-b/a
        if x%1==0:
            return int(x)
        else:
            return 'NO'

if __name__ == '__main__':
    a=int(input())
    b=int(input())

    print(if_N(a,b))