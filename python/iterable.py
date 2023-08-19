from typing import List, Any, Generator


class CharacterRange:
    def __init__(self, start: str, end: str):
        self._start: str = start
        self._end: str = end

    def __iter__(self):
        print("call __iter__")
        return self.CharacterIterator(self._start, self._end)

    class CharacterIterator:
        def __init__(self, start: str, end: str):
            self._start: int = ord(start)
            self._end: int = ord(end)

        def __next__(self) -> str:
            if self._start != self._end:
                self._start += 1
                return chr(self._start - 1)
            else:
                raise StopIteration


c_range = CharacterRange('a', 'e')
for c in c_range:
    print(c)

for c in c_range:
    print(c)


# arr_iterator = iter([1, 2, 3])
# print(next(arr_iterator))
# print(next(iter(c_range)))
# print(list(range(1, 10)))

# for i in map(lambda x: x ** 2, arr_iterator):
#     print(i)
# for c in arr_iterator:
#     print(c)

def split_and_square_chunks(arr: List[Any], chunk_size: int = 10) -> Generator:
    for i in range(0, len(arr), chunk_size):
        yield [i*i for i in arr[i:i + chunk_size]]


arr = list(range(20))
for chunk in split_and_square_chunks(arr, 5):
    print(chunk)


arr = list(range(20))
print(type(filter(lambda x: x**2, arr)))

print(split_and_square_chunks(arr, 5))
print(iter(iter(split_and_square_chunks(arr, 5))))
print(next(iter(split_and_square_chunks(arr, 5))))
# print(gener.__dict__)
