from flask import Flask, request
from database import Database

app = Flask(__name__)
db = Database()


def helper_function(m, n):
    return m + n


@app.route('/ping')
def ping():
    return {'status': 'ok'}


@app.route('/users', methods=["POST"])
def create_user():
    data = request.get_json()

    username = data['username']
    firstname = data['firstname']
    lastname = data['lastname']

    db.add_user(username, firstname, lastname)

    return {
        "username": username,
        "firstname": firstname,
        "lastname": lastname
    }, 201


@app.route('/users/<username>', methods=["GET"])
def get_user(username):
    user = db.get_user(username)

    if not user:
        return {"error": "User not found"}, 404

    return user, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
