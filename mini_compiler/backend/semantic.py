def semantic_analysis(code):
    import re
    lines = code.split("\n")
    declared = set()
    errors = []

    for i, line in enumerate(lines, start=1):
        if "=" in line:
            var, expr = line.split("=")
            var = var.strip()
            expr = expr.strip()

            declared.add(var)

            # Undefined variables
            variables = re.findall(r'[a-zA-Z]+', expr)
            for v in variables:
                if v not in declared:
                    errors.append(f"Line {i}: Semantic Error → '{v}' not defined")

            # Division by zero
            if "/" in expr:
                parts = expr.split("/")
                right = parts[1].strip()

                if right == "0":
                    errors.append(f"Line {i}: Semantic Error → Division by zero")

    return "No Semantic Errors" if not errors else "\n".join(errors)