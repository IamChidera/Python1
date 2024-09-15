def find_bracket_mismatch(input_string):
    stack = []
    for index, char in enumerate(input_string):
        if char in "([{":
            stack.append((char, index))
        elif char in ")]}":
            if not stack:
                return index + 1
            top, top_index = stack.pop()
            if (top == "[" and char != "]") or (top == "{" and char != "}") or (top == "(" and char != ")"):
                return index + 1

    if stack:
        top, top_index = stack.pop()
        return top_index + 1

    return "Success"

# Input
input_string = input()
result = find_bracket_mismatch(input_string)
print(result)
