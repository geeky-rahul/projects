from flask import Flask, request, jsonify
from sympy import sympify

app = Flask(__name__)

def solve_math_expression(expression):
    try:
        result = sympify(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.get_json()
        if not data or 'expression' not in data:
            return jsonify({'result': 'Invalid request. Please provide a valid expression.'}), 400
        
        expression = data['expression']
        result = solve_math_expression(expression)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'result': f"Error: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
