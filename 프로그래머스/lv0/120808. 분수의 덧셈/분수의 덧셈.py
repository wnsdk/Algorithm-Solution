def solution(numer1, denom1, numer2, denom2):
    a = numer1 * denom2 + numer2 * denom1
    b = denom1 * denom2
    
    for i in range(2, 1000000):
        while a % i == 0 and b % i == 0:
            a /= i
            b /= i
    
    answer = [a, b]
    return answer