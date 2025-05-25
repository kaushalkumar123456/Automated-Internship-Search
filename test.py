import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="internship"
    )
    print("Connected successfully!")
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Replace these with your actual database credentials
DB_CONFIG = {
    "host": "localhost",
    "user": "root",   # Change if your MySQL has a different username
    "password": "",   # Change if you have set a password
    "database": "internship"  # Change to your actual database name
}

def store_results_in_db():
    """Stores static internship results in MySQL database for testing."""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Define a static internship record for testing
        static_results = [
            ("Software Engineer Intern", "https://example.com/se-intern", "Software Internship"),
            ("Data Science Intern", "https://example.com/ds-intern", "Data Science Internship"),
            ("Cybersecurity Intern", "https://example.com/cyber-intern", "Cybersecurity Internship")
        ]

        insert_query = """
        INSERT INTO internships (title, link, search_query)
        VALUES (%s, %s, %s)
        """
        
        cursor.executemany(insert_query, static_results)
        conn.commit()

        print(f"{cursor.rowcount} records inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# Call the function to insert test data
store_results_in_db()