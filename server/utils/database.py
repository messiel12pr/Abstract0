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

    def create_user(self, user_id: int, name: str):
        try:
            with self.engine.connect() as conn:
                query = text("INSERT INTO user (user_id, user_name) \
                                   VALUES (:user_id, :user_name)")
                params = {"user_id": user_id, "user_name": name,}
                conn.execute(query, params)

        except Exception as e:  
            print(e.__str__())

    def get_user(self, user_id: int):
        try:
            with self.engine.connect() as conn:
                query = text("SELECT * FROM user WHERE user_id = (:user_id)")
                params = {"user_id": user_id}
                return conn.execute(query, params).all()

        except Exception as e:  
            print(e.__str__())

    def create_submission_details(self, problem_id: int, result: str, last_submission_date: str, time_taken: str, user_id: int):
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
                return conn.execute(query, params).all()

        except Exception as e:  
            print(e.__str__())

    def get_submission_details_id(self, user_id: int):
        try:
            with self.engine.connect() as conn:
                query = text("SELECT submission_details_id FROM submission_details WHERE user_id = (:user_id)")
                params = {"user_id": user_id,}
                return conn.execute(query, params).all()

        except Exception as e:  
            print(e.__str__())

    def create_problem_category(self, title: str, author: str, creation_date: str):
        try:
            with self.engine.connect() as conn:
                query = text("INSERT INTO problem_category (problem_category_title, author, creation_date) \
                                   VALUES (:problem_category_title, :author, :creation_date)")
                params = {"problem_category_title": title, "author": author, "creation_date": creation_date}
                conn.execute(query, params)

        except Exception as e:  
            print(e.__str__())

    def get_problem_category_id(self, title, author):
        try:
            with self.engine.connect() as conn:
                query = text("SELECT problem_category_id FROM problem_category WHERE problem_category_title = (:title) AND author = (:author)")
                params = {"title": title, "author": author}
                return conn.execute(query, params).all()

        except Exception as e:  
            print(e.__str__())

    def create_problem(self, problem_category_id: int, title: str, location: str, difficulty: str, hint: str):
        try:
            with self.engine.connect() as conn:
                query = text("INSERT INTO problem (problem_category_id, problem_title, problem_location, problem_difficulty, hint) \
                                   VALUES (:problem_category_id, :problem_title, :problem_location, :problem_difficulty, :hint)")
                params = {"problem_category_id": problem_category_id, "problem_title": title, "problem_location": location, "problem_difficulty": difficulty, "hint": hint}
                conn.execute(query, params)

        except Exception as e:  
            print(e.__str__())

    def get_problem(self, problem_id: int):
        try:
            with self.engine.connect() as conn:
                query = text("SELECT * FROM problem WHERE problem_id = (:problem_id)")
                params = {"problem_id": problem_id}
                return conn.execute(query, params).all()

        except Exception as e:  
            print(e.__str__()) 

    def get_problem_id(self, problem_category_id: int, problem_title: str):
        try:
            with self.engine.connect() as conn:
                query = text("SELECT problem_id FROM problem WHERE problem_category_id = (:problem_category_id) AND problem_title = (:problem_title)")
                params = {"problem_category_id": problem_category_id, "problem_title": problem_title}
                return conn.execute(query, params).all()

        except Exception as e:  
            print(e.__str__())

    def count_problems_solved(self, user_id: int):
        try:
            with self.engine.connect() as conn:
                query = text("SELECT COUNT(*) AS row_count FROM submission_details WHERE user_id = (:user_id)")
                params = {"user_id": user_id}
                return conn.execute(query, params).all()

        except Exception as e:  
            print(e.__str__())