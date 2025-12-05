from flask import Flask, request

app = Flask(__name__)
db = []


def helper_function(m: int, n: int) -> int:
    return m + n


def add_to_database(username):
    db.append(username)


@app.route('/ping')
def ping():
    return {'status': 'ok'}


@app.route('/add', methods=["POST"])
def add_user():
    username = request.json['username']
    add_to_database(username)
    return {'status': 'ok'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
