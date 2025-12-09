class Database:
    def __init__(self):
        self.db = []

    def add_user(self, username, firstname, lastname):
        self.db.append({'username':username, 'firstname': firstname, 'lastname': lastname})

    def get_user(self, username):
        for user in self.db:
            if user.get('username') == username:
                return user
        return {}

