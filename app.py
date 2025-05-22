from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_data_types():
    # Sample values of different data types
    data = {
        "Integer": (25, type(25).__name__),
        "Float": (5.9, type(5.9).__name__),
        "String": ("Alice", type("Alice").__name__),
        "Boolean": (True, type(True).__name__),
        "List": (["apple", "banana", "cherry"], type(["apple", "banana", "cherry"]).__name__),
        "Tuple": ((10, 20), type((10, 20)).__name__),
        "Set": ({1, 2, 3}, type({1, 2, 3}).__name__),
        "Dictionary": ({"name": "Bob", "age": 30}, type({"name": "Bob", "age": 30}).__name__)
    }
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
