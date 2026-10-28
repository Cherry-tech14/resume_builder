import sqlite3
import tempfile
from pathlib import Path
from unittest.mock import patch

import database


with tempfile.TemporaryDirectory() as folder:
    test_db = Path(folder) / "test.db"

    # Create a separate test database
    with sqlite3.connect(test_db) as connection:
        connection.execute(
            "CREATE TABLE test_data (name TEXT)"
        )

    # Redirect our database manager to the test database
    test_manager = database.DatabaseManager()

    original_connect = sqlite3.connect

    def connect_to_test_database(*args, **kwargs):
        return original_connect(test_db, **kwargs)

    with patch.object(database.sqlite3, "connect", connect_to_test_database):
        with patch.object(database, "manager", test_manager):
            with patch.object(database.connection, "manager", test_manager):

                try:
                    with database.transaction():
                        database.connection.execute(
                            "INSERT INTO test_data VALUES (?)",
                            ("Test User",)
                        )

                        # Simulate a database-saving error
                        raise ValueError("Simulated error")

                except ValueError:
                    print("Simulated error caught.")

                result = database.connection.execute(
                    "SELECT COUNT(*) FROM test_data"
                ).fetchone()[0]

                print("Records remaining:", result)

                test_manager.get_connection().close()