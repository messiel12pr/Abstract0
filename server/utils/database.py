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

    def create_user(self, user_id: int, name: str, submission_details_id: int):
        try:
            with self.engine.connect() as conn:
                query = text("INSERT INTO user (user_id, user_name, submission_details_id) \
                                   VALUES (:user_id, :user_name, :submission_details_id)")
                params = {"user_id": user_id, "user_name": name, "submission_details_id": submission_details_id}
                conn.execute(query, params)

        except Exception as e:  
            print(e.__str__())

    def set_user_submission_details_id(self, user_id: int, submission_details_id: int):
        try:
            with self.engine.connect() as conn:
                query = text("UPDATE user SET submission_details_id = (:submission_details_id) \
                               WHERE user_id = (:user_id)")
                params = {"submission_details_id": submission_details_id, "user_id": user_id}
                conn.execute(query, params)

        except Exception as e:  
            print(e.__str__())

    def get_user(self, user_id: int):
        try:
            with self.engine.connect() as conn:
                query = text("SELECT * FROM user WHERE user_id = (:user_id)")
                params = {"user_id": user_id}
                return conn.execute(query, params)

        except Exception as e:  
            print(e.__str__())

    def create_submission_details(self, problem_id: int, result: str, last_submission_date: str, time_taken: str, user_id: str):
        try:
            with self.engine.connect() as conn:
                query = text("INSERT INTO submission_details (problem_id, result, last_submission_date, time_taken_minutes, user_id) \
                                   VALUES (:problem_id, :result, :last_submission_date, :time_taken_minutes, :user_id)")
                params = {"problem_id": problem_id, "result": result, "last_submission_date": last_submission_date, "time_taken_minutes": time_taken, "user_id": user_id}
                conn.execute(query, params)

        except Exception as e:  
            print(e.__str__())

    def get_submission_details(self, user_id: int):
        try:
            with self.engine.connect() as conn:
                query = text("SELECT * FROM submission_details WHERE user_id = (:user_id)")
                params = {"user_id": user_id,}
                return conn.execute(query, params)

        except Exception as e:  
            print(e.__str__())
    
    def get_submission_details_id(self, user_id: int):
        try:
            with self.engine.connect() as conn:
                query = text("SELECT submission_details_id FROM submission_details WHERE user_id = (:user_id)")
                params = {"user_id": user_id,}
                return conn.execute(query, params)

        except Exception as e:  
            print(e.__str__())