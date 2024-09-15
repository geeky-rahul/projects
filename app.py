from flask import Flask, render_template, request, jsonify, send_file
import sympy as sp

# import os

# Define the path to the folder
app = Flask(__name__, template_folder="template", static_folder="static")


@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/name")
def name():
    return render_template("/name.html")


@app.route("/image")
def get_image():
    # The path to the image file
    image_path = "static/images/iron.jpg"
    return send_file(image_path, mimetype="image/jpeg/")


# @app.route("/image")
# def image():
#     return render_template("/iron.jpg")


@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json()
    question = data.get("question", "")

    try:
        # Use sympy to solve the math question
        answer = sp.sympify(question).evalf()
    except Exception as e:
        answer = f"Error: {e}"

    return jsonify({"answer": str(answer)})


if __name__ == "__main__":
    app.run(debug=True)
