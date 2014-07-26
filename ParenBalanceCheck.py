
from Stack import Stack

SYMBOLS = { '{' : '}', '(' : ')', '[' : ']' }

def check(parens):
    stack = Stack()
    for c in parens:
        if c in SYMBOLS.keys():
            stack.push(c)
        elif c in SYMBOLS.values():
            if not stack.isEmpty() and c == SYMBOLS[stack.peek()]:
                stack.pop()
            else: return False
    return stack.isEmpty()


def withMain(parens):
    msg = "Parenthesis are %s"
    if check(parens):
        msg = msg % 'balanced'
    else:
        msg = msg % 'unbalanced'
    print msg

if __name__ == '__main__':
    withMain('((()))')
    withMain('(()))')
    withMain('(()))')
    withMain('([{}])')
    withMain('({[}])')

