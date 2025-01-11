from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        num1 = request.form.get("num1", type=float)
        num2 = request.form.get("num2", type=float)
        operation = request.form.get("operation")

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: División por cero no permitida"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
