import mysql.connector
from werkzeug.security import generate_password_hash

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'singh@sneha25',
    'database': 'petAdoption'
}

def get_connection():
    return mysql.connector.connect(**db_config)

def insert_user(username,email, hashed_password,role="user"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username,email, password) VALUES (%s, %s, %s)", (username,email, hashed_password))
    conn.commit()
    cursor.close()
    conn.close()

def update_user_password(username, new_password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
    conn.commit()
    cursor.close()
    conn.close()

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT username, password, role FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


if __name__ == "__main__":
    update_user_password("admin", generate_password_hash("admin123"))
    print("Admin password updated successfully.")


