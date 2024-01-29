def f(d):
    if d == 1:
        return ['*']

    nd = d // 3
    stars = f(nd)
    ret = []

    for star in stars:
        ret.append(star * 3)
    for star in stars:
        ret.append(star + ' ' * nd + star)
    for star in stars:
        ret.append(star * 3)
        
    return ret


n = int(input())
print('\n'.join(f(n)))
