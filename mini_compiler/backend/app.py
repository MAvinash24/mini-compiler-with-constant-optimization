from flask_cors import CORS
from flask import Flask, request, jsonify
from lexer import lexer
from parser import parser
from semantic import semantic_analysis
from optimizer import optimize
from codegen import generate_target, generate_tac

app = Flask(__name__)
CORS(app)

@app.route('/compile', methods=['POST'])
def compile_code():
    code = request.json['code']

    tokens = lexer(code)
    parse = parser(tokens)
    semantic = semantic_analysis(code)

    tac = generate_tac(code)          
    optimized = optimize(code)
    target = generate_target(optimized)  

    return jsonify({
        "tokens": tokens,
        "parse": parse,
        "semantic": semantic,
        "tac": tac,
        "optimized": optimized,
        "target": target  
    })

if __name__ == "__main__":
    app.run(debug=True)