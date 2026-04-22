import sys
import os
import time
import streamlit as st

# Backend path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from lexer import lexer
from parser import parser
from semantic import semantic_analysis
from optimizer import optimize
from codegen import generate_target, generate_tac

st.set_page_config(page_title="Mini Compiler", layout="wide")
st.markdown("""
<style>

/* Main background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}

/* Text area */
textarea {
    background-color: #1a1a2e !important;
    color: #e0e0ff !important;
    border-radius: 10px !important;
    border: 1px solid #6a5acd !important;
}

/* Buttons */
button {
    background-color: #6a5acd !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
}

button:hover {
    background-color: #836fff !important;
}

/* Code blocks */
pre {
    background-color: #1a1a2e !important;
    color: #c7c7ff !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

/* Headers */
h1, h2, h3 {
    color: #b19cd9 !important;
}

/* Success box */
div[data-baseweb="notification"] {
    border-radius: 10px !important;
}

/* Section boxes */
.block-container {
    padding: 2rem;
}

</style>
""", unsafe_allow_html=True)
st.title("Mini Compiler (Advanced Visualization)")

code = st.text_area("Enter Code", height=150, value="""a = 5
b = a + 2
c = b * 3""")

# ---------------- PARSE TREE ----------------
def build_parse_tree(expr, var):
    parts = expr.split()

    if len(parts) == 3:
        return f"""
{var}
 |
 =
/ \\
{var}  {parts[1]}
    / \\
   {parts[0]}  {parts[2]}
"""
    return f"{var} = {expr}"

# ---------------- DEPENDENCY GRAPH ----------------
def build_dependency_graph(code):
    graph = []
    for line in code.split("\n"):
        if "=" in line:
            var, expr = line.split("=")
            var = var.strip()
            for ch in expr.split():
                if ch.isalpha():
                    graph.append(f"{ch} → {var}")
    return "\n".join(graph)

# ---------------- ITERATIVE OPTIMIZATION ----------------
def iterative_optimize(code):
    lines = code.split("\n")
    symbol = {}
    iterations = []

    for i, line in enumerate(lines):
        if "=" in line:
            var, expr = line.split("=")
            var = var.strip()
            expr = expr.strip()

            for k, v in symbol.items():
                expr = expr.replace(k, str(v))

            try:
                val = eval(expr)
                symbol[var] = val
                iterations.append(f"Iteration {i+1}: {var} = {val}")
            except:
                iterations.append(f"Iteration {i+1}: {line}")

    return "\n".join(iterations)

# ---------------- MAIN ----------------
if st.button("Compile"):

    tokens = lexer(code)

    # ❌ LEXICAL ERROR
    if isinstance(tokens, str):
        st.error(tokens)
        st.stop()

    parse = parser(code)

    # ❌ SYNTAX ERROR
    if "Error" in parse:
        st.error(parse)
        st.stop()

    semantic = semantic_analysis(code)

    # ---------------- SHOW PHASES ----------------
    st.subheader("🔹 Syntax Analysis")
    st.success(parse)

    st.subheader("🔹 Semantic Analysis")

    if semantic != "No Semantic Errors":
        st.error(semantic)
        st.stop()
    else:
        st.success(semantic)

    # ---------------- CONTINUE ----------------
    tac = generate_tac(code)
    optimized = optimize(code)
    target = generate_target(optimized)

    col1, col2 = st.columns(2)

    # LEFT PANEL
    with col1:
        st.subheader("🔹 Tokens")
        st.code(tokens)

        st.subheader("🌳 Parse Tree (Structured)")
        tree_output = ""
        for line in code.split("\n"):
            if "=" in line:
                var, expr = line.split("=")
                tree_output += build_parse_tree(expr.strip(), var.strip()) + "\n"
        st.code(tree_output)

        st.subheader("🔗 Dependency Graph")
        st.code(build_dependency_graph(code))

    # RIGHT PANEL
    with col2:
        st.subheader("🔹 TAC")
        st.code(tac)

        st.subheader("🔹 Optimized Code")
        st.code(optimized)

        st.subheader("🔹 Target Code")
        st.code(target)

    # ITERATIONS
    st.subheader("🔁 Iterative Optimization")
    st.code(iterative_optimize(code))

    # STEP ANIMATION
    st.subheader("🎬 Step-by-Step Execution")

    steps = optimized.split("\n")
    placeholder = st.empty()
    output = ""

    for step in steps:
        if step.strip():
            output += step + "\n"
            placeholder.code(output)
            time.sleep(0.5)
