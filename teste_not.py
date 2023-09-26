class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is not None:
            value = self.top.value
            self.top = self.top.next
            return value
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return self.top is None

expression = ["/", "+", "-", "837", "35", "-", "332", "124", "-", "-", "260", "605", "-", "751", "463"]
stack = Stack()

def custom_floor(x):
    if x >= 0:
        return int(x)
    else:
        return int(x) if x == int(x) else int(x) - 1

for token in expression:
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
        stack.append(int(token))
    elif token in ('+', '-', '*', '/'):
        operando_2 = stack.pop()
        operando_1 = stack.pop()

        if token == '+':
            resultado = operando_1 + operando_2
        elif token == '-':
            resultado = operando_1 - operando_2
        elif token == '*':
            resultado = operando_1 * operando_2
        elif token == '/':
            if operando_2 == 0:
                print("Erro: Divisão por zero")
            else:
                resultado = operando_1 / operando_2
                resultado = custom_floor(resultado)

        stack.append(resultado)

print("Resultado da expressão 2:", stack[0])



