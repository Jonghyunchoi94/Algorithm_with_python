numbers = [3, 30, 34, 5, 9]
"""
Build-up

고려 사항

1. 같은 자릿수만 비교하는 것이 아니다.
2. 시간 복잡도 고려

1차 시도 : DFS   (Recursion error 발생)  참고 : Permutation 함수도 마찬가지로 시간 초과
2차 시도 : 선택정렬 (시간 초과 발생)  -> N^2 보다 효율적인 정렬 방법 탐색 필요
3차 시도 : 문자열 비교 개념  ( ASCII값으로 치환 후 비교 ) 

숫자 형태의 문자열 비교 예시

'60' < '9'    <= 맨 앞 자리수가 9가 크므로 '9'가 '60'보다 크다.
같은 자릿수로 비교하게 하기 위해 문자열을 늘려야 한다.

"""
def solution(numbers):
    answer = list(map(str, numbers))                 # numbers는 0 ~ 1000 까지의 숫자
    answer.sort(key = lambda x:x*3  , reverse=True)  # 문자열을 3번 곱한다?  '3' * 3  => '333'
    return str(int(''.join(answer)))                 # 모든 숫자가 0일 때 '0000000' => '0'으로 출력하여야 한다.

print(solution(numbers))