
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():

    answer = None
    error = None

    if request.method == "POST":

        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operator = request.form["operator"]

            # SECRET COMBINATION
            if num1 == 1234 and operator == "+" and num2 == 4321:
                return redirect(url_for("secret"))

            # NORMAL CALCULATIONS
            if operator == "+":
                answer = num1 + num2

            elif operator == "-":
                answer = num1 - num2

            elif operator == "*":
                answer = num1 * num2

            elif operator == "/":
                if num2 != 0:
                    answer = num1 / num2
                else:
                    error = "Cannot divide by zero!"

        except ValueError:
            error = "Please enter valid numbers."

    return render_template(
        "index.html",
        answer=answer,
        error=error
    )


# SECRET PAGE
@app.route("/secret")
def secret():
    return render_template("secret.html")


if __name__ == "__main__":
    app.run(debug=True)
