from fastapi import FastAPI

app = FastAPI()

fruits = ['Apple', 'Banana', 'Orange', 'Guava', 'Berry']
my_tuple = ('apple', 'banana', 'orange', 'guava')
my_dict = {1: 'apple', 2: 'banana', 3: 'orange3'}


def toUpppercase(value: str) -> str:
    return value.upper()


result = filter(lambda x: x != 'Apple', fruits)
print(list(result))
