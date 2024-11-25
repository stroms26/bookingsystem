from db_dummy import db
from frontend_dummy import frontend

# TODO: implement normal frontend, db and async


class backend:
    def __init__(self):
        print("Initializing database...")
        self.database = db()
        print("Database initialized")

        print("Testing database")
        if self.database.read_row("meetings", "Tips", "test")[0] == {
            "Nosaukums": "test",
            "Datums": "24.11.2025",
            "Laiks": "15:00",
            "Tips": "test",
        }:
            print("Database works")
        else:
            print("Database doesn't work")

        print("Initializing frontend...")
        self.frontend = frontend()
        print("Frontend initialized")
        print("")

    def cli_frontend(self):  # temporary
        print("for development")
        while True:
            mode = self.frontend.menu()

            match mode:
                case "1":
                    self.database.write_to_table(
                        "accounts", self.frontend.registration()
                    )
                case "2":
                    user = self.frontend.login()
                    self.login(user[0], user[1])
                case "3":
                    self.database.write_to_table("meetings", self.frontend.creating())
                case "4":
                    meeting = self.frontend.search()
                    self.search(meeting[0], meeting[1])
                case "5":
                    username = self.frontend.premium()
                    self.database.change_first_row(
                        "accounts", "username", username, "status", "premium"
                    )
                case "6":
                    print(self.database.__db_data__)
                case _:
                    return
        return

    def login(self, username: str, password_hash: str):
        user = self.database.read_row("accounts", "username", username)[0]
        if user.get("password_hash") == password_hash:
            print("Login succesfull")
        else:
            print("No!")

    def search(self, key: str, value: str):
        rows = self.database.read_row("meetings", key, value)
        for row in rows:
            self.frontend.show(row)


if __name__ == "__main__":
    be = backend()
    be.cli_frontend()
