def solution(n):
    answer = ''
    result = '수박' * 2
    if n % 2 == 0:
        answer = '수박' * int((n/2))
    else:
        answer = '수박' * int((n/2))
        answer += "수"


    return answer
