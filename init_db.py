import sqlite3

# Create or connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL
)
""")

# Insert dummy data
cursor.execute("INSERT INTO users (username) VALUES ('admin')")
cursor.execute("INSERT INTO users (username) VALUES ('test')")

conn.commit()
conn.close()

print("Database initialized ✅")
