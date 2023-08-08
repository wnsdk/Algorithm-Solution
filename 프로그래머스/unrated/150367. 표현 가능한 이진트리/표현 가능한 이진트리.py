import bisect

def solution(numbers):
    answer = []
    arr = [1, 2, 4, 8, 16, 32, 64]
    
    for number in numbers:
        # number를 2진수로 표현한 문자열
        binary = str(bin(number))[2:]
        
        # 2^n - 1 == size (n은 트리의 높이)
        size = len(binary) + 1
        
        # 만일 자연수 n 중에 위 식을 만족할 수 없으면 size를 늘리기 (이진수 앞에 0 추가하기)
        if size not in arr:
            binary = '0' * (arr[bisect.bisect_left(arr, size)] - size) + binary
        
        if chk(binary):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer


def chk(tree):
    size = len(tree)
    
    if size == 1:
        return True
    
    # 루트가 더미 노드이면 자손 노드는 모두 더미 노드여야 함
    if tree[size // 2] == '0' and '1' in tree:
        return False
    
    if chk(tree[:size // 2]) and chk(tree[size // 2 + 1:]):
        return True
    
    return False
    