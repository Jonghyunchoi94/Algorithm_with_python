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

"""
파이썬 sort 함수  => 시간복잡도 O(NlogN)   [팀소트]

# sort 함수
sort(*, key=None, reverse=False)
key는 인자 하나를 받아들이는 함수를 지정하는데, 각 리스트 요소에서 
비교 키를 추출하는 데 사용된다.

# lambda 함수
lambda 인자 : 표현식
익명 함수라고 부르기도 하며 함수 이름 없이 한줄로 간단하게 만드는 방법

"""



print(solution(numbers))