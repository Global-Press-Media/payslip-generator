from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Luckman! Your payslip generator is alive."

if __name__ == '__main__':
    app.run(debug=True)
