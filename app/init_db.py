import sqlite3

conn = sqlite3.connect("restaurants.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    meal TEXT
)
""")

restaurants = [
    ("Pizza Hut", "pizza"),
    ("Burger King", "burger"),
    ("Sushi Place", "sushi"),
    ("Arab Grill", "shawarma")
]

c.executemany("INSERT INTO restaurants (name, meal) VALUES (?, ?)", restaurants)

conn.commit()
conn.close()
