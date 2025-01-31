# 모듈( Module)

한 파일로 묶인 변수와 함수의 모음

특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)

### math내장 모듈

- 파이썬이 미리 작성해둔 수학 관련 변수와 함수가 작성된 모듈

```python
import math  #import = 가져오다
print(math.pi)  #이미 내장된 모듈
print(math.sqrt(4)) #제곱근
```

### 모듈을 가져오는 방법

- import문 사용(권장)

```python
import math
print(math.sqrt(4))
```

- from 절 사용

        - 모듈에서 가져온 게 아니기 때문에 사용자가 만든 함수라고 오해할 수 있음

        - 이름 충돌이 날 수도 있음

        - 경로가 길면 ‘.’ 사용, from 여러 번X

```python
from math import sqrt #어디에서 ~을 가져오겠다
print(sqrt(4))  #모듈을 가져오지 않음
```

## 모듈 사용

### .(dot) 연산자

- 점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라 라는 의미

```python
#모듈명.변수명
print(math.pi)

#모듈명.함수명
print(math.sqrt(4))
```

### 주의 사항

- 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
- 마지막에 import된 이름으로 대체됨

```python
from math import pi, sqrt
from my_math import sqrt
#모듈 내 모든 요소를 한번에 import 하는 * 표기는 권장하지 않음

from math import *
```

- 모듈을 가져오고 함수 호출

### ‘as’키워드

- as 키워드를 사용하여 별칭(alias)을 부여
- 두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결

```python
from math import sqrt
from my_math import sqrt as my_sqrt

sqrt(4)
my_sqrt(4)
```

## 사용자 정의 모듈

### 직접 정의한 모듈

다른 파일에 함수를 만들고 새로운 파일에 import 작성 후 불러오기

## 파이썬 표준 라이브러리(Python Standard Library)

파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

## 패키지(Package)

연관된 모듈들을 하나의 디렉토리에 모아 놓은 것

### 패키지 사용

- import할 필요가 없을 경우(상위폴더) from 사용 후 import하기

```python
from my_package.math import my_math
```

- 그 이후 import
- PSL 내부 패키지 : 설치 없이 바로import하여 사용
- 외부 패키지 : pip를 사용하여 설치 후 import 필요(더 많이 활용하게 됨)

### pip(파이썬 패키지 관리자)

외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

PyPI(Python Package Index)에 저장된 외부 패키지들을 설치

**패키지 설치**

- 최신 버전/ 특정 버전/ 최소 버전을 명시하여 설치할 수 있음

```python
$ pip install SomePackage           #최신버전
$ pip install SomePackage==1.0.5    #특정버전
$ pip install SomePackage>=1.0.4    #최소버전
```

- 패키지 삭제 uninstall
- requests : 외부 API  서버로 요청을 보냄(사용법 가이드 문서 존재)
- request 라이브러리에 있는 get함수

```python
$ pip install requests
import requests

url = ''
response = requests.get(url).json()

print(response)
```

### 패키지 사용 목적

모듈들의 이름공간을 구분하여 충돌을 방지

모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할