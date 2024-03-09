# python_example
파이선_공부를_위한_레포지토리입니다.

참고: https://wikidocs.net/book/2

공부하면서 알게된 사항

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