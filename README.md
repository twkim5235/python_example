# python_example
파이선_공부를_위한_레포지토리입니다.

참고: https://wikidocs.net/book/2

## 공부하면서 정리한 사항

### 변수명과 함수명 명명 법칙

Function names should be lowercase, with words separated by underscores as necessary to improve readability.
- 함수명은 소문자로 만들어야 되며, 가독성을 위해 '_'로 분리한다.

Variable names follow the same convention as function names.
- 변수명도 함수명과 동일한 규칙을 갖는다.

https://peps.python.org/pep-0008/#function-and-variable-names



### condition = (a, b) in [(조건, 조건), (조건, 조건), ...]

- 파이썬은 조건문을 밖에서도 쓸 수 있다.
- 위의 내용은 (a, b)가 in 우측에 있는 조건에 맞는가에 대한 조건을 변수로 선언해놓은것이다.
- 코드는 tuple의 ex2를 참고하면 된다.
- ~~~python
  condition = (a, b) in [(조건, 조건), (조건, 조건), ...]
  
  if condition:
  ~~~



### map()

- iter 각각의 원소에 대해서 연산을 처리하는 함수이다.



### reduce()

- iter에 대해서 누적치를 구해주는 함수이다.
- reduce(집계함수, iter)
- 첫번째 인자에는 집계함수가 들어가며 대표적인 예를 들자면
  - lambda(x, y: x + y, iter) 같은 함수가 들어간다.
- 두번째 인자에는 연산을 처리할 iter 가 들어간다.



### dictionary

- Java의 HashMap과 비슷하며, key값과 Value를 가짐



### 모듈

모듈은 다른 프로그래머가 내가 만들고 싶어하는 기능과 비슷한 기능을 만들어 둔 것이다.

비유를 하자면 공구통이라고 생각하면된다.

- 내가 망치질을 하고 싶으면, 못과 망치를 만드는 것이 아니라 공구통에서 꺼내서 쓴다.

### self를 왜 메소드의 인자로 받는 이유
예전에 자바를 공부할 때 self는 객체의 인스턴스라고 알고 있었다.
- 객체 자기 자신을 참조하는 매개변수인 셈이다.

하지만 왜 파이썬에서는 self를 메소드의 매개변수로 정의하는지에 의문을 가졌다.
- 객체지향 언어는 self를 메소드에 안보이게 전달한다.
- 파이썬은 메소드를 불러올 때 self는 자동으로 전달된다. 
- self를 사용함으로 클래스내에 정의한 멤버에 접근할 수 있기 때문이다.

### 메소드의 리턴을 정하지도 않았는데 None이 리턴이 되는 경우
- 파이썬은 return 값을 명시해주지 않으면 자체적으로 None을 반환을 한다.