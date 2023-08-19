address_arr = []

global_var = ["123"]
global_var2 = 20
class Person:
    person_count = 0
    def __init__(self, age):
        self.age = age

def f(num):
    person = Person(10)
    address_arr.append(("person id :", id(person)))
    address_arr.append(("num :", id(num)))
    
f(1234)

address_arr.append(("global_var id :", id(global_var)))
address_arr.append(("person_count id :", id(Person.person_count)))
address_arr.append(("global_var2 id :", id(global_var2)))
address_arr.append(("f id :", id(f)))

for address in sorted(address_arr, key=lambda x: -x[1]):
    print(address)