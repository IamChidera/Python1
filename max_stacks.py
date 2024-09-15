class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_values = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_values or value >= self.max_values[-1]:
            self.max_values.append(value)

    def pop(self):
        if not self.stack:
            return None
        if self.stack[-1] == self.max_values[-1]:
            self.max_values.pop()
        return self.stack.pop()

    def max(self):
        if not self.max_values:
            return None
        return self.max_values[-1]

# Input
q = int(input())
max_stack = MaxStack()

# Process queries
for _ in range(q):
    query = input().split()
    if query[0] == "push":
        value = int(query[1])
        max_stack.push(value)
    elif query[0] == "pop":
        max_stack.pop()
    elif query[0] == "max":
        print(max_stack.max())
