from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/form", methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template("base.html", title='Анкета')
    elif request.method == 'POST':
        print(request.form['full_name'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['study'])
        print(request.form['about'])
        print(request.form['profession'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
