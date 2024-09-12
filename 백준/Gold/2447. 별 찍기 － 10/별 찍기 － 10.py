def f(n):
    if n == 1:
        return ['*']

    ret = []
    stars = f(n // 3)
    for star in stars:
        ret.append(star * 3)
    for star in stars:
        ret.append(star + ' ' * (n // 3) + star)
    for star in stars:
        ret.append(star * 3)

    return ret


print('\n'.join(f(int(input()))))