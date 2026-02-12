# This file scans the database for missing tables and creates them if they are missing.
from config import db
from sqlite3 import Error
from os import path

def check_db():
    try:
        if path.exists("database.db"):
            print("Database found. Checking for missing tables...")
            cursor = db.cursor()
            
            tables = {
                "currency": "CREATE TABLE currency (user_id INTEGER PRIMARY KEY, qp INTEGER DEFAULT 0, credits INTEGER DEFAULT 0)",
                "reminderData": "CREATE TABLE reminderData (user_id INTEGER, reminder_id INTEGER, time TEXT, reason TEXT)",
                "softbannedMebers": "CREATE TABLE softbannedMebers (user_id INTEGER, guild_id INTEGER, time TEXT, reason TEXT)",
                "suspentionData": "CREATE TABLE suspentionData (user_id INTEGER, time TEXT, reason TEXT)",
                "botbannedData": "CREATE TABLE botbannedData (user_id INTEGER PRIMARY KEY, reason TEXT)",
                "devWarnData": "CREATE TABLE devWarnData (user_id INTEGER, reason TEXT, warn_id INTEGER, revoke_date INTEGER)",
                "suspensionData": "CREATE TABLE suspensionData (user, modules, timeout)",
                "bankData": "CREATE TABLE bankData (user_id INTEGER PRIMARY KEY, amount INTEGER DEFAULT 0, claimed_date INTEGER)",
                "userWallpaperInventory": "CREATE TABLE userWallpaperInventory (user_id INTEGER, wallpaper TEXT, link TEXT, brightness INTEGER, selected INTEGER, country TEXT)",
                "wallpapers": "CREATE TABLE wallpapers (name TEXT PRIMARY KEY, link TEXT, price INTEGER)",
                "userBio": "CREATE TABLE userBio (user_id INTEGER PRIMARY KEY, bio TEXT, color TEXT)",
                "serverxpData": "CREATE TABLE serverxpData (guild_id INTEGER, user_id INTEGER, lvl INTEGER, exp INTEGER, next_time INTEGER, cumulative_exp INTEGER)",
                "globalxpData": "CREATE TABLE globalxpData (user_id INTEGER PRIMARY KEY, lvl INTEGER, exp INTEGER, next_time INTEGER, cumulative_exp INTEGER)",
                "serverData": "CREATE TABLE serverData (server INTEGER PRIMARY KEY, levelup_message TEXT, levelup_channel INTEGER, rankup_update INTEGER)",
                "confessData": "CREATE TABLE confessData (server_id INTEGER, channel_id INTEGER)",
                "welcomerData": "CREATE TABLE welcomerData (server_id INTEGER PRIMARY KEY, welcome_channel INTEGER, goodbye_channel INTEGER, welcome_msg TEXT, goodbye_msg TEXT)"
            }

            for table_name, create_sql in tables.items():
                cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
                if cursor.fetchone() is None:
                    print(f"Creating {table_name} table...")
                    cursor.execute(create_sql)
                    print(f"{table_name} table created.")
                else:
                    print(f"{table_name} table found.")
            
            db.commit()

    except Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_db()
