import datetime
import pytest

from server.utils.database import Database

db = Database()

def test_problem_category_creation():
    db.create_problem_category("Linked List", "Joel M. Gonzalez", "2024-01-12")
    assert db.get_problem_category_id("Linked List", "Joel M. Gonzalez") == [(1,)]

def test_problem_creation():
    db.create_problem(1, "Append node to list", "/problems/linked_list", "Easy", "Use the tail of the linked list")
    assert db.get_problem_id(1, "Append node to list") == [(1, )]

def test_user_creation():
    db.create_user(12345, 'test_user')
    assert db.get_user(12345) == [(12345, 'test_user')]

def test_submission_details_creation():
    db.create_submission_details(1, "Accepted", "2024-01-12", "0", 12345)
    assert db.get_submission_details(12345) == [(1, 1, 'Accepted', datetime.date(2024, 1, 12), 0, 12345)]