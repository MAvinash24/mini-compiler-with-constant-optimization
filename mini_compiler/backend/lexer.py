import re

def lexer(code):
    lines = code.split("\n")

    for i, line in enumerate(lines, start=1):
        for ch in line:
            if not re.match(r'[a-zA-Z0-9=+\-*/()\s]', ch):
                return f"Line {i}: Lexical Error → Invalid character '{ch}'"

    tokens = re.findall(r'[a-zA-Z]+|\d+|[=+\-*/()]', code)
    return tokens