from typing import Dict, Callable
from functools import wraps
import sys

# def my_decorator(f):
#     @wraps(f)
#     def wrapper(*args, **kwds):
#         print('Calling decorated function')
#         cur_f = f(*args, **kwds)
#         print('Calling decorated function after')
#         return cur_f
#     return wrapper


# @my_decorator
# def test():
#     print("123")
#     return 1235


# print(test())


# n: int = 10000


# def fib_decorator(f):
#     dp: List[int] = [0]*(n+1)

#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         n = args[0]
#         if dp[n]:
#             return dp[n]
#         dp[n] = f(n)
#         return dp[n]
#     return wrapper


# @fib_decorator
# def fib(n) -> int:
#     if n < 3:
#         return 1
#     return fib(n-2) + fib(n-1)
#     if dp[n]:
#         return dp[n]
#     dp[n] = fib(n-2) + fib(n-1)
#     return dp[n]


# print(fib(100))


# def is_cached(f):
#     cache = {}

#     def inner(n):
#         if n in cache:
#             return cache[n]
#         cache[n] = f(n)
#         return cache[n]
#     return inner


# cnt = 0


# @is_cached
# def fib(n):
#     global cnt
#     cnt += 1
#     if n < 3:
#         return 1
#     return fib(n-2) + fib(n-1)


# print(fib(100))
# print("cnt", cnt)
# print(fib.__closure__[0].cell_contents)


# def fib(n) -> int:
#     if n < 3:
#         return 1
#     return fib(n-2) + fib(n-1)
# print(fib(100))

# cache: Dict[int, int] = {}
# def fib(n: int) -> int:
#     if n < 3:
#         return 1

#     if cache.get(n):
#         return cache[n]

#     cache[n] = fib(n-2) + fib(n-1)
#     return cache[n]


# print(fib(100))


def cache(f: Callable) -> Callable:
    cache = {}

    def inner(*arg, **kwargs):
        n = arg[0]

        if cache.get(n):
            return cache[n]

        cache[n] = f(*arg, **kwargs)
        return cache[n]
    return inner


@cache
def fib(n: int) -> int:
    if n < 3:
        return 1
    return fib(n-2) + fib(n-1)


print("fuction name", fib.__name__)
print("__closure__ 1", fib.__closure__[0].cell_contents)
fib(10)
print("__closure__ 2", fib.__closure__[0].cell_contents)

def add(a, b):
    return a + b

def add_custom(a, b):
    return a + b

if add == add_custom:
    print("같다")
else:
    print("다르다")

add2 = add

if add == add2:
    print("같다")
else:
    print("다르다")


e = 10
def outer(a: int, b: int) -> None:
    c = a + b
    def inner(n: int) -> int:
        d = 10 + e
        print(d)
        return c + n
    print("결과값 :", inner(10))

outer(2, 3)





import sys

x = [1, 2, 3]
y = x

ref_count = sys.getrefcount(x)  # x 객체의 레퍼런스 카운트 확인
print(ref_count)  # 출력: 3 (변수 x, y, sys.getrefcount() 함수 내에서 각각 1번씩 레퍼런스가 증가됨)

del x

ref_count = sys.getrefcount(y)  # y 객체의 레퍼런스 카운트 확인
print(ref_count)  # 출력: 2 (변수 y, sys.getrefcount() 함수 내에서 각각 1번씩 레퍼런스가 증가됨)

print(y)  # 출력: [1, 2, 3]



e = 10
def outer(f) -> Callable:
    c = 10
    def inner(n: int) -> int:
        d = 10 + c
        
        return d
    return inner


@outer
def test():
    return 1

