#  Mini Compiler with Constant Optimization

## 📌 Overview
This project implements a **Mini Compiler** that demonstrates key compiler design phases along with **optimization techniques** like:

- Constant Folding
- Constant Propagation

It also provides an **interactive UI (Streamlit)** to visualize each phase of compilation.

---

## 🎯 Features

✔ Lexical Analysis (Tokenization)  
✔ Syntax Analysis (Basic Parsing)  
✔ Semantic Analysis (Error Checking)  
✔ Intermediate Code Generation (Three Address Code - TAC)  
✔ Optimization  
   - Constant Folding  
   - Constant Propagation  
✔ Target Code Generation  
✔ Parse Tree Visualization 🌳  
✔ Dependency Graph 🔗  
✔ Iterative Optimization 🔁  
✔ Step-by-Step Execution 🎬  
✔ Error Handling (Lexical, Syntax, Semantic)  

---

## 🧠 Constant Optimization Explained

### 🔹 1. Constant Folding

Constant folding evaluates expressions at **compile time** instead of runtime.

#### Example:
a = 3 + 5

👉 Compiler computes:
a = 8

✔ Reduces runtime computation  
✔ Improves performance  

---

### 🔹 2. Constant Propagation

Constant propagation replaces variables with their **known constant values**.

#### Example:
a = 5  
b = a + 2  

👉 Replace a:
b = 5 + 2 → 7  

✔ Eliminates unnecessary variables  
✔ Simplifies expressions  

---

### 🔹 3. Combined Optimization

a = 5  
b = a + 2  
c = b * 3  

Step-by-step:
- a = 5  
- b = 5 + 2 → 7  
- c = 7 * 3 → 21  

✔ Multi-level optimization  
✔ Recursive propagation  

---

## 🔁 Optimization Flow

Input Code → Propagation → Folding → Repeat → Optimized Code

---

## 🏗️ Project Structure

mini-compiler/
│
├── backend/
│   ├── lexer.py
│   ├── parser.py
│   ├── semantic.py
│   ├── optimizer.py
│   ├── codegen.py
│
├── frontend/
│   └── streamlit_app.py
│
└── README.md

---

## ▶️ How to Run

### 1️⃣ Install Dependencies
pip install streamlit

### 2️⃣ Navigate to frontend
cd frontend

### 3️⃣ Run Application
streamlit run streamlit_app.py

### 4️⃣ Open in Browser
http://localhost:8501

---

## 🧪 Sample Input

a = 5  
b = a + 2  
c = b * 3  

---

## ✅ Output

Optimized Code:
a = 5  
b = 7  
c = 21  

---

## 🎤 Viva Explanation

This project demonstrates how compiler optimization techniques like constant folding and constant propagation reduce runtime computation by evaluating expressions during compilation.

---

## 💡 Future Enhancements

- AST-based optimization  
- Graphical parse tree visualization  
- Symbol table UI  
- Advanced parsing (LL/LR parser)  

---

## 👨‍💻 Author

Avinash
