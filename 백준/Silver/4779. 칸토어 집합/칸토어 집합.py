while True:
    try:
        n = int(input())
        length = pow(3, n)
        l = ['-'] * length


        def solve(start, size):
            global l

            if size:
                size //= 3

                solve(start, size)
                for i in range(start + size, start + size * 2):
                    l[i] = ' '
                solve(start + size * 2, size)


        solve(0, length)
        for item in l:
            print(item, end='')
        print()
    except:
        break
