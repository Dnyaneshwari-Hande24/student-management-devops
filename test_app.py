from app import greet_student, validate_student


def test_greet_student():
    assert greet_student("Student") == "Welcome, Student!"


def test_valid_student_name():
    assert validate_student("Rahul") is True


def test_empty_student_name():
    assert validate_student("") is False
