# import json


class db:
    __db_data__ = {}

    def __init__(self):
        self.__db_data__ = {
            "businesses": [
                {
                    "name": "rtu",
                    "status": "premium",
                },
                {
                    "name": "lu",
                    "status": "active",
                },
            ],
            "accounts": [
                {"username": "Lukas", "password_hash": "ruf43nf#", "status": "premium"},
                {
                    "username": "Karlis",
                    "password_hash": "ruf46nf#",
                    "status": "premium",
                },
            ],
            "meetings": [
                {
                    "Nosaukums": "Annual meeting",
                    "Datums": "24.11.2025",
                    "Laiks": "15:00",
                    "Tips": "Online",
                },
                {
                    "Nosaukums": "test",
                    "Datums": "24.11.2025",
                    "Laiks": "15:00",
                    "Tips": "test",
                },
            ],
        }
        return

    def __read_table__(self, table: str):
        result = self.__db_data__.get(table)
        return result

    def read_row(self, table: str, key: str, value: str):
        table = self.__read_table__(table)
        rows = []
        for row in table:
            if row.get(key) == value:
                rows.append(row)
        return rows

    def write_to_table(self, table: str, data):
        table_data = self.__db_data__.get(table)
        table_data.append(data)
        self.__db_data__[table] = table_data
        return

    def change_first_row(
        self, table: str, key: str, value: str, change_key: str, change_value: str
    ):
        """changes first row with the same key (only docstring here, cuz hard to understand what this does)

        Args:
            table (str): where
            key (str): key to search for
            value (str): value of that key
            change_key (str): key of value to change
            change_value (str): to what change it
        """
        table_data = self.__read_table__(table)
        index = -1
        for row in table_data:
            index = index + 1
            if row.get(key) == value:
                break

        self.__db_data__[table][index][change_key] = change_value
        return
