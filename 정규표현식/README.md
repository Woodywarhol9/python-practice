# Python을 활용한 정규 표현식 작성법

### 정규 표현식 패턴
- `\d` : 모든 숫자를 인식
``` python
regex = r'\d'

# 주소록입니다. 이후 강의에서 모두 이 search_target을 사용합니다.
search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))
```
실행 결과
```
0
2
1
...
3
4
5
7
```
---
- `\w` : 모든 문자와 숫자를 인식, 특수 문자 중 `_`(언더 스코어)도 인식 됨
``` python
# 빈칸에 정규표현식을 적습니다.
regex = r'\w'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))
```

실행 결과

```
L
u
k
...
l
c
o
m
```
---
- `+` : 1개 이상 반복되는 패턴을 인식
``` python
# 빈칸에 정규표현식을 적습니다.
regex = r'\d+'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

#아래 부분은 본 강의에서 다루지 않습니다.
import re
result=re.findall(regex,search_target)
print(result)
```
실행 결과
```
['02', '123', '4567', '070', '9999', '9999', '010', '2454', '3457']
```
---
- `*` : 0개 이상 반복되는 패턴을 인식
``` python
regex = r'[1-9]\d*'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))
```
실행 결과
```
2
123
4567
70
9999
9999
10
2454
3457
```
---
- `?` : 있을 수도, 없을 수도 있는 패턴을 지정
``` python
regex = r'\d+-?\d+-?\d+'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

#아래 부분은 본 강의에서 다루지 않습니다.
import re
result=re.findall(regex,search_target)
print(result)
```
실행 결과
```
['02-123-4567', '070-9999-9999', '010', '2454', '3457']
```
---
- `[ ]` : 문자 다중 지정 가능 → `[- ]?`를 통해 공백 또는, `-`를 확인 가능
``` python
regex = r'\d+[- ]?\d+[- ]?\d+'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

#아래 부분은 본 강의에서 다루지 않습니다.
import re
result=re.findall(regex,search_target)
print(result)
```
실행 결과
```
['02-123-4567', '070-9999-9999', '010 2454 3457']
```
---
- `{n}` : 패턴 반복 횟수 지정 가능
``` python
regex = r'\d{2}[- ]?\d{3}[- ]?\d{4}'

search_target = '''이상한 전화번호 0030589-5-95826
Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

#아래 부분은 본 강의에서 다루지 않습니다.
import re
result=re.findall(regex,search_target)
print(result)
```
실행 결과
```
['02-123-4567']
```
---
- `{n, m}` : 최소 반복 횟수 `n`, 최대 반복 횟수 `m` 지정 가능
``` python
regex = r'\d{2,3}[- ]?\d{3,4}[- ]?\d{4}'

search_target = '''이상한 전화번호 0030589-5-95826
Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

#아래 부분은 본 강의에서 다루지 않습니다.
import re
result=re.findall(regex,search_target)
print(result)
```
실행 결과
```
['02-123-4567', '070-9999-9999', '010 2454 3457']
```
---
- 대표 문자로 `[ ]`을 간단하게 활용하기
  - `[a-z]` : 모든 알파벳 문자
  - `[0-9]` : 모든 숫자
  - `[가-힣]` : 모든 한글 → `ㄱ`, `ㅏ` 자-모가 분리된 경우엔 확인 불가
  - `\s` : 모든 공백(띄어쓰기, 탭, 줄바꿈)
  - 대문자는 각 소문자 패턴을 제외하는 역할 
    - ex) `\W`, `\S`, `\D`
---
### 정규 표현식에 사용되는 함수
- `re.match` : 패턴이 문자열의 처음 부분과 일치하는지 확인
- `re.search` : 문자열 어디선가 패턴이 일치하는지 확인
- `re.findall` : 정규 표현식 패턴과 일치하는, 모든 부분을 `list`로 반환
- `re.sub` : 패턴을 찾아, 지정한 문자로 변경