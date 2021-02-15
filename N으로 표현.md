프로그래머스 - N으로 표현 (동적 계획법)

###### 문제 설명

아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

##### 제한사항

- N은 1 이상 9 이하입니다.
- number는 1 이상 32,000 이하입니다.
- 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
- 최솟값이 8보다 크면 -1을 return 합니다.

##### 입출력 예

| N    | number | return |
| ---- | ------ | ------ |
| 5    | 12     | 4      |
| 2    | 11     | 3      |

##### 입출력 예 설명

예제 #1
문제에 나온 예와 같습니다.

예제 #2
`11 = 22 / 2`와 같이 2를 3번만 사용하여 표현할 수 있습니다.

---

참고한 Solution

```python
def solution(N, number):
    answer = -1
    num_set = [set() for x in range(8)]
    
    for idx, i in enumerate(num_set):
        i.add(int(str(N)*(idx+1)))
    
    for i in range(1, len(num_set)):
        for j in range(i):
            for x in num_set[j]:
                for y in num_set[i-j-1]:
                    num_set[i].add(x+y)
                    num_set[i].add(x-y)
                    num_set[i].add(x*y)
                    if y != 0:
                        num_set[i].add(x//y)
        if number in num_set[i]:
            answer = i+1
            return answer
        
    return answer
```

동적 계획법에 대한 접근 방법을 전혀 몰랐어서 여러 블로그를 참고했다.

먼저 숫자의 사용 횟수를 담을 리스트를 선언해준다.

문제에서 제시된 8보다 크다는 점을 이용해서 최대 사용 횟수를 8로 정해서 리스트를 만든다.

반복문을 돌면서 이전 사용 횟수로 사칙 연산한 결과를 계속해서 누적해나가는 방식이며,

반복되는 값을 저장하여 사용한다는 점에서 동적 계획법의 풀이라고 이해할 수 있겠다.