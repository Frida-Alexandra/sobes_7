class Stack(list):
    def isEmpty(self):
        return len(self) == 0

    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.isEmpty():
            item = self[-1]
            del self[-1]
            return item

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


SBAL = ["(((([{}]))))", "[([])((([[[]]])))]{()}", "{{[()]}}"]

NOTBAL = ["}{}", "{{[(])]}}", "[[{())}]"]


def isBalanced(expr):
    s = Stack()
    for c in expr:
        if c in "({[":
            s.push(c)
        elif c in ")}]":
            if s.isEmpty():
                return False
            if c == ")" and s.peek() != "(":
                return False
            if c == "}" and s.peek() != "{":
                return False
            if c == "]" and s.peek() != "[":
                return False
            s.pop()
    return s.isEmpty()


if __name__ == "__main__":
    for expr_ in SBAL + NOTBAL:
        print(f"{expr_:<25}{isBalanced(expr_)}")
