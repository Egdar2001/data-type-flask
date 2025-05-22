from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def show_data_types():
    predefined_data = {
        "Integer": (25, type(25).__name__),
        "Float": (5.9, type(5.9).__name__),
        "String": ("Alice", type("Alice").__name__),
        "Boolean": (True, type(True).__name__),
        "List": (["apple", "banana", "cherry"], type(["apple", "banana", "cherry"]).__name__),
        "Tuple": ((10, 20), type((10, 20)).__name__),
        "Set": ({1, 2, 3}, type({1, 2, 3}).__name__),
        "Dictionary": ({"name": "Bob", "age": 30}, type({"name": "Bob", "age": 30}).__name__)
    }

    user_input = None
    input_type = None

    if request.method == 'POST':
        raw_input = request.form['value']
        try:
            # Evaluate input as Python literal
            evaluated = eval(raw_input)
            user_input = evaluated
            input_type = type(evaluated).__name__
        except Exception as e:
            user_input = str(raw_input)
            input_type = "String (default or invalid literal)"

    return render_template("index.html", data=predefined_data, user_input=user_input, input_type=input_type)

if __name__ == "__main__":
    app.run(debug=True)
