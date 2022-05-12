from flask import Flask, Response, redirect, url_for

app = Flask(__name__)


@app.route("/")
def start_page():
    return Response("", status=200)


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('start_page'))


if __name__ == "__main__":
    app.run()
