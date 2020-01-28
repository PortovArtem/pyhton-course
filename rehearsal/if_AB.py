def if_AB(n):
    if 11<=n%100<=14:
        return f'{n} bochek'
    ostatok = n % 10
    if ostatok == 1:
        return f'{n} bochka'
    if 1 < ostatok < 5:
        return f'{n} bochki'
    if 5<= ostatok <= 9 or ostatok == 0:
        return f'{n} bochek'


if __name__ == '__main__':
    n = int(input())

    print(if_AB(n))
