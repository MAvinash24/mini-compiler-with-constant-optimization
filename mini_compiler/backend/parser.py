def parser(code):
    lines = code.split("\n")

    for i, line in enumerate(lines, start=1):
        if line.strip() == "":
            continue

        if "=" not in line:
            return f"Line {i}: Syntax Error → Missing '='"

        parts = line.split("=")
        if len(parts) != 2 or parts[1].strip() == "":
            return f"Line {i}: Syntax Error → Incomplete expression"

    return "Valid Assignment Expression"