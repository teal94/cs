# pow_count: int = 0
# def pow(n: int) -> int:
#     print(aa)
#     pow_count += 1
#     return n ** 2

# print(pow(10))
# print(pow(5))
# print(pow_count)



# for i in range(6):
#     print(i, id(i))

# print()
# for i in range(10, 5, -1):
#     print(i, id(i))

# a = 111111111111111111111
# c = 123132432938293829932
# b = 111111111111111111112
# c = 111111111111111111111
# print(id(a))
# print(id(b))
# print(id(c))

# def test():
#     num = 1
#     a = 257
#     b = 256 + num
#     c = 256 + 1
#     print(id(a))
#     print(id(b))
#     print(id(c))
# test()


# arr = [1, 2, 3]

# print(id(arr))

# arr.append(4)

# print(id(arr))

# arr.insert(0, 0)

# print(id(arr))


pow_cnt = 10
def pow(n: int) -> int:
    pow_cnt = 1
    return n ** 2

# print(pow(10))
# print(pow(20))

# print(pow_cnt)

class charactor:
    pass
ch = charactor()
print(id(pow), id(ch))

def dfs(aloc, bloc, turn):
    print(aloc, bloc, turn)
    print(type(aloc))

dfs((1,0), (2,0), 1 + 1)
dfs([1,0], [2,0], 1 + 1)