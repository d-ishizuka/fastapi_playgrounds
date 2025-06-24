def parse_input(value: int | str) -> str:
    if isinstance(value, int):
        return f"値は整数型です=>{value}"
    elif isinstance(value, str):
        return f"値は文字列型です=>{value}"
    else:
        raise ValueError("引数が整数型/文字列型ではありません")

print(parse_input(123))
print(parse_input("abc"))
# print(parse_input(99.9))