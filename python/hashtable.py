from typing import List, Any, Optional

class HashTable:
    def __init__(self, size:int, *arg, **kwargs):
        self._size: int = size
        self._table: List[Optional[List]] = [None] * self._size

    def _hash_function(self, key) -> int:
        return hash(key) % self._size

    def insert(self, key: Any, value: Any) -> Any:
        index = self._hash_function(key)
        table = self._table[index]
        if table == None:
            self._table[index] = [(key, value)]
        else:
            table.append((key, value))

    def get(self, key) -> Any:
        index = self._hash_function(key)
        table = self._table[index]
        if table != None:
            for cur_key, cur_value in table:
                if key == cur_key:
                    return cur_value
        return None

    def remove(self, key) -> None:
        index = self._hash_function(key)
        table = self._table[index]
        if table != None:
            for ind, e in enumerate(table):
                if e[0] == key:
                    del table[ind]
                    return



hash_table = HashTable(100)

hash_table.insert("test", 123)
hash_table.insert("test123", "232332")
hash_table.insert("test145", 555)


print(hash_table.get("test123"))
print(hash_table.get("test"))

hash_table.remove("test")

print(hash_table.get("test"))