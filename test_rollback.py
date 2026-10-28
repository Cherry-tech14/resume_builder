import sqlite3

# Create a temporary database in memory
connection = sqlite3.connect(":memory:")

# Create a test table
connection.execute(
    "CREATE TABLE test_resumes (id INTEGER, name TEXT)"
)

try:
    # Start a transaction
    connection.execute("BEGIN")

    # Save a test resume
    connection.execute(
        "INSERT INTO test_resumes VALUES (1, 'Test User')"
    )

    # Simulate an error
    raise ValueError("Something went wrong!")

    # This line will not run
    connection.commit()

except ValueError:
    connection.rollback()
    print("Error occurred. Transaction rolled back.")

# Check whether the resume was saved
result = connection.execute(
    "SELECT COUNT(*) FROM test_resumes"
).fetchone()[0]

print("Number of saved resumes:", result)

connection.close()