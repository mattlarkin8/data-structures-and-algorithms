from data_structures.stack import Stack

def multi_bracket_validation(string):
    open_stack = Stack()
    openers = ["{","[","("]
    closers = ["}","]",")"]
    pairs = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    chars = list(string)
    for char in chars:
        if char in openers:
            open_stack.push(char)

        if char in closers:
            if open_stack.is_empty():
                return False

            if pairs.get(char) == open_stack.peek():
                open_stack.pop()
            else:
                return False

    return True
