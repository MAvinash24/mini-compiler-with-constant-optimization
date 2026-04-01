import re

def optimize(code):
    symbol_table = {}
    lines = code.split("\n")
    result = []

    for i, line in enumerate(lines, start=1):
        if "=" in line:
            var, expr = line.split("=")
            var = var.strip()
            expr = expr.strip()

            # Replace variables safely
            for k, v in symbol_table.items():
                expr = re.sub(rf'\b{k}\b', str(v), expr)

            try:
                value = eval(expr)
                symbol_table[var] = value
                result.append(f"Line {i}: {var} = {value}")
            except:
                result.append(f"Line {i}: {var} = ERROR")

    return "\n".join(result)