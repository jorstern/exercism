
import ast

def is_valid(source, file=True):
    if file:
        file = open(source).read()
        tree = ast.parse(source=file)
    else:
        tree = ast.parse(source=source)

    for node in ast.walk(tree):
        if isinstance(node, ast.Return):
            try:
                if node.value.s == "Hello, World!":
                    return True
            except:
                return False
    return False

