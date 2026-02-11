# This file scans the database for missing tables and creates them if they are missing.
# Tables:
# reminderData: user_id, reminder_id, time, reason
# softbannedMembers: user_id, guild_id, time, reason
# suspentionData: user_id, time, reason
from config import db
from sqlite3 import Error
from os import path

def check_db():
    try:
        if path.exists("database.db"):
            print("Database found. Checking for missing tables...")
            cursor = db.cursor()
            
            # Currency table
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='currency'"
            )
            if cursor.fetchone() is None:
                print("Creating currency table...")
                cursor.execute(
                    "CREATE TABLE currency (user_id INTEGER PRIMARY KEY, qp INTEGER DEFAULT 0, credits INTEGER DEFAULT 0)"
                )
                print("Currency table created.")
            else:
                print("Currency table found.")

            # reminderData table
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='reminderData'"
            )
            if cursor.fetchone() is None:
                print("Creating reminderData table...")
                cursor.execute(
                    "CREATE TABLE reminderData (user_id INTEGER, reminder_id INTEGER, time TEXT, reason TEXT)"
                )
                print("reminderData table created.")
            else:
                print("reminderData table found.")

            # softbannedMebers table
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='softbannedMembers'"
            )
            if cursor.fetchone() is None:
                print("Creating softbannedMembers table...")
                cursor.execute(
                    "CREATE TABLE softbannedMembers (user_id INTEGER, guild_id INTEGER, time TEXT, reason TEXT)"
                )
                print("softbannedMembers table created.")
            else:
                print("softbannedMembers table found.")

            # suspentionData table
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='suspentionData'"
            )
            if cursor.fetchone() is None:
                print("Creating suspentionData table...")
                cursor.execute(
                    "CREATE TABLE suspentionData (user_id INTEGER, time TEXT, reason TEXT)"
                )
                print("suspentionData table created.")
            else:
                print("suspentionData table found.")

    except Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_db()
