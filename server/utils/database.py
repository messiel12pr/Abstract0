import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

class Database:
    def __init__(self):
        load_dotenv()

        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USERNAME"),
        password = os.getenv("DB_PASSWORD"),
        db = os.getenv("DB_NAME"),

        self.engine = create_engine (
        f"mysql+pymysql://{user[0]}:{password[0]}@{host[0]}/{db[0]}?charset=utf8mb4",
        connect_args = {
            "ssl": {
                "ssl_ca": "/etc/ssl/cert.pem"
            }
        })

    def set_user(self):
        try:
            with self.engine.connect() as conn:
                query = text("INSERT INTO user (user_id, user_name) VALUES (:user_id, :user_name)")
                params = {"user_id": 95717805, "user_name": "Joel"}
                conn.execute(query, params)

        except Exception as e:  
            print(e.__str__())

    def get_user(self, user_id: int):
        try:
            with self.engine.connect() as conn:
                query = text("SELECT * FROM user WHERE user_id = (:user_id)")
                params = {"user_id": user_id,}
                return conn.execute(query, params)

        except Exception as e:  
            print(e.__str__())

db = Database()
print(db.get_user(95717805).all())