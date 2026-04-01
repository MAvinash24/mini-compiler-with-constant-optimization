def generate_tac(code):
    lines = code.split("\n")
    temp_count = 1
    tac = []

    for i, line in enumerate(lines, start=1):
        if "=" in line:
            var, expr = line.split("=")
            var = var.strip()
            expr = expr.strip()

            tac.append(f"Line {i}: t{temp_count} = {expr}")
            tac.append(f"Line {i}: {var} = t{temp_count}")
            temp_count += 1

    return "\n".join(tac)


def generate_target(code):
    lines = code.split("\n")
    target = []

    for line in lines:
        if "=" in line:
            var, val = line.split("=")
            target.append(f"MOV {var.strip()}, {val.strip()}")

    return "\n".join(target)