def add(num1: int, num2: int) -> str:
    result: str = "足し算の結果:"
    return result + str(num1 + num2)

def greet(name: str) -> str:
    return f"おはよう!{name}!"

def devide(dividend: float, divisor: float) -> float:
    return dividend / divisor

from typing import List
def get_first_three_elements(elements: List[int]) -> List[int]:
    return elements[:3]

def process_items(items: list[str]) -> None:
    for item in items:
        print(item)

def count_characters(word_list: list[str]) -> dict[str, int]:
    count_map: dict[str, int] = {}
    for word in word_list:
        count_map[word] = len(word)
    return count_map

result_add = add(10, 20)
print(result_add)

greeting = greet("太郎")
print(greeting)

result_devide = devide(10.0, 2.0)
print(result_devide)

result_get_first_three_elements = get_first_three_elements([1, 2, 3, 4, 5])
print(result_get_first_three_elements)

result_process_items = process_items(["apple", "banana", "cherry"])

character_count = count_characters(["apple", "banana", "cherry"])
print(character_count)