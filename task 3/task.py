from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/gallery")
def gallery():
    return render_template("carousel.html", title='Карусель')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
