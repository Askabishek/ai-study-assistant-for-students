import sqlite3

conn = sqlite3.connect("study.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE study_materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    topic TEXT,
    notes TEXT,
    faculty TEXT
)
""")

# Insert data
cursor.executemany("""
INSERT INTO study_materials (subject, topic, notes, faculty)
VALUES (?, ?, ?, ?)
""", [
    ("AI", "Machine Learning", "ML basics and algorithms", "Dr. Kumar"),
    ("DSA", "Trees", "Binary trees and traversal", "Prof. Anitha"),
    ("DBMS", "Normalization", "1NF 2NF 3NF concepts", "Dr. Ravi"),
    ("AI", "Deep Learning", "Neural networks basics", "Dr. Kumar")
])

conn.commit()
conn.close()

print("✅ Database created successfully!")
