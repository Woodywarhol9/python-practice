# 파이썬을 파이썬답게
목차
1. [int 다루기](#`int`-다루기)
2. [str 다루기](#`str`-다루기)
3. [Iterable 다루기](#`Iterable`-다루기)
4. [seqeunce 다루기](#`sequence`-다루기)
5. [Itertools/Combinations 모듈 활용하기](#`Itertools`/`Combinations`-모듈-활용하기)
6. [기타 팁](#기타-팁)

### `int` 다루기
#### 몫과 나머지 구하기
- `divmod`와 `unpacking`을 이용해서 쉽게 표현 가능

``` python
a = 7
b = 5
print(a//b, a%b)
```

<center>↓</center>

``` python
a = 7
b = 5
print(*divmod(a, b))
```

</br>

#### 진법 변환
- `int(x, base)`으로 10진수 ↔ N 진수를 쉽게 변환 가능


``` python
num = '3212'
base = 5

answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)
print(answer)
```

<center>↓</center>

``` python
num = "3212"
base = 5
answer = int(num, 5)
print(answer)
```

</br>

### `str` 다루기
#### 문자열 정렬하기
- 좌측/가운데/우측 기준 정렬 : `ljust`, `center`, `rjust` 메소드 활용
``` python
s = "가나다라"
n = 7
print(f'{s:<{n}}') # 변수를 조건으로 주려면 {} 안에다 줘야함.
print(f'{s:^{n}}')
print(f'{s:>{n}}')
```
<center>↓</center>

``` python
s = '가나다라'
n = 7

print(s.ljust(n)) # 좌측 정렬
print(s.center(n)) # 가운데 정렬
print(s.rjust(n)) # 우측 정렬
```
</br>

#### 자주쓰는 문자열 활용하기
- 자주쓰는 문자열은 string에서 상수로 관리한다.

``` python
import string 

print(string.ascii_lowercase) # 소문자 abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters) # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 숫자 0123456789
```
</br>

### `Iterable` 다루기
#### 원본을 유지한 채 정렬된 리스트를 구하기
- `sort()` 함수를 사용해서 리스트의 원소를 정렬하면 원본의 순서도 변경한다.
- 따라서 `deep copy` 수행 후 `sort()`를 수행해야하는 번거로움이 있다.   
- `sorted()`의 경우 기존 리스트의 순서를 변경하지 않고도 정렬할 수 있다!


``` python
list1 = [3, 2, 5, 1]
list2 = [i for i in list1] # 또는 copy.deepcopy를 사용
list2.sort()
print(list2)
```

<center>↓</center>

``` python
list1 = [3, 2, 5, 1]
list2 = sorted(list1)
print(list1)
```

</br>

#### 2차원 리스트 뒤집기
- 2차원 리스트를 뒤집기 위해서는 보통 2중 `for`문을 사용합니다.    
- 하지만 `zip`과 `unpacking`을 이용하면 코드 한 줄로 리스트를 뒤집을 수 있습니다.

``` python
def solution(mylist):
    answer = [[0 for col in range(len(mylist))] for row in range(len(mylist[0]))]
    for i, lst in enumerate(mylist):
        for j, num in enumerate(lst):
            answer[j][i] = num          
    return answer
```

<center>↓</center>

``` python
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
print(*mylist)
print(list(zip(*mylist)))
print(new_list)
```

</br>

#### `zip` 함수?
- `zip` 함수는 주어진 `iterables`의 요소들을 모아 `iterator`를 만듭니다.   
- 위 코드에선 `[1, 2, 3] , [4, 5, 6], [7, 8, 9]`의 원소로   
- `(1, 4, 7), (2, 5, 8), (3, 6, 9)`를 구성합니다.
- `zip`의 특성을 활용하면, 여러 `iterable`을 동시에 순회할 때 사용할 수 있습니다.

``` python
mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)

(1, 40)
(2, 50)
(3, 60)
```

</br>

#### `i` 번째 원소와 `i + 1` 번째 원소 접근 - `zip` 활용 가능
- 보통 `len`, `index`를 통해서 각 `i`, `i + 1` 원소에 접근하지만,  
- `python`에서는 `zip`을 이용해 각 원소에 접근할 수 있습니다.

``` python
def solution(mylist):
    answer = []
    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i] - mylist[i+1]))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    
    print(solution(mylist))
```

<center>↓</center>

``` python
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]): # 길이가 짧은 mylist[1:]이 끝날 때 까지 진행
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    
    print(solution(mylist))
```
- `zip` 함수에 서로 길이가 다른 `iterable`이 인자로 사용되는 경우, 길이가 짧은 쪽의 순회가 끝날 때 까지 반복됩니다.

</br>

#### 모든 멤버의 type 변환하기
- `iterable`의 모든 멤버의 `type`을 변환할 때 `map`을 이용하면 `for`문 사용 없이 일괄 변경할 수 있습니다.
``` python
list1 = ["1", "100", "33"]
list2 = [int(i) for i in list1]
print(list2)
```

<center>↓</center>

``` python
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
print(list2)
```

</br>

### `sequence` 다루기
#### `sequence` 멤버를 하나로 이어붙이기
- 시퀀스의 멤버들을 하나의 `str`로 이어붙여야 할 때,
- `str.join(iterable)`를 활용하면 더 간단하게 가능하다.

``` python
my_list = ['1', '100', '33']
answer = ''
for value in my_list:
    answer += value
```

<center>↓</center>

``` python
my_list = ['1', '100', '33']
answer = ''.join(my_list)
```

</br>

#### 곱셈 연산 `*`를 통해 반복하기
- `for`문을 이용해서 기존 `str`, `list`에 더해가는 방법도 있지만   
- `*` 연산자를 활용하면 더 간단하게 표현할 수 있다.

``` python
answer = ''
n = 3
for _ in range(n):
    answer += 'abc'
print(answer)
```

<center>↓</center>

``` python
n = 3
answer= "abc" * n
print(answer)
```
</br>

### `Itertools`/`Combinations` 모듈 활용하기
#### 곱집합(Cartesian product) 구하기
- 여러 `iterable`에서 곱집합을 구하기 위해서 다중 `for`문을 사용하는 방법도 있지만,   
- `itertools.product`를 이용하면 간단하게 곱집합을 구할 수 있습니다.
``` python
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)
```
<center>↓</center>

``` python
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))
```

</br>

#### 2차원 리스트를 1차원 리스트로 만들기
- 단순 반복문을 이용할 수도 있지만 python에서는 다양한 방법이 존재합니다.
- `sum` 함수
- `itertools.chain` 함수
- `itertools`과 `unpacking`
- `list comprehension`
- `reduce` 함수
  - 실행 속도? :  `sum`이 가장 느리고, 나머지는 비슷
  - [참고 링크](https://blog.winterjung.dev/2017/04/21/list-of-lists-to-flatten)
``` python
my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for element in my_list:
    answer += element
```
<center>↓</center>

``` python
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))
```
- 각 원소의 길이가 동일한 경우엔 `numpy.flatten`을 사용할 수 있습니다.

``` python
# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()
```

</br>

#### 순열과 조합
`itertools`의 `combinations`, `permutations`을 이용해 쉽게 구할 수 있습니다.

``` python
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
```

</br>

#### 원소가 등장한 개수 세기
- 보통 반복문을 통해서 원소에 접근해 개수를 세는 방법을 사용하지만,
- `collections.Counter`를 사용하면 이 코드를 간략하게 만들 수 있습니다.
``` python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100])  # =  raise KeyError
```

</br>

### 기타 팁
#### `List Comprehension`
- `list` 생성 및 순회를 한 줄로 가능
``` python
mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]
print(answer)
```

</br>

#### flag 대신 `for - else` 활용하기
- `for`문의 결과로 `True`, `False`를 나눠서 다른 행동을 하고 싶을 때, 
- flag 설정 대신 `for - else`를 활용할 수 있습니다.
  
``` python
import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    flag = True
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            flag = False
            print('found')
            break

    if flag:
        print('not found')
```

<center>↓</center>

``` python
import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            print('found')
            break
    else:
        print('not found')
```

</br>

#### 두 변수의 값 바꾸기
- 임시 변수 temp 없이도, 간단하게 한 줄로 두 변수의 값을 바꿀 수 있습니다.


``` python
a = 3
b = 'abc'

temp = a
a = b
b = temp
print(a, b)
```

<center>↓</center>

``` python
a = 3
b = 'abc'

a, b = b, a # 참 쉽죠?
print(a, b)
```

</br>

#### 이진 탐색
- 이진 탐색 시, bisect 모듈을 활용할 수 있습니다.


``` python
def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3))
```

<center>↓</center>

``` python
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
```

</br>

#### 클래스 인스턴스 출력하기
- 다른 언어에서는 클래스 바깥에 출력 함수를 만들거나, `print` 문 안에서 `format`을 지정합니다.
- 파이썬에서는 `__str__` 메소드를 정의하여 클래스 내부의 출력 `format`을 설정할 수 있습니다.
``` python
class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)
print(point)
```

</br>

#### 가장 큰 수 INF
- 대소 관계 비교를 위한 큰 수가 필요할 때, `inf`를 활용할 수 있습니다.
``` python
min_val = float("inf") #문자열로 선언해줘야 합니다.
print(min_val)
```

#### 파일 입출력 간단하게 하기
- `with - as`를 통해 파일을 close할 필요 없이 끝까지 읽을 수 있습니다.


``` python
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line: 
        break
    raw = line.split()
    print(raw)
f.close()
```

<center>↓</center>

``` python
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))
```