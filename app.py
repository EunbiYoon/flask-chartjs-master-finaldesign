from flask import Flask, render_template, json

app = Flask(__name__)

@app.route("/")
def chart():
    legend = 'Monthly Data'
    labels = [1,2,3,4,5,6,7,8]
    values = [10, 9, 8, 7, 6, 4, 7, 30]
    return render_template('index.html', values=values, labels=labels, legend=legend)

if __name__ == "__main__":
    app.run(debug=True)