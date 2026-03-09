# calculator.py
# A minimal Flask web app that presents a form to enter two numbers and select an arithmetic operation.
# How to run:
#   1) Ensure Flask is installed:  pip install flask
#   2) Start the app:           python calculator.py
#   3) Open your browser at:    http://127.0.0.1:5000/

from __future__ import annotations
from flask import Flask, request, render_template_string
from typing import Optional

app = Flask(__name__)

PAGE_TEMPLATE = """
<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>Simple Calculator</title>
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 2rem; }
    .card { max-width: 520px; padding: 1.25rem 1.5rem; border: 1px solid #e5e7eb; border-radius: 12px; box-shadow: 0 1px 2px rgba(0,0,0,0.04); }
    label { display:block; font-weight:600; margin-top: 0.75rem; }
    input[type=\"number\"] { width:100%; padding:0.5rem; margin-top:0.25rem; border:1px solid #d1d5db; border-radius:8px; }
    .ops { display:flex; gap: 0.75rem; margin: 0.75rem 0 0.25rem; flex-wrap: wrap; }
    .ops label { font-weight:500; display:flex; align-items:center; gap:0.35rem; }
    button { margin-top: 1rem; padding: 0.6rem 1rem; background:#2563eb; color:#fff; border:none; border-radius:8px; cursor:pointer; }
    button:hover { background:#1d4ed8; }
    .result { margin-top: 1rem; font-size: 1.125rem; font-weight: 600; }
    .error { color: #b91c1c; }
    .muted { color:#6b7280; font-size: 0.9rem; }
  </style>
</head>
<body>
  <div class=\"card\">
    <h1>Simple Calculator</h1>
    <p class=\"muted\">Enter two numbers and choose an operation.</p>

    <form method=\"post\" action=\"/calculate\">\n      <label for=\"a\">First number</label>\n      <input id=\"a\" name=\"a\" type=\"number\" step=\"any\" required value=\"{{ a if a is not none else '' }}\">\n\n      <label for=\"b\">Second number</label>\n      <input id=\"b\" name=\"b\" type=\"number\" step=\"any\" required value=\"{{ b if b is not none else '' }}\">\n\n      <label>Operation</label>\n      <div class=\"ops\">\n        <label><input type=\"radio\" name=\"op\" value=\"plus\"      {% if op == 'plus' %}checked{% endif %}> Plus</label>\n        <label><input type=\"radio\" name=\"op\" value=\"minus\"     {% if op == 'minus' %}checked{% endif %}> Subtraction</label>\n        <label><input type=\"radio\" name=\"op\" value=\"times\"     {% if op == 'times' %}checked{% endif %}> Times By</label>\n        <label><input type=\"radio\" name=\"op\" value=\"divide\"    {% if op == 'divide' %}checked{% endif %}> Divide By</label>\n      </div>\n\n      <button type=\"submit\">Calculate</button>\n    </form>\n\n    {% if error %}\n      <div class=\"result error\">Error: {{ error }}</div>\n    {% elif result is not none %}\n      <div class=\"result\">Result: {{ result }}</div>\n    {% endif %}\n  </div>\n</body>\n</html>\n"""


def compute(a: float, b: float, op: str) -> float:
    """Compute the operation on a and b.

    Args:
        a: First number
        b: Second number
        op: One of 'plus', 'minus', 'times', 'divide'
    Returns:
        The computed float result.
    Raises:
        ValueError: If op is invalid or division by zero occurs.
    """
    if op == "plus":
        return a + b
    elif op == "minus":
        return a - b
    elif op == "times":
        return a * b
    elif op == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Invalid operation.")


@app.route("/", methods=["GET"]) 
def index():
    # Initial page load with empty fields
    return render_template_string(PAGE_TEMPLATE, a=None, b=None, op="plus", result=None, error=None)


@app.route("/calculate", methods=["POST"]) 
def calculate():
    a_raw: Optional[str] = request.form.get("a")
    b_raw: Optional[str] = request.form.get("b")
    op: str = request.form.get("op", "plus")

    error: Optional[str] = None
    result: Optional[float] = None

    try:
        if a_raw is None or b_raw is None:
            raise ValueError("Both numbers are required.")
        a = float(a_raw)
        b = float(b_raw)
        result = compute(a, b, op)
    except ValueError as e:
        error = str(e)

    # Re-render page with the result or error and preserve inputs
    return render_template_string(PAGE_TEMPLATE, a=a_raw, b=b_raw, op=op, result=result, error=error)


if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True)
