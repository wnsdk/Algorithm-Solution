def f(n):
    if n == 1:
        return ['*']

    L = []
    Stars = f(n//3)

    for star in Stars:
        L.append(star * 3)
    for star in Stars:
        L.append(star + ' ' * (n//3) + star)
    for star in Stars:
        L.append(star * 3)

    return L

n = int(input())
print('\n'.join(f(n)))