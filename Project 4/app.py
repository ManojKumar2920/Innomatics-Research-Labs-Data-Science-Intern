from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def Home ():
    return 'Welcome to Home Page & Please go to uppercase page '

@app.route('/uppercase')
def uppercase():
    name = request.args.get("user")
    return (f"Welcome to CodersCave {name.upper()}")


if(__name__ == "__main__"):
    app.run(debug=True)
