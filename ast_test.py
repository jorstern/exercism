
import ast

def is_valid(filename="hello_world.py"):
    file = open(filename).read()
    tree = ast.parse(source=file)

    for node in ast.walk(tree):
        if isinstance(node, ast.Return):
            try:
                if node.value.s == "Hello, World!":
                    return True
                else:
                    return False
            except:
                return False

print(is_valid())