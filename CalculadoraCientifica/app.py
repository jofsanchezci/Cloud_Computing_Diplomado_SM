from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            num1 = request.form.get("num1", type=float)
            num2 = request.form.get("num2", type=float, default=None)
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
                    error = "Error: División por cero no permitida"
            elif operation == "sin":
                result = math.sin(math.radians(num1))
            elif operation == "cos":
                result = math.cos(math.radians(num1))
            elif operation == "tan":
                result = math.tan(math.radians(num1))
            elif operation == "log":
                if num1 > 0:
                    result = math.log10(num1)
                else:
                    error = "Error: Logaritmo indefinido para números no positivos"
            elif operation == "power":
                result = math.pow(num1, num2)
        except ValueError:
            error = "Error: Entrada inválida. Ingresa números válidos."

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
