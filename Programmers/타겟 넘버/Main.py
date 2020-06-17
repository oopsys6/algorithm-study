# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0
    super = [0]
    for num in numbers:
        sub = []
        for sup in super:
            sub.append(sup + num)
            sub.append(sup - num)
        super = sub
        answer = super.count(target)
    return answer


print(solution([1, 1, 1, 1, 1], 3))