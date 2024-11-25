class frontend:
    def __init__(self):
        self.business_structure = {
            "name": "",
            "status": "",
        }
        self.account_structure = {
            "username": "",
            "password_hash": "",
            "status": "active",
        }
        self.meeting_structure = {
            "Nosaukums": "",
            "Datums": "",
            "Laiks": "",
            "Tips": "",
        }
        return

    def menu(self):
        print()
        print("what do you want to test?")
        print()
        mode = input(
            "1 for registration(no hashing yet); 2 for login(partially implemented); 3 for creating meeting; 4 for searching for meeting(partially implemented); 5 for premium(partially implemented); 6 for database dump(for development only);  "
        )
        print()
        return mode

    def registration(self):
        username = input("username: ")
        password_hash = input("password: ")
        account = self.account_structure
        account["username"] = username
        account["password_hash"] = password_hash
        return account

    def premium(self):
        user = input("who wants it? (username for premium): ")
        return user

    def creating(self):
        meeting = self.meeting_structure
        meeting["Nosaukums"] = input("Nosaukums: ")
        meeting["Datums"] = input("Datums: ")
        meeting["Laiks"] = input("Laiks: ")
        meeting["Tips"] = input("Tips: ")
        return meeting

    def login(self):
        username = input("username: ")
        password = input("password: ")
        return [username, password]

    def search(self):
        options = {
            "1": "Nosaukums",
            "2": "Datums",
            "3": "Laiks",
            "4": "Tips",
        }
        key = input(
            "by what you want to search (options: 1 - Nosaukums; 2 - Datums; 3 - Laiks; 4 - Tips;): "
        )
        option = options.get(key)
        value = input("value: ")
        return [option, value]

    def show(self, meeting):
        print()
        print(meeting)
        return
